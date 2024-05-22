import tkinter as tk
from PIL import Image, ImageTk


class BouncingLogo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bouncing Logo")
        self.geometry("800x600")
        self.resizable(False, False)
        self.canvas = tk.Canvas(self, bg="black", width=800, height=600)
        self.canvas.pack()

        self.logo_image = Image.open("logo.png")
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo = self.canvas.create_image(0, 0, anchor="nw", image=self.logo_image)

        self.dx = 5
        self.dy = 5

        self.animate()

    def animate(self):
        self.move_logo()
        self.after(50, self.animate)

    def move_logo(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.logo)
        if x1 <= 0 or x2 >= self.canvas.winfo_width():
            self.dx = -self.dx
        if y1 <= 0 or y2 >= self.canvas.winfo_height():
            self.dy = -self.dy

        self.canvas.move(self.logo, self.dx, self.dy)


if __name__ == "__main__":
    app = BouncingLogo()
    app.mainloop()

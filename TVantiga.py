import tkinter as tk

class BouncingLogo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bouncing Logo")
        self.geometry("600x400")
        self.resizable(False, False)
        self.canvas = tk.Canvas(self, bg="black", width=600, height=400)
        self.canvas.pack()

        self.logo = self.canvas.create_oval(10, 10, 50, 50, fill="red")
        self.dx = 5
        self.dy = 5

        self.animate()

    def animate(self):
        self.move_logo()
        self.after(50, self.animate)

    def move_logo(self):
        x1, y1, x2, y2 = self.canvas.coords(self.logo)
        if x1 <= 0 or x2 >= self.canvas.winfo_width():
            self.dx = -self.dx
        if y1 <= 0 or y2 >= self.canvas.winfo_height():
            self.dy = -self.dy

        self.canvas.move(self.logo, self.dx, self.dy)

if __name__ == "__main__":
    app = BouncingLogo()
    app.mainloop()

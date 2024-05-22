import tkinter as tk 


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("400x600")
        self.resizable(0, 0)
        self.result_var = tk.StringVar()
        self.create_display()
        self.create_buttons()

    def create_display(self):
        display = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14,
                           borderwidth=4)
        display.grid(row=0, column=0, columnspan=4)

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row = 1
        col = 0

        for button in buttons:
            if button == '=':
                btn = tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=self.calculate_result)
            elif button == 'C':
                btn = tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=self.clear_display)
            else:
                btn = tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18),
                                command=lambda b=button: self.append_to_display(b))

            btn.grid(row=row, column=col, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1


        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

    def append_to_display(self, value):
        current_text = self.result_var.get()
        new_text = current_text + value
        self.result_var.set(new_text)

    def clear_display(self):
        self.result_var.set("")

    def calculate_result(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Erro")
            self.after(1500, self.clear_display)  # Limpa o display após 1.5 segundos se houver erro
if __name__ == "__main__":
    calc = Calculator()
    calc.mainloop()

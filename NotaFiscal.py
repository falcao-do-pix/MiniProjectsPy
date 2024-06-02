import tkinter as tk
from tkinter import ttk, messagebox


# Função para adicionar um item à lista de compras
def adicionar_item():
    nome_item = entry_nome.get()
    preco_item = entry_preco.get()
    quantidade_item = entry_quantidade.get()

    if nome_item and preco_item and quantidade_item:
        try:
            preco_item = float(preco_item)
            quantidade_item = int(quantidade_item)
            total_item = preco_item * quantidade_item

            lista_itens.append((nome_item, preco_item, quantidade_item, total_item))
            atualizar_lista()
            limpar_campos()
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser um número e Quantidade deve ser um número inteiro.")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")


# Função para atualizar a lista de itens na interface
def atualizar_lista():
    for i in tree.get_children():
        tree.delete(i)

    total_compra = 0
    for item in lista_itens:
        tree.insert("", "end", values=item)
        total_compra += item[3]

    label_total['text'] = f"Total: R${total_compra:.2f}"


# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)


# Função para gerar e salvar a nota fiscal em um arquivo de texto
def gerar_nota_fiscal():
    if lista_itens:
        with open("nota_fiscal.txt", "w") as f:
            f.write("Nota Fiscal\n")
            f.write("=============\n")
            total_compra = 0
            for item in lista_itens:
                f.write(f"{item[0]} - R${item[1]:.2f} x {item[2]} = R${item[3]:.2f}\n")
                total_compra += item[3]
            f.write("=============\n")
            f.write(f"Total: R${total_compra:.2f}\n")
        messagebox.showinfo("Nota Fiscal", "Nota fiscal gerada com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Nenhum item para gerar nota fiscal.")


# Configuração inicial da janela principal
root = tk.Tk()
root.title("Sistema de Notas Fiscais")
root.geometry("600x400")

# Lista para armazenar os itens
lista_itens = []

# Frame para os campos de entrada
frame_inputs = ttk.Frame(root)
frame_inputs.pack(pady=10)

ttk.Label(frame_inputs, text="Nome do Item:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = ttk.Entry(frame_inputs)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Preço:").grid(row=1, column=0, padx=5, pady=5)
entry_preco = ttk.Entry(frame_inputs)
entry_preco.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_inputs, text="Quantidade:").grid(row=2, column=0, padx=5, pady=5)
entry_quantidade = ttk.Entry(frame_inputs)
entry_quantidade.grid(row=2, column=1, padx=5, pady=5)

ttk.Button(frame_inputs, text="Adicionar Item", command=adicionar_item).grid(row=3, columnspan=2, pady=10)

# Treeview para exibir a lista de itens
columns = ("Nome do Item", "Preço", "Quantidade", "Total")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Nome do Item", text="Nome do Item")
tree.heading("Preço", text="Preço")
tree.heading("Quantidade", text="Quantidade")
tree.heading("Total", text="Total")
tree.pack(pady=10)

# Label para exibir o total da compra
label_total = ttk.Label(root, text="Total: R$0.00")
label_total.pack(pady=10)

# Botão para gerar a nota fiscal
ttk.Button(root, text="Gerar Nota Fiscal", command=gerar_nota_fiscal).pack(pady=10)

# Iniciar o loop da interface
root.mainloop()

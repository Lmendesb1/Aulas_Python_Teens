import tkinter as tk

# Criar a janela principal
janela = tk.Tk()

# Configurar a janela
janela.title("Minha Janela Simples")  # Título da janela
janela.geometry("800x600")  # Tamanho da janela (largura x altura)
janela.resizable(False, False)  # Impede redimensionamento da janela

# Adicionar um rótulo (texto)
label = tk.Label(janela, text="Olá, alunos!", font=("Arial", 16))
label.pack(pady=20)  # Adicionar espaçamento vertical (20px)

# Adicionar um botão
def clique_do_botao():
    label.config(text="Você clicou no botão!")

botao = tk.Button(janela, text="Clique Aqui", command=clique_do_botao)
botao.pack(pady=10)

# Executar o loop principal
janela.mainloop()

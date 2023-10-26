import tkinter as tk

janela = tk.Tk()
janela.title("GUI com Tkinter")
botao = tk.Button(janela, text = "Botão de tela", fg = "blue").pack(side = 'left')
janela.mainloop()
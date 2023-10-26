import tkinter as tk

class Application:

    def __init__(self, master = None):

        janela.title("GUI com Tkinter")
        botao = tk.Button(janela, text = "Botão")
        botao.pack()

janela = tk.Tk()
Application(janela)
janela.mainloop()
import tkinter as tk
from tkinter import *

class Application:

    def __init__(self, master = None):

        janela.title("GUI com Tkinter")
        self.tela1 = Frame(master)
        self.tela1.pack()
        self.msg = Label(self.tela1, text = "Hello World! 1")
        self.msg.pack()
        self.botao = Button(self.tela1, text = "Fechar", command = self.tela1.quit)
        self.botao.pack()
        self.tela2 = Frame(master)
        self.tela2.pack()
        self.msg = Label(self.tela2, text = "Hello World! 2")
        self.msg.pack()
        self.botao = Button(self.tela2, text = "Cancelar", command = self.tela2.quit)
        self.botao.pack()

janela = tk.Tk()
Application(janela)
janela.mainloop()
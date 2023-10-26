import tkinter as tk
from tkinter import *

class Application:

    def __init__(self, master = None):

        janela.title("GUI em Tkinter")
        self.tela1 = Frame(master)
        self.tela1.pack()
        self.msg = Label(self.tela1)
        self.msg["text"] = "Hello World!"
        self.msg.pack()
        self.botao = Button(self.tela1)
        self.botao["text"] = "Fechar"
        self.botao["command"] = self.tela1.quit
        self.botao.pack()
        

janela = tk.Tk()
Application(janela)
janela.mainloop()
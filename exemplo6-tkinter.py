import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title("GUI com Tkinter")
checkVar1 = tk.IntVar()
checkVar2 = tk.IntVar()

tk.Checkbutton(janela, text = "Machine Learning", variable = checkVar1, onvalue = 1, offvalue = 0).grid(row = 0, sticky = W)
tk.Checkbutton(janela, text = "Deep Learning", variable = checkVar2, onvalue = 1, offvalue = 0).grid(row = 1, sticky = W)

janela.mainloop()
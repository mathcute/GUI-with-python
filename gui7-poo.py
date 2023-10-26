import tkinter as tk

def escolhe_linguagem():

    escolha = v.get()

    if escolha == 1:

        print("Escolheu Python")

    elif escolha == 2:

        print("Escolheu C++")

    elif escolha == 3:

        print("Escolheu Java")

janela = tk.Tk()
v = tk.IntVar()
tk.Label(janela,
         text = """Esolha uma linguagem de Programação""",
         justify = tk.LEFT,
         padx = 20).pack()

tk.Radiobutton(janela, text = "Python", variable = v, value = 1).pack(anchor = tk.W)
tk.Radiobutton(janela, text = "Java", variable = v, value = 2).pack(anchor = tk.W)
tk.Radiobutton(janela, text = "C++", variable = v, value = 3).pack(anchor = tk.W)
tk.Button(janela, text = 'Imprime escolha', command = escolhe_linguagem).pack()
tk.mainloop()
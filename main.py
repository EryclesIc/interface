from tkinter import *
from lista import *


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title("ESTRUTURA DE DADOS")
        self.window.minsize(width=360, height=200)
        self.window.maxsize(width=360, height=200)

        self.text = Label(self.window, text="ESCOLHA UMA ESTRUTURA:")
        self.text.pack()

        self.Button_List = Button(self.window, text="LISTA", width=10, command=lambda: self.NovaJanela("LISTA"))
        self.Button_List.pack()

        self.Button_Pilha = Button(self.window, text="PILHA", width=10, command=lambda: self.NovaJanela("PILHA"))
        self.Button_Pilha.pack()

        self.Button_Fila = Button(self.window, text="FILA", width=10, command=lambda: self.NovaJanela("FILA"))
        self.Button_Fila.pack()

        self.Button_Arvore = Button(self.window, text="ARVORE", width=10, command=lambda: self.NovaJanela("ARVORE"))
        self.Button_Arvore.pack()

        self.Button_Grafo = Button(self.window, text="GRAFO", width=10, command=lambda: self.NovaJanela("GRAFO"))
        self.Button_Grafo.pack()

        self.window.mainloop()

    def NovaJanela(self, nome):
        self.window1 = Tk()
        self.window1.title(nome)
        self.window1.minsize(width=360, height=200)
        self.window1.maxsize(width=360, height=200)

        if nome == "LISTA":
            self.new_label = Label(self.window1, text="DIGITE O ELEMENTO PARA A LISTA:").grid(row=0)
            dado = Entry(self.window1)
            bt = Button(self.window1, text="OK", command=lambda: self.Onclick(dado)).grid(row=0, column=2)
            dado.grid(row=0, column=1)
            self.fechar = Button(self.window1, text="FECHAR", command=lambda: self.quit()).grid(row=1, column=1)
        self.window1.mainloop()

    def Onclick(self, dado):
        lista.append(dado.get())
        dado.delete(0, END)

    def quit(self):
        self.window1.destroy()

lista = LinkedList()
App()
print(lista)
print(lista.index("1"))
print('\n')

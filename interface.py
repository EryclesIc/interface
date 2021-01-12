import tkinter *

class TelaPrincipal:

    def opcoes_tela_inicial(self):
        janela1 = tkinter.Tk()
        janela1.geometry("500x500")

        # Exibe o titulo de apresentação da tela inicial
        titulo = tkinter.Label(janela1, text = "Seja bem vindo ao sistema de Estrutura de Dados!")
        titulo.config(font=("Verdana", 12))
        titulo.pack()

        mensagem1 = tkinter.Label(janela1, text = "Escolha uma das opções abaixo:")
        mensagem1.config(font=("Verdana", 10))
        mensagem1.pack()

        estrutura1 = tkinter.Button(janela1, text = "Lista Dinâmica", command = test)
        estrutura1.pack()
        estrutura2 = tkinter.Button(janela1, text = "Pilha")
        estrutura2.pack()
        estrutura3 = tkinter.Button(janela1, text = "Fila")
        estrutura3.pack()
        estrutura4 = tkinter.Button(janela1, text = "Árvore")
        estrutura4.pack()
        estrutura5 = tkinter.Button(janela1, text = "Grafo")
        estrutura5.pack()

        janela1.mainloop()
    
    def test(self):
        print("foi essa merda")

tela = TelaPrincipal()
tela.opcoes_tela_inicial()
from tkinter import *
import barcode
from barcode.writer import ImageWriter
import os

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 5
        self.quintoContainer["padx"] = 3
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.cpfLabel = Label(self.terceiroContainer, text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.terceiroContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Gerar código"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaQuantidadeNumeros
        self.autenticar.pack(side="left")

        self.limpar = Button(self.quartoContainer)
        self.limpar["text"] = "Limpar"
        self.limpar["font"] = ("Calibri", "8")
        self.limpar["width"] = 12
        self.limpar["command"] = self.limpaDados
        self.limpar.pack(side="right")

        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem["height"] = 2
        self.mensagem.pack()        


    def geraImagem(self,cpf):

        code128 = barcode.get_barcode_class('code128')

        with open(str(cpf) +'.jpeg', 'wb') as f:
            codigo = code128(cpf, writer=ImageWriter()).write(f)

        imagem = codigo.save(codigo)
        code = PhotoImage(file=imagem)
        self.img = Label(self.quintoContainer, image=code)

        ##FUNCIONA SALVANDO A IMAGEM
        #code128 = barcode.get_barcode_class('code128')
        #codigo = code128(cpf, writer=ImageWriter())
        #arquivo = str(cpf) + '.png'
        #imagem = codigo.save(arquivo)
        #code = PhotoImage(file=imagem)
        #self.img = Label(self.quintoContainer, image=code)
        #self.img.code = code
        #self.img.pack(side="top")
        
        ##REMOVE O ARQUIVO DO PC
        ##os.remove(imagem)

    #Método verificar quantidade de numeros
    def verificaQuantidadeNumeros(self):
        cpf = self.cpf.get()
        self.mensagem["text"] = ""
        #nome = self.nome.get()
        if len(cpf) != 11:
            self.mensagem["text"] = "Atenção. Digite os 11 números do CPF"
        else:
            self.img = self.geraImagem(cpf)
            
    def limpaDados(self):
        self.cpf.delete(0, END)
        self.nome.delete(0, END)
        self.mensagem["text"] = ""
        #self.quintoContainer.pack_forget()
        for item in self.quintoContainer.winfo_children():
            item.destroy()

    def deletaArquivo(self, arquivo):
        os.remove(arquivo)






root = Tk()
Application(root)
root.mainloop()

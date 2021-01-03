#!/usr/bin/python
import pyrebase
import csv
import sys
from tkinter import *
from tkinter import ttk

elementos = []
number = ""
contador = 0
lista = []

def atualizar():
    config = {
        "apiKey": "AIzaSyDnr73j6rAWweD05JWNBTfUVLC7Y_wi00s",
        "authDomain": "minha-colecao-a01d5.firebaseapp.com",
        "databaseURL": "https://minha-colecao-a01d5.firebaseio.com",
        "projectId": "minha-colecao-a01d5",
        "storageBucket": "minha-colecao-a01d5.appspot.com",
        "messagingSenderId": "275801323997",
        "appId": "1:275801323997:web:5663d46308a2cbb5e29e34"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password("christian.coliveira@gmail.com", "chr15714n")
    print("Usuario autenticado")
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    storage.child("Y2hyaXN0aWFuLmNvbGl2ZWlyYUBnbWFpbC5jb20=/bancodados/bancoMoedas.csv").download("bancoMoedas.csv")
    print("Download concluido bancoMoedas")
    storage.child("Y2hyaXN0aWFuLmNvbGl2ZWlyYUBnbWFpbC5jb20=/bancodados/bancoNotas.csv").download("bancoNotas.csv")
    print("Download concluido bancoNotas")

def Tipo():
    pesquisa = editBusca.get()
    if(rb_valor['text'] == 0):
        elementos = ['Voce','precisa', 'preencher', 'a', 'pesquisa','']
        tree.insert('',END,values=elementos)
    else:
        if(rb_valor['text'] == 2):
            arquivo = 'bancoNotas.csv'
        if(rb_valor['text'] == 1):
            arquivo = 'bancoMoedas.csv'
        
        contador = 0
        for i in tree.get_children():
            tree.delete(i)
        #read csv, and split on "," the line
        with open(arquivo, "rt") as f:
            reader = csv.reader(f, delimiter=",") 
            for row in reader:
                for field in row:
                    if field == pesquisa:
                        elementos = []
                        elementos = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]]
                        print(elementos)
                        tree.insert('',END,values=elementos)
                        contador = contador + 1  
                        print(contador)
        labelResultado['text']= 'Total de Registros: ' + str(contador) + ' itens'

janela = Tk()
janela.title('Pesquisa Colecao')
janela.geometry('1045x550')
janela.configure(background = 'white')
janela.resizable(False,False)
conteudo = Frame(janela, width=900, height=700, background='white')
conteudo.grid(row=0,column=0,sticky=W+E+N+S)

label = Label(conteudo, text='Pesquisa na Colecao de notas/moedas', padx=2, pady=2, background='white')
label.grid(row=0, column=0)

selecao = Frame(conteudo, bg='gray')
selecao.grid(row=1,column=1,columnspan=1)

radioValor = IntVar()
rb_moeda = Radiobutton(selecao, text="Moeda", variable=radioValor, value=1, background='white')
rb_nota = Radiobutton(selecao, text="Notas", variable=radioValor, value=2, background='white')
rb_moeda.grid(row=0, column=0)
rb_nota.grid(row=0, column=1)

rb_valor = Label(conteudo, textvariable=radioValor, padx=2, pady=2, background='white', fg='white')
rb_valor.grid(row=0, column=1)

label = Label(conteudo, text='Pesquisar por Nota ou Moeda?', padx=2, pady=2, background='white')
label.grid(row=1, column=0)

label1 = Label(conteudo, text='O que procura?', padx=2, pady=2, background='white')
label1.grid(row=2, column=0)
editBusca = Entry(conteudo)
editBusca.grid(row=2, column=1)

Button(conteudo, text='Pesquisar', command=Tipo).grid(row=2, column=2)

labelResultado = Label(conteudo, text='Total de Registros: ', padx=2, pady=2)
labelResultado.grid(row=6, column=0)
'''
treeview
'''
tree = ttk.Treeview(conteudo, selectmode='browse', 
column=('column1','column2','column3','column4','column5',
'column6','column7','column8','column9','column10','column11','column12','column13'), 
height=20, show='headings')

tree.column('column1', width=100, stretch=False, anchor='center')
tree.heading("#1", text='Pais')
tree.column('column2', width=40, stretch=False)
tree.heading("#2", text='Ano')
tree.column('column3', width=60, stretch=False)
tree.heading("#3", text='Krause')
tree.column('column4', width=90, stretch=False)
tree.heading("#4", text='Valor')
tree.column('column5', width=100, stretch=False)
tree.heading("#5", text='Moeda')
tree.column('column6', width=80, stretch=False)
tree.heading("#6", text='Tipo')
tree.column('column7', width=80, stretch=False)
tree.heading("#7", text='Qualidade')
tree.column('column8', width=80, stretch=False)
tree.heading("#8", text='Material')
tree.column('column9', width=80, stretch=False)
tree.heading("#9", text='Diametro')
tree.column('column10', width=80, stretch=False)
tree.heading("#10", text='Detalhe')
tree.column('column11', width=80, stretch=False)
tree.heading("#11", text='Anverso')
tree.column('column12', width=80, stretch=False)
tree.heading("#12", text='Reverso')
tree.column('column13', width=80, stretch=False)
tree.heading("#13", text='Data de Cadastro')

hscroll = Scrollbar(conteudo, orient = 'horizontal', command = 'tree.xview')
vscroll = Scrollbar(conteudo, orient = 'vertical', command = 'tree.yview')
tree.configure(yscrollcommand=vscroll.set,xscrollcommand=hscroll.set)
vscroll.configure(command=tree.yview)
hscroll.configure(command=tree.xview)
vscroll.grid(row=4, column=10, sticky='nse')
hscroll.grid(row=5, column=0, columnspan=4, sticky='ew')
'''
insere os valores no grid
'''


tree.grid(row=4, column=0, columnspan=4, sticky='nsew')


janela.mainloop()


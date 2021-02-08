#!/usr/bin/python
import pyrebase
import csv
import sys

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

def pesquisar():
    number = ""
    contador = 0

    escolha = input("Escolha o que deseja buscar\nAtualizar, Nota, Moeda :  ")
    if(escolha == 'Atualizar' or escolha == 'atualizar'):
        atualizar()
        return
    if(escolha == 'Nota' or escolha == 'Notas' or escolha == 'nota' or escolha == 'notas'):
        arquivo = 'bancoNotas.csv'
    if(escolha == 'Moedas' or escolha == 'moedas' or escolha == 'Moeda' or escolha == 'moeda'):
        arquivo = 'bancoMoedas.csv'
    lista = []
    while (number != "sair"):
        #input number you want to search
        if contador != 0:
            print("Encontrado "+str(contador)+" resultados\n\n\n\n\n")
        if number == "nota" or  number == "Nota" or number == "notas" or  number == "Notas" :
            arquivo = 'bancoNotas.csv'
        if number == "moeda" or  number == "moedas" or number == "Moeda" or  number == "Moedas" :
            arquivo = 'bancoMoedas.csv'
        contador = 0
        number = input("para sair digite 'sair'\nPesquisar em "+escolha+": ")
        #read csv, and split on "," the line
        if number == 'sair':
            exit()
        with open(arquivo, "rt") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                for field in row:
                    if field.upper() == number.upper():
                        print(f'>{row[0]}\tAno:{row[1]}\tKrause:{row[2]}\tValor:{row[3]}\t{row[4]}\tTipo:{row[5]}\tQualidade:{row[6]}')
                        contador = contador + 1



if __name__ == '__main__':
    while True:
        pesquisar()


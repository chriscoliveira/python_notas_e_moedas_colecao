import collections
import csv
import unidecode
from sys import exit
from lib import *

# from docs import firebase_colecao, leitura_csv


"""
necessario instalar 
pip3 install unidecode
pip3 install pyrebase4
sudo apt install python3-tk
"""

'''
MOEDAS verifica se existe o csv baixado da ucoin
'''
u_lista_total = abrecsv_ucoin()
u_lista_unica = lista_unica(u_lista_total)

'''
MOEDAS verifica se existe o csv do firebase do google, senao faz o download
'''
a_lista_total = abrecsv_google_moedas()
a_lista_unica = lista_unica(a_lista_total)

'''
NOTAS verifica se existe o csv do firebase do google, senao faz o download
'''
n_lista_total = abrecsv_google_notas()
n_lista_unica = lista_unica(n_lista_total)

# exibe_totais()

while True:
    opcao = ['exibir totais de moedas da Ucoin', 'exibir totais de moedas do Celular', 'exibir divergencias em moedas',
             'totais em notas', 'Pesquisar']
    valor = menu('Confere Moedas e Notas',opcao)


    if valor == '1':
        exibe_totais(u_lista_unica, u_lista_total,'TOTAL_MOEDA_UCOIN')
        continua = input('continue...')
    elif valor == '2':
        exibe_totais(a_lista_unica, a_lista_total,'TOTAL_MOEDA_ANDROID_APP')
        continua = input('continue...')
    elif valor == '3':
        exibe_divergencias(a_lista_unica, a_lista_total, u_lista_unica, u_lista_total)
        continua = input('continue...')
    elif valor == '4':
        exibe_totais(n_lista_unica, n_lista_total,'TOTAL_NOTAS_ANDROID_APP')
        continua = input('continue...')
    elif valor == '5':

        contador = 0
        opcao = ['Nota', 'Moeda']
        escolha = menu('Deseja pesquisar em:', opcao)

        if (escolha == '1'):
            arquivo = 'bancoNotas.csv'
        if (escolha == '2'):
            arquivo = 'bancoMoedas.csv'
        lista = []
        saida = str(len(opcao) + 1)
        while not escolha == saida:
            print()
            if contador != 0:
                print("Encontrado " + str(contador) + " resultados\n")

            termo = input("Para retornar digite 'voltar'\nPesquisar em " + opcao[int(escolha) - 1] + ": ")
            if termo.upper() == 'VOLTAR':
                break
            pesquisar(arquivo,termo)
    elif valor == '6':
        exit()
    else:
        print('Opção inválida!')

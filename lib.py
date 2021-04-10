import collections
import csv
import os
import pandas as pd
import pyrebase
import unidecode
from sys import exit

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)
pd.set_option('display.width', None)


def menu(msg, opcao):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{"#" * 50}\n{msg.upper()}\n{"#" * 50}')
    contador = 1
    for item in opcao:
        print(f'[{contador}] {item.upper()}')
        contador += 1
    print(f'[{contador}] SAIR\n{"#" * 50}')
    return input('\nOpção: ')


def baixar_CSV_android():
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
    storage.child("Y2hyaXN0aWFuLmNvbGl2ZWlyYUBnbWFpbC5jb20=/bancodados/bancoMoedas.csv").download(path='.',
                                                                                                  filename="bancoMoedas.csv")
    print("Download concluido bancoMoedas")
    storage.child("Y2hyaXN0aWFuLmNvbGl2ZWlyYUBnbWFpbC5jb20=/bancodados/bancoNotas.csv").download(path='.',
                                                                                                 filename="bancoNotas.csv")
    print("Download concluido bancoNotas")


def pesquisar(arquivo, termo):
    # print(arquivo, termo)
    contador = 0
    saida = []
    lista = ''
    with open('_resultado.txt', "w", encoding="utf8") as resultado1:
        lista += 'PAIS, ANO, #, VALOR, MOEDA, QUALIDADE, MATERIAL, DIAMETRO, VENDA\n'
        with open('resultado.txt', "w", encoding="utf8") as resultado:
            with open(arquivo, "rt", encoding="utf8") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    for field in row:
                        if field.upper() == termo.upper():
                            saida.append([row[0], row[1], row[2], row[3], row[4], row[6], row[7], row[8], row[12]])
                            lista += f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[6]}, {row[7]}, {row[8]}, {row[12]}\n'
                            contador = contador + 1

            final = pd.DataFrame(saida)
            final.columns = ['PAIS', 'ANO', '#', 'VALOR', 'MOEDA', 'QUALIDADE', 'MATERIAL', 'DIAMETRO', 'VENDA']
            resultado.write(str(final))
            resultado1.write(lista)


def abrecsv_ucoin():
    try:
        return pais_csv('ucoin.csv')[1:]
    except FileNotFoundError:
        print(
            'Esta Faltando algum Arquivo CSV da Ucoin acesse\nhttps://pt.ucoin.net/uid26638?export=csv\n verifique\nSaindo...')
        exit()


def abrecsv_google_moedas():
    try:
        return pais_csv('bancoMoedas.csv')[1:]

    except FileNotFoundError:
        print('Baixando o CSV "Android", aguarde um momento...')
        baixar_CSV_android()


def abrecsv_google_notas():
    try:
        return pais_csv('bancoNotas.csv')[1:]

    except FileNotFoundError:
        print('Baixando o CSV "Android", aguarde um momento...')
        baixar_CSV_android()
        exit()


def limpa_lista(lista):
    '''Limpa a lista retirando os acentos e demais caracteres especiais'''
    lista = ['ESTADOS UNIDOS' if v == 'EUA' else v for v in lista]
    lista = ['IRAN' if v == 'IRAO' else v for v in lista]
    lista = ['AFRICA OCIDENTAL' if v == 'AFRICA OCCIDENTAL' else v for v in lista]
    lista = ['ALEMANHA TERCEIRO REICH' if v == 'ALEMANHA - TERCEIRO REICH' else v for v in lista]

    try:
        lista.remove('IMPERIO ROMANO')
    except:
        pass
    return lista


def lista_unica(lista_total):
    '''funcao que retira os itens repetidos'''
    lista = list(dict.fromkeys(lista_total))
    lista = limpa_lista(lista)
    return lista


def pais_csv(arquivo, delimitador=','):
    """ funcao que le o arquivo csv e retorna uma lista em UPPER() """
    pais = []
    with open(arquivo, newline='', encoding='utf8') as file:
        lines = csv.reader(file, delimiter=delimitador)
        next(file)
        pais.append([row[0].rstrip().upper] for row in lines)
        for row in lines:
            pais.append(unidecode.unidecode(row[0].rstrip().upper()))

    pais = limpa_lista(pais)
    return pais


def exibe_totais(unica, total, tipo):
    saida = []
    lista = ''
    resultado = collections.Counter(total)
    # ucoin = collections.Counter(u_lista_total)
    with open(f'{tipo.upper()}.txt', 'w') as file:
        with open(f'_{tipo.upper()}.txt', 'w') as file1:
            saida.append(['PAIS', 'QUANTIDADE'])
            lista += f'PAIS, QUANTIDADE\n'
            for pais in range(len(resultado)):
                print(f'{unica[pais]}: {resultado[unica[pais]]}')
                saida.append([unica[pais], resultado[unica[pais]]])
                lista += f'{unica[pais]}, {resultado[unica[pais]]}\n'
            print(f'Total Paises {pais}')
            saida.append(['TOTAL', pais])
            final = pd.DataFrame(saida)
            file.write(str(final))
            file1.write(str(lista))


def exibe_divergencias(a_lista_unica, a_lista_total, u_lista_unica, u_lista_total):
    android_resultado = collections.Counter(a_lista_total)
    ucoin_resultado = collections.Counter(u_lista_total)
    saida = []
    lista = ''
    with open(f'DIVERGENCIAS.txt', 'w') as file:
        with open(f'_DIVERGENCIAS.txt', 'w') as file1:
            print(f'\n{"*" * 65}\n  Verica se foi encontrado divergencias entre os 2 arquivos CSV\n{"*" * 65}\n')
            saida.append(['PAIS', 'ANDROID', 'UCOIN'])
            lista += 'PAIS, ANDROID, UCOIN\n'
            for v in range(len(a_lista_unica)):
                if not android_resultado[a_lista_unica[v]] == ucoin_resultado[a_lista_unica[v]]:
                    print([a_lista_unica[v], android_resultado[a_lista_unica[v]], ucoin_resultado[u_lista_unica[v]]])
                    saida.append([a_lista_unica[v], android_resultado[a_lista_unica[v]], ucoin_resultado[u_lista_unica[v]]])
                    lista += f'{a_lista_unica[v]}, {android_resultado[a_lista_unica[v]]}, {ucoin_resultado[u_lista_unica[v]]}\n'
            print([len(u_lista_total), len(a_lista_total)])
            saida.append(['TOTAL ', str(len(a_lista_total)), str(len(u_lista_total))])
            final = pd.DataFrame(saida)
            file.write(str(final))
            file1.write(lista)


def total(arquivo):
    # print(arquivo, termo)
    contador = 0
    saida = []
    lista = ''
    with open('_resultado.txt', "w", encoding="utf8") as resultado1:

        with open('resultado.txt', "w", encoding="utf8") as resultado:
            with open(arquivo, "rt", encoding="utf8") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    saida.append([row[0], row[1], row[2], row[3], row[4], row[6], row[7], row[8], row[12]])
                    lista += f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[6]}, {row[7]}, {row[8]}, {row[12]}\n'
                    contador = contador + 1

            final = pd.DataFrame(saida)
            final.columns = ['PAIS', 'ANO', '#', 'VALOR', 'MOEDA', 'QUALIDADE', 'MATERIAL', 'DIAMETRO', 'VENDA']
            resultado.write(str(final))
            resultado1.write(lista)


if __name__ == '__main__':
    baixar_CSV_android()

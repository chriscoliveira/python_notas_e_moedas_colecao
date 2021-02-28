import collections
import csv
import unidecode
import pyrebase
from sys import exit
import os


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


def pesquisar():
    number = ""
    contador = 0
    opcao = ['Nota', 'Moeda']
    escolha = menu('Deseja pesquisar em:', opcao)

    if (escolha == '1'):
        arquivo = 'bancoNotas.csv'
    if (escolha == '2'):
        arquivo = 'bancoMoedas.csv'
    lista = []
    saida = str(len(opcao)+1)
    while not escolha == saida:
        print()
        if contador != 0:
            print("Encontrado " + str(contador) + " resultados\n")

        contador = 0
        termo = input("Para retornar digite 'voltar'\nPesquisar em " + opcao[int(escolha) - 1] + ": ")

        if termo.upper() == 'VOLTAR':
            break
        with open(arquivo, "rt", encoding="utf8") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                for field in row:
                    if field.upper() == termo.upper():
                        print(
                            f'>{row[0]}\tAno:{row[1]}\tKrause:{row[2]}\tValor:{row[3]}\t{row[4]}\tTipo:{row[5]}\tQualidade:{row[6]}')
                        contador = contador + 1


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


def exibe_totais(unica, total,tipo):
    resultado = collections.Counter(total)
    # ucoin = collections.Counter(u_lista_total)
    with open(f'{tipo.upper()}.txt','w') as file:
        file.write(f'{tipo.replace("_", " ")}\n\n')
        for pais in range(len(resultado)):
            print(f'{unica[pais]}: {resultado[unica[pais]]}')
            file.write(f'{unica[pais]}: {resultado[unica[pais]]}\n')
        print(f'Total Paises {pais}')
        file.write(f'Total Paises {pais}\n')



def exibe_divergencias(a_lista_unica, a_lista_total, u_lista_unica, u_lista_total):
    android_resultado = collections.Counter(a_lista_total)
    ucoin_resultado = collections.Counter(u_lista_total)
    print(f'\n{"*" * 65}\n  Verica se foi encontrado divergencias entre os 2 arquivos CSV\n{"*" * 65}\n')
    for v in range(len(a_lista_unica)):
        if not android_resultado[a_lista_unica[v]] == ucoin_resultado[a_lista_unica[v]]:
            print(
                f'\t{a_lista_unica[v]}\tAndroid:{android_resultado[a_lista_unica[v]]}\tUcoin:{ucoin_resultado[u_lista_unica[v]]}')

    print(f'\nTotal Ucoin: {len(u_lista_total)}\nTotal Android: {len(a_lista_total)}')


if __name__ == '__main__':
    baixar_CSV_android()

import collections
import csv, unidecode
from itertools import groupby
from collections import Counter
from sys import exit
import firebase_colecao
import urllib.request

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


def exibe_totais(unica, total):
    resultado = collections.Counter(total)
    ucoin = collections.Counter(u_lista_total)

    for pais in range(len(resultado)):
        print(f'{unica[pais]}: {resultado[unica[pais]]}')
    print(f'Total Paises {pais}')


def exibe_divergencias():
    android_resultado = collections.Counter(a_lista_total)
    ucoin_resultado = collections.Counter(u_lista_total)
    print(f'\n{"*" * 65}\n  Verica se foi encontrado divergencias entre os 2 arquivos CSV\n{"*" * 65}\n')
    for v in range(len(a_lista_unica)):
        if not android_resultado[a_lista_unica[v]] == ucoin_resultado[a_lista_unica[v]]:
            print(
                f'\t{a_lista_unica[v]}\tAndroid:{android_resultado[a_lista_unica[v]]}\tUcoin:{ucoin_resultado[u_lista_unica[v]]}')

    print(f'\nTotal Ucoin: {len(u_lista_total)}\nTotal Android: {len(a_lista_total)}')


try:
    u_lista_total = pais_csv('ucoin.csv')[1:]
    u_lista_unica = lista_unica(u_lista_total)
except FileNotFoundError:
    print('Esta Faltando algum Arquivo CSV da Ucoin acesse\nhttps://pt.ucoin.net/uid26638?export=csv\n verifique\nSaindo...')
    exit()


try:
    a_lista_total = pais_csv('bancoMoedas.csv')[1:]
    a_lista_unica = lista_unica(a_lista_total)
except FileNotFoundError:
    print('Baixando o CSV "Android", aguarde um momento...')
    firebase_colecao.baixar_CSV_android()
    reload()
    
try:
    n_lista_total = pais_csv('bancoNotas.csv')[1:]
    n_lista_unica = lista_unica(n_lista_total)
except FileNotFoundError:
    print('Baixando o CSV "Android", aguarde um momento...')
    firebase_colecao.baixar_CSV_android()
    exit()
# exibe_totais()

while True:
    print(f'\n{"#" * 65}\nConfere Moedas e Notas\n{"#" * 65}\n'
          f'Digite 1 para exibir totais de moedas da Ucoin\n'
          f'Digite 2 para exibir totais de moedas do Celular\n'
          f'Digite 3 para exibir divergencias em moedas\n'
          f'Digite 4 para totais em notas')
    valor = input('Opção: ')
    if valor == '1':
        exibe_totais(u_lista_unica, u_lista_total)
    elif valor == '2':
        exibe_totais(a_lista_unica, a_lista_total)
    elif valor == '3':
        exibe_divergencias()
    elif valor == '4':
        exibe_totais(n_lista_unica,n_lista_total)
    else:
        break

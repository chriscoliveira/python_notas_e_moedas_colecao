from os import link
from pprint import pprint
import sys
from threading import Thread
import unicodedata
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from layout import *
from functools import partial
from datetime import date, datetime
import requests
import urllib
from funcoes import Colecao
from PyQt5.QtWidgets import QMainWindow, QApplication
import os
from currency_converter import CurrencyConverter

colecao = Colecao('db_colecao.db')


'''
THREADS
'''


def baixar_fotos(id, link1, link2):

    try:

        with requests.Session() as session:
            resp_2 = session.get(link1,
                                 headers={'User-Agent': 'Mozilla/5.0'})
            with open(f"fotos/id_{id}_1.jpg", "wb") as f:
                f.write(resp_2.content)

    except Exception as e:
        print(e)

    try:
        with requests.Session() as session:
            resp_2 = session.get(link2,
                                 headers={'User-Agent': 'Mozilla/5.0'})
            with open(f"fotos/id_{id}_2.jpg", "wb") as f:
                f.write(resp_2.content)

    except Exception as e:
        print(e)


# id, venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto, serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao, tipo =
for i in range(1718, 1753):
    try:
      
        print(f'item {i=}')
        item = colecao.buscar_id(i)
        baixar_fotos(item[0], item[23], item[24])
        print(item[0], item[23], item[24])
    except:
        print(f'falha {i=}')
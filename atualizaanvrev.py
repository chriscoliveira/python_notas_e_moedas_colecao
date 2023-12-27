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
import sqlite3
from playwright.sync_api import sync_playwright
from time import sleep
import os
from bs4 import BeautifulSoup
from funcoes import Colecao
from PyQt5.QtWidgets import QMainWindow, QApplication
import os
from currency_converter import CurrencyConverter

colecao = Colecao('db_colecao.db')
conn = sqlite3.connect('db_colecao.db')
cursor = conn.cursor()

def editar(id, anverso, reverso):
    sql = "UPDATE colecao SET anverso=?, reverso=? WHERE id=?"
    cursor.execute(sql, (anverso, reverso, id))
    conn.commit()


def captura_infos(link):
    if link:
        with sync_playwright() as p:
            VENDA, CUNHAGEM, FOTO1, FOTO2, CADASTRO, PAIS, ANO, KRAUSE, VALOR, PERIODO, CIRCULACAO, ASSUNTO, SERIE, SOBERANO, COMPOSICAO, BORDA, FORMATO, ALINHAMENTO, PESO, DIAMETRO, ESPESSURA, ANVERSO, REVERSO, CONSERVACAO = '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
            browser = p.chromium.launch_persistent_context(channel='chrome', user_data_dir=os.path.join(
                os.path.dirname(__file__), 'user_data'), headless=True)
            page = browser.new_page()
            # entra link por link
            page.goto(link)
            page.set_default_timeout(0)

            htm = page.content()
            soup = BeautifulSoup(htm, 'html.parser', from_encoding='UTF-8')
            with open('tmp.txt', 'w', encoding='utf-8') as tmp:
                tmp.write(soup.prettify())


            infopublicacao = soup.find_all('table', class_='my-func-info')
            soupinfo = BeautifulSoup(str(infopublicacao), 'html.parser')
            linhasinfo = soupinfo.find_all('tr')

            info = soup.find_all('table', class_='coin-info')
            soupinfo = BeautifulSoup(
                str(info), 'html.parser', from_encoding='utf-8')
            linhasinfo = soupinfo.find_all('tr')

            anv_rev = soup.find_all('table', class_='tbl coin-desc')
            soupinfo = BeautifulSoup(
                str(anv_rev), 'html.parser', from_encoding='utf-8')

            linhas_anvrev = soupinfo.find_all('tr')

            ANVERSO = linhas_anvrev[0].text.replace('\t', '')

            REVERSO = linhas_anvrev[1].text.replace('\t', '')

            return ANVERSO.replace("\n",""),REVERSO.replace("\n","")

def buscareg(id,pesquisa):
    destino=""
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(channel='chrome', user_data_dir=os.path.join(
            os.path.dirname(__file__), 'user_data'), headless=True)
        page = browser.new_page()
        # entra link por link
        page.goto("https://pt.ucoin.net/catalog")
        # page.set_default_timeout(0)
        page.fill('#search', pesquisa)
        sleep(2)
        page.keyboard.down("Enter")
        sleep(3)

        htm = page.content()
        soup = BeautifulSoup(htm, 'html.parser', from_encoding='UTF-8')
        with open('tmp.txt', 'w', encoding='utf-8') as tmp:
            tmp.write(soup.prettify())
        itens = soup.find_all('td',class_="coin-info")
        destino=itens[0].find('a')['href']
        # for i in itens:
    anv,rev = captura_infos("https://pt.ucoin.net"+destino)
    editar(id,anv,rev)
    sleep(20)
lista=[["1","Espanha KM# 766"],["64","França KM# 902"],["130","Brasil KM# 648"],["131","Brasil KM# 651a"],["145","Peru KM# 272"],["159","Brasil KM# 556a"],["178","Espanha KM# 948"],["210","Brasil KM# 559"],["221","Grécia KM# 183"],["230","França KM# 931"],["238","Estados Unidos da América KM# 478"],["294","Brasil KM# 555a"],["334","Noruega KM# 460"],["352","República Checa KM# 4"],["366","França KM# 777"],["382","Argentina KM# 112"],["415","Rússia Y# 602a"],["583","Colômbia KM# 287"],["613","Chile KM# 228"],["621","Holanda KM# 183"],["623","Estados Unidos da América KM# 372"],["638","Uzbequistão KM# 1"],["639","Uzbequistão KM# 2"],["640","Uzbequistão KM# 3"],["670","Alemanha KM# 11"],["675","Brasil KM# 556a"],["676","Brasil KM# 555a"],["687","Bélgica KM# 154"],["737","Alemanha KM# 209"],["752","Brasil KM# 557a"],["753","Brasil KM# 559"],["754","Brasil KM# 558"],["975","Estados Unidos da América KM# 396"],["978","Estados Unidos da América KM# 297"],["983","Estados Unidos da América KM# 310"],["1017","Estados Unidos da América KM# 201b"],["1023","Estados Unidos da América KM# 164a"],["1027","Estados Unidos da América KM# 201b"],["1028","Estados Unidos da América KM# 164a"],["1029","Estados Unidos da América KM# 201b"],["1034","Estados Unidos da América KM# 201"],["1037","Estados Unidos da América KM# 201"],["1042","Estados Unidos da América KM# 164a"],["1044","Estados Unidos da América KM# 164a"],["1045","Estados Unidos da América KM# A192"],["1047","Estados Unidos da América KM# 164a"],["1048","Estados Unidos da América KM# 203"],["1050","Estados Unidos da América KM# 201"],["1058","Estados Unidos da América KM# A192"],["1060","Estados Unidos da América KM# 201"],["1061","Estados Unidos da América KM# 192"],["1079","Índia KM# 14.2"],["1104","Rússia Y# 338"],["1291","Bahamas KM# 63.1"],["1297","Chile KM# 228"],["1305","Uruguai KM# 121"],["1713","Brasil KM# 652a"],["1714","Guernsey KM# 96"],["1715","Argentina KM# 57"],["1716","Argentina KM# 46"],["1717","Argentina KM# 40"],["1718","Guatemala KM# 276.6"],["1723","Itália KM# 93"],["1724","Itália KM# 111"],["1725","Portugal KM# 591"],["1726","Portugal KM# 590"],["1727","Portugal KM# 596"],["1741","Suécia KM# 850"],["1742","Suécia KM# 850"],["1743","Suécia KM# 836"],["1744","Suécia KM# 852"],["1745","Suécia KM# 852"],["1746","Dinamarca KM# 866"],["1747","Kuwait KM# 12"],["1748","Iraque KM# 125a"],["1749","Uruguai KM# 135"],["1750","Portugal KM# 742"],["1751","Países baixos KM# 235"],["1752","Estados unidos da américa KM# 195a"],["1753","Reino unido KM# 915"],["1754","Japão Y# 97"],["1755","Canadá KM# 1255"],["1756","Canadá KM# 493"]]
for i in lista:
    print(i[1])
    try:
        buscareg(i[0],i[1])
    except Exception as e:
        print(e)
# print(captura_infos("https://pt.ucoin.net/coin/japan-10-yen-1989-2019/?tid=2213"))
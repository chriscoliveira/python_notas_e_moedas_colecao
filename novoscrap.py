import os
import re
from threading import Thread
from time import sleep

import requests
from PyQt5 import uic
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

link_colecao = 'https://pt.ucoin.net/gallery/?uid=26638&page='
# https://pt.ucoin.net/gallery/?uid=26638&page=111 ultima pagina


def criartabela():
    sql = 'CREATE TABLE IF NOT EXISTS "DBColecao"( ' \
        + '"id"	INTEGER UNIQUE,' \
        + '"PAIS"	TEXT', \
        +'"ANO"	TEXT,'\
        + '"KRAUSE"	TEXT,' \
        + '"VALOR"	TEXT,' \
        + '"PERIODO"	TEXT,' \
        + '"CIRCULACAO"	TEXT,' \
        + '"ASSUNTO"	TEXT,' \
        + '"SERIE"	TEXT,' \
        + '"SOBERANO"	TEXT,' \
        + '"CUNHAGEM"	TEXT,' \
        + '"COMPOSICAO"	TEXT,' \
        + '"BORDA"	TEXT,' \
        + '"FORMATO"	TEXT,' \
        + '"ALINHAMENTO"	TEXT,' \
        + '"PESO"	TEXT,' \
        + '"CONSERVACAO"	TEXT,' \
        + '"DIAMETRO"	TEXT,' \
        + '"ESPESSURA"	TEXT,' \
        + '"ANVERSO"	TEXT,' \
        + '"REVERSO"	TEXT,' \
        + '"VENDA"	TEXT,' \
        + '"CADASTRO"	TEXT,' \
        + '"FOTO1"	TEXT,' \
        + '"FOTO2"	TEXT,' \
        + 'PRIMARY KEY("id" AUTOINCREMENT) )'


def login_site():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=os.path.join(os.path.dirname(__file__), 'user_data'), headless=False)
        page = browser.new_page()
        # entra na pagina do anime

        page.goto('https://pt.ucoin.net/')

        page.click('text=Entrar')
        page.fill('input[name="login-email"]', 'christian.coliveira@gmail.com')
        page.fill('input[name="login-passwd"]', 'Chr1571@n')
        page.click('button[type="submit"]')


def captura_itens_pagina(pagina):
    req = requests.get(pagina, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.content, 'html.parser')
    itens = soup.find_all('a', class_='blue-15')
    for item in itens:
        link = 'https://pt.ucoin.net'+item['href']


def captura_dados_moeda(link):
    # req = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'})
    # soup = BeautifulSoup(req.content, 'html.parser')
    # itens = soup.find_all('div', class_='centerCol')
    # for item in itens:

    with sync_playwright() as p:
        # browser = p.chromium.launch(
        #     channel='chrome', headless=False)
        browser = p.chromium.launch_persistent_context(
            user_data_dir=os.path.join(os.path.dirname(__file__), 'user_data'), headless=True)
        page = browser.new_page()
        # entra na pagina do anime

        page.goto(link)

        htm = page.content()
        soup = BeautifulSoup(htm, 'html.parser')

        # pega todas as informacoes da moeda
        info = soup.find('table', class_='coin-info')
        soupinfo = BeautifulSoup(str(info), 'html.parser')
        linhasinfo = soupinfo.find_all('tr')
        for linha in linhasinfo:
            if 'País' in str(linha):
                PAIS = str(linha).replace(
                    '<tr><th>País</th><td>', '').replace('</td></tr>', '')
                print(PAIS)
            if 'Ano' in str(linha):
                ANO = str(linha).replace(
                    '<tr><th>Ano</th><td>', '').replace('</td></tr>', '')
                print(ANO)
            if 'Krause' in str(linha):
                KRAUSE = str(linha).replace(
                    '<tr><th>Número Krause</th><td>', '').replace('</td></tr>', '')
                print(KRAUSE)

            if 'Denominação' in str(linha):
                VALOR = str(linha).replace(
                    '<tr><th>Denominação</th><td>', '').replace('</td></tr>', '')
                print(VALOR)
            if 'Período' in str(linha):
                PERIODO = str(linha).replace(
                    '<tr><th>Período</th><td>', '').replace('</td></tr>', '')
                print(PERIODO)
            if 'Tipo de moeda' in str(linha):
                CIRCULACAO = str(linha).replace(
                    '<tr><th>Tipo de moeda</th><td>', '').replace('</td></tr>', '')
                print(CIRCULACAO)
            if 'Assunto' in str(linha):
                ASSUNTO = str(linha).replace(
                    '<tr><th>Assunto</th><td>', '').replace('</td></tr>', '')
                print(ASSUNTO)
            if 'Série' in str(linha):
                SERIE = str(linha).replace(
                    '<tr><th>Série</th><td>', '').replace('</td></tr>', '')
                print(SERIE)
            if 'Soberano' in str(linha):
                SOBERANO = str(linha).replace(
                    '<tr><th>Soberano</th><td>', '').replace('</td></tr>', '')
                print(SOBERANO)
            # CUNHAGEM
            if 'Composição' in str(linha):
                COMPOSICAO = str(linha).replace(
                    '<tr><th>Composição</th><td>', '').replace('</td></tr>', '')
                print(COMPOSICAO)
            if 'Tipo de Bordo' in str(linha):
                BORDA = str(linha).replace(
                    '<tr><th>Tipo de Bordo</th><td>', '').replace('</td></tr>', '')
                print(BORDA)
            if 'Formato' in str(linha):
                FORMATO = str(linha).replace(
                    '<tr><th>Formato</th><td>', '').replace('</td></tr>', '')
                print(FORMATO)
            if 'Peso' in str(linha):
                PESO = str(linha).replace(
                    '<tr><th>Peso (gr)</th><td>', '').replace('</td></tr>', '')
                print(PESO)
            if 'Diametro' in str(linha):
                DIAMETRO = str(linha).replace(
                    '<tr><th>Diametro (mm)</th><td>', '').replace('</td></tr>', '')
                print(DIAMETRO)
            if 'Espessura' in str(linha):
                ESPESSURA = str(linha).replace(
                    '<tr><th>Espessura (mm)</th><td>', '').replace('</td></tr>', '')
                print(ESPESSURA)

            # ANVERSO
            # REVERSO
            # VENDA = soup.find('a', class_='pricewj').text
            # VENDA = VENDA.replace('Preço: R$ ', '')
            # CADASTRO
            # FOTO1
            # FOTO2
            # print(VENDA)


# captura_itens_pagina(link_colecao+'1')
captura_dados_moeda(
    'https://pt.ucoin.net/coin/brazil-25-centavos-2021/?ucid=49530412')

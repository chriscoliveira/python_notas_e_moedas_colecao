import os
import re
from socket import setdefaulttimeout
from threading import Thread
from time import sleep

import requests
from PyQt5 import uic
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import sqlite3
from sqlite3 import Error

link_colecao = 'https://pt.ucoin.net/gallery/?uid=26638&page='
# https://pt.ucoin.net/gallery/?uid=26638&page=111 ultima pagina


class DBase:
    ''' CRIAÇÃO DE TABELAS '''

    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.c = self.conn.cursor()

    def criartabela(self):
        sql = 'CREATE TABLE IF NOT EXISTS "moedas"( "id" INTEGER UNIQUE,"PAIS" TEXT,"ANO" TEXT,"KRAUSE" TEXT,"VALOR" TEXT,"PERIODO" TEXT,"CIRCULACAO" TEXT,"ASSUNTO" TEXT,"SERIE" TEXT,"SOBERANO" TEXT,"CUNHAGEM" TEXT,"COMPOSICAO" TEXT,"BORDA" TEXT,"FORMATO" TEXT,"ALINHAMENTO" TEXT,"PESO" TEXT,"CONSERVACAO" TEXT,"DIAMETRO" TEXT,"ESPESSURA" TEXT,"ANVERSO" TEXT,"REVERSO" TEXT,"VENDA" TEXT,"CADASTRO" TEXT,"FOTO1" TEXT,"FOTO2" TEXT,PRIMARY KEY("id" AUTOINCREMENT) )'
        self.c.execute(sql)

    def cadastrar(self, venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto, serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso):
        sql = 'INSERT INTO moedas(venda,cunhagem,foto1,foto2,cadastro,pais,ano,krause,valor,periodo,circulacao,assunto,serie,soberano,composicao,borda,formato,alinhamento,peso,diametro,espessura,anverso,reverso) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '
        self.c.execute(sql, (venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao,
                       assunto, serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso))


Banco = DBase('db_colecao.db')
Banco.criartabela()


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
        page.click('input[name="remember"]')
        page.click('button[type="submit"]')
        page.close()


def captura_itens_pagina(pagina):
    req = requests.get(pagina, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.content, 'html.parser')
    itens = soup.find_all('a', class_='blue-15')
    for item in itens:
        link = 'https://pt.ucoin.net'+item['href']


def captura_dados_moeda(link):
    VENDA, CUNHAGEM, FOTO1, FOTO2, CADASTRO, PAIS, ANO, KRAUSE, VALOR, PERIODO, CIRCULACAO, ASSUNTO, SERIE, SOBERANO, COMPOSICAO, BORDA, FORMATO, ALINHAMENTO, PESO, DIAMETRO, ESPESSURA, ANVERSO, REVERSO = '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''

    with sync_playwright() as p:
        # browser = p.chromium.launch(
        #     channel='chrome', headless=False)
        browser = p.chromium.launch_persistent_context(
            user_data_dir=os.path.join(os.path.dirname(__file__), 'user_data'), headless=True)
        page = browser.new_page()

        # entra na pagina do anime

        page.goto(link)
        page.set_default_timeout(0)

        htm = page.content()
        soup = BeautifulSoup(htm, 'html.parser')

        VENDA = soup.find('a', class_='pricewj').text
        VENDA = VENDA.replace('Preço: R$ ', '')
        print(VENDA)
        try:
            CUNHAGEM = soup.find('h4').text
            print(CUNHAGEM)
        except:
            CUNHAGEM = ''
        FOTO = soup.find_all('img', id='coin-img1')
        for i in FOTO:
            print(i['src'])
        infopublicacao = soup.find_all('table', class_='my-func-info')
        soupinfo = BeautifulSoup(str(infopublicacao), 'html.parser')
        linhasinfo = soupinfo.find_all('tr')
        for i in linhasinfo:
            if 'Publicado' in str(i):
                CADASTRO = str(i).replace(
                    '<tr><td class="lgray-12">Publicado</td><td class="gray-12">', '').replace('</td></tr>', '')
                print(CADASTRO)

        # pega todas as informacoes da moeda
        info = soup.find_all('table', class_='coin-info')
        soupinfo = BeautifulSoup(str(info), 'html.parser')
        linhasinfo = soupinfo.find_all('tr')
        with open('teste.txt', 'w') as f:

            for linha in linhasinfo:
                f.write(str(linha)+'\n')
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
                if 'Periodo' in str(linha):
                    PERIODO = str(linha).replace(
                        '<tr><th>Periodo</th><td>', '').replace('</td></tr>', '')
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

                if 'Composição' in str(linha):
                    COMPOSICAO = str(linha).replace(
                        '<tr><th>Composição</th><td>', '').replace('</td></tr>', '')
                    print(COMPOSICAO)
                if 'Tipo de bordo' in str(linha):
                    BORDA = str(linha).replace(
                        '<tr><th>Tipo de bordo</th><td>', '').replace('</td></tr>', '')
                    print(BORDA)
                if 'Formato' in str(linha):
                    FORMATO = str(linha).replace(
                        '<tr><th>Formato</th><td>', '').replace('</td></tr>', '')
                    print(FORMATO)
                if 'Alinhamento' in str(linha):
                    ALINHAMENTO = str(linha).replace(
                        '<tr><th>Alinhamento</th><td>', '').replace('</td></tr>', '')
                    print(ALINHAMENTO)
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
                if 'Anverso' in str(linha):
                    ANVERSO = str(linha).replace(
                        '<tr><th class="nowrap">Anverso</th><td>', '').replace('<span class="lgray-11"> / </span>', ' / ').replace('</td></tr>', '')
                    print(ANVERSO)
                if 'Reverso' in str(linha):
                    REVERSO = str(linha).replace(
                        '<tr><th class="nowrap">Reverso</th><td>', '').replace('<span class="lgray-11"> / </span>', ' / ').replace('</td></tr>', '')
                    print(REVERSO)
            print(VENDA, CUNHAGEM, FOTO1, FOTO2, CADASTRO, PAIS, ANO, KRAUSE, VALOR, PERIODO, CIRCULACAO, ASSUNTO,
                  SERIE, SOBERANO, COMPOSICAO, BORDA, FORMATO, ALINHAMENTO, PESO, DIAMETRO, ESPESSURA, ANVERSO, REVERSO)


# captura_itens_pagina(link_colecao+'1')
captura_dados_moeda(
    'https://pt.ucoin.net/coin/usa-1-cent-2017/?ucid=44236499')
# 'https://pt.ucoin.net/coin/united_kingdom-1-penny-1988/?ucid=47106083')


# login_site()

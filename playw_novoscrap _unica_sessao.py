from base64 import encode
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
        sql = 'CREATE TABLE IF NOT EXISTS "moedas"( "id" INTEGER UNIQUE, "PAIS" TEXT, "ANO" TEXT, "KRAUSE" TEXT, "VALOR" TEXT, "PERIODO" TEXT, "CIRCULACAO" TEXT, "ASSUNTO" TEXT, "SERIE" TEXT, "SOBERANO" TEXT, "CUNHAGEM" TEXT, "COMPOSICAO" TEXT, "BORDA" TEXT, "FORMATO" TEXT, "ALINHAMENTO" TEXT, "PESO" TEXT, "CONSERVACAO" TEXT, "DIAMETRO" TEXT, "ESPESSURA" TEXT, "ANVERSO" TEXT, "REVERSO" TEXT, "VENDA" TEXT, "CADASTRO" TEXT, "FOTO1" TEXT, "FOTO2" TEXT,PRIMARY KEY("id" AUTOINCREMENT) )'
        self.c.execute(sql)

    def cadastrar(self, venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto, serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao):

        try:
            sqliteConnection = sqlite3.connect('db_colecao.db')
            cursor = sqliteConnection.cursor()
            # print("Successfully Connected to SQLite")

            sqlite_insert_query = "INSERT INTO Moedas (venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto, serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            sqlite_data_tuple = (venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao,
                                 assunto, serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao)
            count = cursor.execute(sqlite_insert_query, sqlite_data_tuple)
            sqliteConnection.commit()
            # print(
            #     "Record inserted successfully into SqliteDb_developers table ",  cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")


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


def novacaptura(inicio, fim):
    VENDA, CUNHAGEM, FOTO1, FOTO2, CADASTRO, PAIS, ANO, KRAUSE, VALOR, PERIODO, CIRCULACAO, ASSUNTO, SERIE, SOBERANO, COMPOSICAO, BORDA, FORMATO, ALINHAMENTO, PESO, DIAMETRO, ESPESSURA, ANVERSO, REVERSO, CONSERVACAO = '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
    with sync_playwright() as p:
        # browser = p.chromium.launch(
        #     channel='chrome', headless=False)
        browser = p.chromium.launch_persistent_context(channel='chrome', user_data_dir=os.path.join(
            os.path.dirname(__file__), 'user_data'), headless=False)
        page = browser.new_page()

        # pega os links por pagina
        for i in range(int(inicio), int(fim)):
            print(link_colecao+str(i))
            with open('paginas_feitas.txt', 'a') as p:
                p.write(link_colecao+str(i)+'\n')
            req = requests.get(link_colecao+str(i),
                               headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(req.content, 'html.parser')
            itens = soup.find_all('a', class_='blue-15')
            for item in itens:
                link = 'https://pt.ucoin.net'+item['href']

                # entra link por link
                page.goto(link)
                page.set_default_timeout(0)

                htm = page.content()
                soup = BeautifulSoup(htm, 'html.parser', from_encoding='UTF-8')

                try:
                    VENDA = soup.find('a', class_='pricewj').text
                    VENDA = VENDA.replace('Preço: R$ ', '')
                except:
                    VENDA = ''

                try:
                    CUNHAGEM = soup.find('h4').text

                except:
                    CUNHAGEM = ''
                try:
                    FOTO = soup.find_all('img', id='coin-img1')
                    FOTOS = []
                    for i in FOTO:
                        FOTOS.append(i['src'])
                    FOTO1 = FOTOS[0]
                    FOTO2 = FOTOS[1]
                except:
                    FOTO1 = ''
                    FOTO2 = ''

                infopublicacao = soup.find_all('table', class_='my-func-info')
                soupinfo = BeautifulSoup(str(infopublicacao), 'html.parser')
                linhasinfo = soupinfo.find_all('tr')
                for i in linhasinfo:
                    if 'Publicado' in str(i):
                        CADASTRO = str(i).replace(
                            '<tr><td class="lgray-12">Publicado</td><td class="gray-12">', '').replace('</td></tr>', '')
                    if 'Conservação' in str(i):
                        # CONSERVACAO = str(i).replace(
                        #     '<tr><td class="lgray-12">Conservação</td><td class="gray-12">', '').replace('</td></tr>', '')
                        try:
                            CONSERVACAO = soupinfo.find(
                                'div', class_='wrap').text
                        except:
                            CONSERVACAO = ''
                        # <div class="wrap" title="VF - Soberba">VF - Soberba</div>
                        # pega todas as informacoes da moeda
                        # pega todas as informacoes da moeda
                info = soup.find_all('table', class_='coin-info')
                soupinfo = BeautifulSoup(
                    str(info), 'html.parser', from_encoding='utf-8')
                linhasinfo = soupinfo.find_all('tr')

                with open('teste.txt', 'w', encoding='utf-8') as f:
                    for linha in linhasinfo:

                        if 'País' in str(linha):
                            PAIS = str(linha).replace(
                                '<tr><th>País</th><td>', '').replace('</td></tr>', '')

                        if 'Ano' in str(linha):
                            ANO = str(linha).replace(
                                '<tr><th>Ano</th><td>', '').replace('</td></tr>', '')

                        if 'Krause' in str(linha):
                            KRAUSE = str(linha).replace(
                                '<tr><th>Número Krause</th><td>', '').replace('</td></tr>', '')

                        if 'Denominação' in str(linha):
                            VALOR = str(linha).replace(
                                '<tr><th>Denominação</th><td>', '').replace('</td></tr>', '')

                        if 'Periodo' in str(linha):
                            PERIODO = str(linha).replace(
                                '<tr><th>Periodo</th><td>', '').replace('</td></tr>', '')

                        if 'Tipo de moeda' in str(linha):
                            CIRCULACAO = str(linha).replace(
                                '<tr><th>Tipo de moeda</th><td>', '').replace('</td></tr>', '')

                        if 'Assunto' in str(linha):
                            ASSUNTO = str(linha).replace(
                                '<tr><th>Assunto</th><td>', '').replace('</td></tr>', '')

                        if 'Série' in str(linha):
                            SERIE = str(linha).replace(
                                '<tr><th>Série</th><td>', '').replace('</td></tr>', '')

                        if 'Soberano' in str(linha):
                            SOBERANO = str(linha).replace(
                                '<tr><th>Soberano</th><td>', '').replace('</td></tr>', '')

                        if 'Composição' in str(linha):
                            COMPOSICAO = str(linha).replace(
                                '<tr><th>Composição</th><td>', '').replace('</td></tr>', '')

                        if 'Tipo de bordo' in str(linha):
                            BORDA = str(linha).replace(
                                '<tr><th>Tipo de bordo</th><td>', '').replace('</td></tr>', '')

                        if 'Formato' in str(linha):
                            FORMATO = str(linha).replace(
                                '<tr><th>Formato</th><td>', '').replace('</td></tr>', '')

                        if 'Alinhamento' in str(linha):
                            ALINHAMENTO = str(linha).replace(
                                '<tr><th>Alinhamento</th><td>', '').replace('</td></tr>', '')

                        if 'Peso' in str(linha):
                            PESO = str(linha).replace(
                                '<tr><th>Peso (gr)</th><td>', '').replace('</td></tr>', '')

                        if 'Diametro' in str(linha):
                            DIAMETRO = str(linha).replace(
                                '<tr><th>Diametro (mm)</th><td>', '').replace('</td></tr>', '')

                        if 'Espessura' in str(linha):
                            ESPESSURA = str(linha).replace(
                                '<tr><th>Espessura (mm)</th><td>', '').replace('</td></tr>', '')

                        if 'Anverso' in str(linha):
                            ANVERSO = str(linha).replace(
                                '<tr><th class="nowrap">Anverso</th><td>', '').replace('<span class="lgray-11"> / </span>', ' / ').replace('</td></tr>', '')

                        if 'Reverso' in str(linha):
                            REVERSO = str(linha).replace(
                                '<tr><th class="nowrap">Reverso</th><td>', '').replace('<span class="lgray-11"> / </span>', ' / ').replace('</td></tr>', '')
                    Banco.cadastrar(VENDA, CUNHAGEM, FOTO1, FOTO2, CADASTRO, PAIS, ANO, KRAUSE, VALOR, PERIODO, CIRCULACAO, ASSUNTO,
                                    SERIE, SOBERANO, COMPOSICAO, BORDA, FORMATO, ALINHAMENTO, PESO, DIAMETRO, ESPESSURA, ANVERSO, REVERSO, CONSERVACAO)


novacaptura(40, 50)

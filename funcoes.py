import sqlite3
from playwright.sync_api import sync_playwright
from time import sleep
import os


class Colecao:

    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def scrap(self):

        URL = 'https://pt.ucoin.net/uid26638?v=home'
        with sync_playwright() as p:
            browser = p.webkit.launch()
            page = browser.new_page()
            page.goto(URL)
            page.click('#cookies-warning > div > div.right > div')
            # page.query_selector(id="map")
            #    sleep(8)
            page.click('#map')

            page.locator(
                '#user-map > div.modal-container > div.modal-body').screenshot(path="screenshot.png")
            browser.close()

    def upload():
        pass

    def inserir(self, pais, ano, krause, valor, moeda, tipo, qualidade, material, diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2):

        sql = "INSERT INTO colecao (pais,ano,krause,valor,moeda,tipo,qualidade,material,diametro,detalhe,anverso,reverso,valor_venda,datacadastro,imagem1,imagem2) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        self.cursor.execute(sql, (pais, ano, krause, valor, moeda, tipo, qualidade, material,
                            diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2))
        self.conn.commit()

    def editar(self, id, pais, ano, krause, valor, moeda, tipo, qualidade, material, diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2):
        sql = "UPDATE colecao SET pais=?,ano=?,krause=?,valor=?,moeda=?,tipo=?,qualidade=?,material=?,diametro=?,detalhe=?,anverso=?,reverso=?,valor_venda=?,datacadastro=?,imagem1=?,imagem2=? WHERE id=?"
        self.cursor.execute(sql, (pais, ano, krause, valor, moeda, tipo, qualidade, material,
                            diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2, id))
        self.conn.commit()

    def remover(self, id):
        sql = "DELETE FROM colecao WHERE id=?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()

    def listar_tudo(self):
        sql = "SELECT * FROM colecao"
        self.cursor.execute(sql)
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, termo):

        sql = "SELECT * FROM colecao WHERE pais LIKE ? OR ano LIKE ? OR valor LIKE ? OR moeda LIKE ? OR qualidade LIKE ? OR material LIKE ? OR anverso LIKE ? OR reverso LIKE ? "
        termo = f'%{termo}%'
        self.cursor.execute(
            sql, (termo, termo, termo, termo, termo, termo, termo, termo))
        retorno = []
        for linha in self.cursor.fetchall():
            id = str(linha[0]) + ':'
            pais = linha[1]
            ano = linha[2]
            krause = linha[3]

            moeda = linha[5]
            if not moeda == None:
                valor = linha[4] + ' ' + linha[5]
            else:
                valor = linha[4]
            tipo = linha[6]
            qualidade = linha[7]
            material = linha[8]
            diametro = linha[9]
            detalhe = linha[10]
            anverso = linha[11]
            reverso = linha[12]
            valor_venda = linha[13]
            datacadastro = linha[14]
            imagem1 = linha[15]
            imagem2 = linha[16]

            retorno.append(
                f'{str(id): <6}{str(pais): <30}\t{ano} \t{str(krause): <10} \t{str(valor): <20} \t{tipo: <10}datacadastro: {datacadastro}')
        return retorno

    def buscar_tipos(self, termo):
        if termo == 'Moeda Nacional':
            sql = "SELECT * FROM colecao WHERE pais LIKE ? AND tipo LIKE ? ORDER BY ano"
            self.cursor.execute(
                sql, ('brasil', 'moeda'))
        elif termo == 'Nota Nacional':
            sql = "SELECT * FROM colecao WHERE pais LIKE ? AND tipo LIKE ? ORDER BY ano"
            self.cursor.execute(
                sql, ('brasil', 'nota'))
        elif termo == 'Moeda Internacional':
            sql = "SELECT * FROM colecao WHERE pais NOT LIKE ? AND tipo LIKE ? ORDER BY ano"
            self.cursor.execute(
                sql, ('brasil', 'moeda'))
        elif termo == 'Nota Internacional':
            sql = "SELECT * FROM colecao WHERE pais NOT LIKE ? AND tipo LIKE ? ORDER BY ano"
            self.cursor.execute(
                sql, ('brasil', 'nota'))
        elif termo == 'Colecao Completa':
            sql = "SELECT * FROM colecao ORDER BY ano"
            self.cursor.execute(sql)
        elif termo == 'Ultimos Adicionados':
            sql = "SELECT * FROM colecao ORDER BY id DESC"
            self.cursor.execute(sql)

        retorno = []
        for linha in self.cursor.fetchall():
            id = str(linha[0]) + ':'
            pais = linha[1]
            ano = linha[2]
            krause = linha[3]

            moeda = linha[5]
            if not moeda == None:
                valor = linha[4] + ' ' + linha[5]
            else:
                valor = linha[4]
            tipo = linha[6]
            qualidade = linha[7]
            material = linha[8]
            diametro = linha[9]
            detalhe = linha[10]
            anverso = linha[11]
            reverso = linha[12]
            valor_venda = linha[13]
            datacadastro = linha[14]
            imagem1 = linha[15]
            imagem2 = linha[16]

            retorno.append(
                f'{str(id): <6}{str(pais): <30}\t{ano} \t{str(krause): <10} \t{str(valor): <20} \t{tipo: <10}datacadastro: {datacadastro}')
        return retorno

    def buscar_id(self, id):
        sql = "SELECT * FROM colecao WHERE id=?"
        self.cursor.execute(sql, (id,))
        retorno = []
        for linha in self.cursor.fetchall():
            id = linha[0]
            pais = linha[1]
            ano = linha[2]
            krause = linha[3]
            valor = linha[4]
            moeda = linha[5]
            tipo = linha[6]
            qualidade = linha[7]
            material = linha[8]
            diametro = linha[9]
            detalhe = linha[10]
            anverso = linha[11]
            reverso = linha[12]
            valor_venda = linha[13]
            datacadastro = linha[14]
            imagem1 = linha[15]
            imagem2 = linha[16]

            # retorno.append(
            # f'{id},{pais},{ano},{krause},{valor},{moeda},{tipo},{qualidade} \tmaterial {material} \tdiametro {diametro}\tdetalhe {detalhe} \tanverso {anverso} \treverso {reverso} \tvalor venda {valor_venda}\tdatacadastro: {datacadastro} \timagem1 {imagem1} \timagem2 {imagem2}')
        return linha

    def exibir_resumo_paises(self):
        # pega a lista de pais unicos
        listapais = []
        listapaismoeda = []
        listapaisnota = []
        listagem = []
        sql_pais = 'Select distinct pais as quantidade from Colecao order by pais'
        self.cursor.execute(sql_pais)
        for pais in self.cursor.fetchall():
            listapais.append(pais[0])

        # verifica a quantidade moedas de cada pais
        for pais in listapais:
            sql_qtde_moedas = f"Select count(pais) from Colecao where pais == '{pais}' and tipo == 'Moeda'"
            self.cursor.execute(sql_qtde_moedas)
            for linha in self.cursor.fetchall():
                listapaismoeda.append([pais, linha[0]])

        # verifica a quantidade notas de cada pais
        for pais in listapais:
            sql_qtde_notas = f'Select count(pais) from Colecao where pais == "{pais}" and tipo == "Nota"'
            self.cursor.execute(sql_qtde_notas)
            for linha in self.cursor.fetchall():
                listapaisnota.append([pais, linha[0]])

        for i in range(len(listapais)):
            listagem.append(
                f'{str(listapais[i]+":"): <30}\tMoedas:{listapaismoeda[i][1]}\tNotas:{listapaisnota[i][1]}')
        return listagem

    def exibir_resumo(self):
        # pega a lista de pais unicos
        mbrasil = 0
        nbrasil = 0
        nfora = 0
        mfora = 0
        valorcolecao = 0
        # verifica a quantidade moedas do brasil

        sql_qtde_moedas = f"Select * from Colecao where pais == 'Brasil' and tipo == 'Moeda'"
        self.cursor.execute(sql_qtde_moedas)
        for linha in self.cursor.fetchall():
            mbrasil += 1

        # verifica a quantidade notas do brasil
        sql_qtde_notas = f'Select * from Colecao where pais == "Brasil" and tipo == "Nota"'
        self.cursor.execute(sql_qtde_notas)
        for linha in self.cursor.fetchall():
            nbrasil += 1

        # verifica a quantidade moedas de fora do brasil
        sql_qtde_moedas = f"Select * from Colecao where pais != 'Brasil' and tipo == 'Moeda'"
        self.cursor.execute(sql_qtde_moedas)
        for linha in self.cursor.fetchall():
            mfora += 1

        # verifica a quantidade notas de fora do brasil
        sql_qtde_notas = f'Select * from Colecao where pais != "Brasil" and tipo == "Nota"'
        self.cursor.execute(sql_qtde_notas)
        for linha in self.cursor.fetchall():
            nfora += 1

        # soma os valores de venda de todas as moedas e notas
        sql_valor_moedas = f'Select sum(valor_venda) from Colecao '
        valorcolecao = self.cursor.execute(sql_valor_moedas)
        valorcolecao1 = list(valorcolecao)
        valorcolecao1 = valorcolecao1[0]

        return f'Moedas do Brasil: {mbrasil}\nNotas do Brasil: {nbrasil}\n\nMoedas estrangeiras: {mfora}\nNotas estrangeiras: {nfora}\n\nTotal de moedas: {mbrasil+mfora}\nTotal de notas: {nbrasil+nfora}\nContagem total: {mbrasil+mfora+nbrasil+nfora}\n\nValor total de coleção: R${valorcolecao1[0]:.2f}'

    def criartabela(self):
        sql = 'CREATE TABLE IF NOT EXISTS "Colecao" ("id" INTEGER,"pais" TEXT NOT NULL,"ano" TEXT NOT NULL,"krause" TEXT NOT NULL,"valor" TEXT NOT NULL,"moeda" TEXT NOT NULL,"tipo" TEXT NOT NULL,"qualidade" TEXT NOT NULL,"material" TEXT NOT NULL,"diametro" TEXT NOT NULL,"detalhe" TEXT NOT NULL,"anverso" TEXT NOT NULL,"reverso" TEXT NOT NULL,"valor_venda" TEXT NOT NULL,"datacadastro" TEXT NOT NULL,"imagem1" TEXT NOT NULL,"imagem2" TEXT NOT NULL,PRIMARY KEY("id" AUTOINCREMENT))'
        self.cursor.execute(sql)

    def importarTXT(self, tipo):
        contador = 0
        if tipo == 'total':
            sql_drop = 'DROP TABLE IF EXISTS "Colecao"'
            self.cursor.execute(sql_drop)
            self.criartabela()
            with open('bancoMoedas.txt', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    contador += 1
                    self.cursor.execute(linha)
                    self.conn.commit()

        elif tipo == 'parcial':
            with open('bancoMoedas.txt', 'r', encoding='utf-8') as arquivo:
                for linha in arquivo:
                    contador += 1
                    self.cursor.execute(linha)
                    self.conn.commit()
        return contador

    def exportarTXT(self):
        contador = 0
        ini = 'INSERT INTO Colecao (pais,ano,krause,valor,moeda,tipo,qualidade,material,diametro,detalhe,anverso,reverso,valor_venda,datacadastro,imagem1,imagem2) VALUES '
        with open('bancoMoedas.txt', 'w', encoding='utf-8') as arquivo:
            sql = 'SELECT pais,ano,krause,valor,moeda,tipo,qualidade,material,diametro,detalhe,anverso,reverso,valor_venda,datacadastro,imagem1,imagem2 FROM colecao'
            self.cursor.execute(sql)
            for linha in self.cursor.fetchall():
                contador += 1
                arquivo.write(f'{ini}{linha}\n')
        return contador

    def fechar(self):
        self.conn.close()
        self.cursor.close()

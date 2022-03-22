import sqlite3
from playwright.sync_api import sync_playwright
from time import sleep
import os
from bs4 import BeautifulSoup

# from firebase_admin import credentials, initialize_app, storage


class Colecao:

    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def scrap(self):
        try:
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
        except Exception as e:
            print(e)

    def upload():
        pass

    def inserir(self, venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto, serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao, tipo):

        sql = "INSERT INTO colecao (venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto, serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao,tipo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        self.cursor.execute(sql, (venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto,
                            serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao, tipo))
        self.conn.commit()

    def editar(self, id, venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto, serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao, tipo):
        sql = "UPDATE colecao SET venda=?, cunhagem=?, foto1=?, foto2=?, cadastro=?, pais=?, ano=?, krause=?, valor=?, periodo=?, circulacao=?, assunto=?, serie=?, soberano=?, composicao=?, borda=?, formato=?, alinhamento=?, peso=?, diametro=?, espessura=?, anverso=?, reverso=?, conservacao=?,tipo=? WHERE id=?"
        self.cursor.execute(sql, (venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto,
                            serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao, tipo, id))
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

        sql = "SELECT * FROM colecao WHERE venda LIKE ? OR cunhagem LIKE ? OR foto1 LIKE ? OR foto2 LIKE ? OR cadastro LIKE ? OR pais LIKE ? OR ano LIKE ? OR krause LIKE ? OR valor LIKE ? OR periodo LIKE ? OR circulacao LIKE ? OR assunto LIKE ? OR serie LIKE ? OR soberano LIKE ? OR composicao LIKE ? OR borda LIKE ? OR formato LIKE ? OR alinhamento LIKE ? OR peso LIKE ? OR diametro LIKE ? OR espessura LIKE ? OR anverso LIKE ? OR reverso LIKE ? OR conservacao LIKE ? OR tipo LIKE ?"
        termo = f'%{termo}%'
        self.cursor.execute(
            sql, (termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo, termo))
        retorno = []
        for linha in self.cursor.fetchall():
            # print(linha)
            id = str(linha[0]) + ':'
            pais = linha[1]
            ano = linha[2]
            krause = linha[3]
            valor = linha[4]
            periodo = linha[5]
            circulacao = linha[6]
            assunto = linha[7]
            serie = linha[8]
            soberano = linha[9]
            cunhagem = linha[10]
            composicao = linha[11]
            borda = linha[12]
            formato = linha[13]
            alinhamento = linha[14]
            peso = linha[15]
            conservacao = linha[16]
            diametro = linha[17]
            espessura = linha[18]
            anverso = linha[19]
            reverso = linha[20]
            venda = linha[21]
            cadastro = linha[22]
            foto1 = linha[23]
            foto2 = linha[24]
            tipo = linha[25]
            retorno.append(
                f'{str(id): <6}{str(pais): <30}\t{ano} \t{str(krause): <10} \t{str(valor): <20} \tdatacadastro: {cadastro}')
        return retorno

    def buscar_tipos(self, termo):
        if termo == 'Moeda Nacional':
            sql = "SELECT * FROM colecao WHERE pais LIKE ? AND tipo LIKE ?  ORDER BY ano"
            self.cursor.execute(sql, ('brasil', 'moeda'))
        elif termo == 'Nota Nacional':
            sql = "SELECT * FROM colecao WHERE pais LIKE ? AND tipo LIKE ?  ORDER BY ano"
            self.cursor.execute(
                sql, ('brasil', 'nota'))
        elif termo == 'Moeda Internacional':
            sql = "SELECT * FROM colecao WHERE pais NOT LIKE ? AND tipo LIKE ?  ORDER BY ano"
            self.cursor.execute(
                sql, ('brasil', 'moeda'))
        elif termo == 'Nota Internacional':
            sql = "SELECT * FROM colecao WHERE pais NOT LIKE ? AND tipo LIKE ?  ORDER BY ano"
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
            valor = linha[4]
            periodo = linha[5]
            circulacao = linha[6]
            assunto = linha[7]
            serie = linha[8]
            soberano = linha[9]
            cunhagem = linha[10]
            composicao = linha[11]
            borda = linha[12]
            formato = linha[13]
            alinhamento = linha[14]
            peso = linha[15]
            conservacao = linha[16]
            diametro = linha[17]
            espessura = linha[18]
            anverso = linha[19]
            reverso = linha[20]
            venda = linha[21]
            cadastro = linha[22]
            foto1 = linha[23]
            foto2 = linha[24]
            tipo = linha[25]
            retorno.append(
                f'{str(id): <6}{str(pais): <30}\t{ano} \t{str(krause): <10} \t{str(valor): <20} \tdatacadastro: {cadastro}')
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
            periodo = linha[5]
            circulacao = linha[6]
            assunto = linha[7]
            serie = linha[8]
            soberano = linha[9]
            cunhagem = linha[10]
            composicao = linha[11]
            borda = linha[12]
            formato = linha[13]
            alinhamento = linha[14]
            peso = linha[15]
            conservacao = linha[16]
            diametro = linha[17]
            espessura = linha[18]
            anverso = linha[19]
            reverso = linha[20]
            venda = linha[21]
            cadastro = linha[22]
            foto1 = linha[23]
            foto2 = linha[24]
            tipo = linha[25]
            # retorno.append(
            # f'{id},{pais},{ano},{krause},{valor},{moeda},{tipo},{qualidade} \tmaterial {material} \tdiametro {diametro}\tdetalhe {detalhe} \tanverso {anverso} \treverso {reverso} \tvalor venda {valor_venda}\tdatacadastro: {datacadastro} \timagem1 {imagem1} \timagem2 {imagem2}')
        return linha

    def exibir_resumo_paises(self):
        # pega a lista de pais unicos
        listapais = []
        listapaismoeda = []
        listapaisnota = []
        listagem = []
        sql_pais = 'Select distinct pais as quantidade FROM colecao order by pais'
        self.cursor.execute(sql_pais)
        for pais in self.cursor.fetchall():
            listapais.append(pais[0])

        # verifica a quantidade moedas de cada pais
        for pais in listapais:
            sql_qtde_moedas = f"Select count(pais) FROM colecao where pais == '{pais}'"
            self.cursor.execute(sql_qtde_moedas)
            for linha in self.cursor.fetchall():
                listapaismoeda.append([pais, linha[0]])

        # # verifica a quantidade notas de cada pais
        for pais in listapais:
            sql_qtde_notas = f'Select count(pais) from Colecao where pais == "{pais}" and tipo == "Nota"'
            self.cursor.execute(sql_qtde_notas)
            for linha in self.cursor.fetchall():
                listapaisnota.append([pais, linha[0]])

        for i in range(len(listapais)):
            listagem.append(
                f'{str(listapais[i]+":"): <30}\tMoedas:{listapaismoeda[i][1]}')
        return listagem

    def exibir_resumo(self):
        try:
            # pega a lista de pais unicos
            mbrasil = 0
            nbrasil = 0
            nfora = 0
            mfora = 0
            valorcolecao = 0
            # verifica a quantidade moedas do brasil

            sql_qtde_moedas = f"Select * FROM colecao where pais == 'Brasil' and tipo == 'moeda'"
            self.cursor.execute(sql_qtde_moedas)
            for linha in self.cursor.fetchall():
                mbrasil += 1

            # # verifica a quantidade notas do brasil
            sql_qtde_notas = f'Select * FROM colecao where pais == "Brasil" and tipo == "Nota"'
            self.cursor.execute(sql_qtde_notas)
            for linha in self.cursor.fetchall():
                nbrasil += 1

            # verifica a quantidade moedas de fora do brasil
            sql_qtde_moedas = f"Select * FROM colecao where pais != 'Brasil' and tipo == 'moeda'"
            self.cursor.execute(sql_qtde_moedas)
            for linha in self.cursor.fetchall():
                mfora += 1

            # # verifica a quantidade notas de fora do brasil
            sql_qtde_notas = f'Select * FROM colecao where pais != "Brasil" and tipo == "Nota"'
            self.cursor.execute(sql_qtde_notas)
            for linha in self.cursor.fetchall():
                nfora += 1

            # soma os valores de venda de todas as moedas e notas
            sql_valor_moedas = f'Select sum(venda) FROM colecao '
            valorcolecao = self.cursor.execute(sql_valor_moedas)
            valorcolecao1 = list(valorcolecao)
            valorcolecao1 = valorcolecao1[0]
            return f'Moedas do Brasil: {mbrasil}\nNotas do Brasil: {nbrasil}\n\nMoedas estrangeiras: {mfora}\nNotas estrangeiras: {nfora}\n\nTotal de moedas: {mbrasil+mfora}\nContagem total: {mbrasil+mfora+nfora+nbrasil}\n\nValor total de coleção: R${valorcolecao1[0]:.2f}'

        except Exception as e:
            return f'Não há dados para exibir: {e}'

    def criartabela(self):
        sql = 'CREATE TABLE IF NOT EXISTS "moedas"( "id" INTEGER UNIQUE, "PAIS" TEXT, "ANO" TEXT, "KRAUSE" TEXT, "VALOR" TEXT, "PERIODO" TEXT, "CIRCULACAO" TEXT, "ASSUNTO" TEXT, "SERIE" TEXT, "SOBERANO" TEXT, "CUNHAGEM" TEXT, "COMPOSICAO" TEXT, "BORDA" TEXT, "FORMATO" TEXT, "ALINHAMENTO" TEXT, "PESO" TEXT, "CONSERVACAO" TEXT, "DIAMETRO" TEXT, "ESPESSURA" TEXT, "ANVERSO" TEXT, "REVERSO" TEXT, "VENDA" TEXT, "CADASTRO" TEXT, "FOTO1" TEXT, "FOTO2" TEXT, "TIPO" TEXT, PRIMARY KEY("id" AUTOINCREMENT) )'
        self.cursor.execute(sql)

    def exportarTXT(self):
        contador = 0
        ini = 'INSERT INTO Colecao (pais,ano,krause,valor,moeda,tipo,qualidade,material,diametro,detalhe,anverso,reverso,valor_venda,datacadastro,imagem1,imagem2) VALUES ('
        with open('bancoMoedas.txt', 'w', encoding='utf-8') as arquivo:
            sql = 'SELECT * FROM colecao'
            self.cursor.execute(sql)
            for linha in self.cursor.fetchall():
                pais = linha[1]
                ano = linha[2]
                krause = linha[3]
                valor = linha[4]
                valor1 = valor.split('\xa0')
                periodo = linha[5]
                circulacao = linha[6]
                assunto = linha[7]
                serie = linha[8]
                soberano = linha[9]
                cunhagem = linha[10]
                composicao = linha[11]
                borda = linha[12]
                formato = linha[13]
                alinhamento = linha[14]
                peso = linha[15]
                conservacao = linha[16]
                diametro = linha[17]
                espessura = linha[18]
                anverso = linha[19]
                anverso = anverso.replace("'", "")
                reverso = linha[20]
                reverso = reverso.replace("'", "")
                venda = linha[21]
                cadastro = linha[22]
                foto1 = linha[23]
                foto2 = linha[24]
                tipo = linha[25]
                tipo = tipo.capitalize()
                detalhe = f'PERIODO {periodo} CIRCULACAO {circulacao} ASSUNTO {assunto} SERIE {serie} SOBERANO {soberano} CUNHAGEM {cunhagem} BORDA {borda} FORMATO {formato} ALINHAMENTO {alinhamento} PESO {peso} ESPESSURA {espessura}'
                detalhe = detalhe.replace("'", "")
                contador += 1
                # arquivo.write(f'{valor1[0]} = {" ".join(valor1[1:])}\n')
                texto = f"{ini}'{pais}',{ano},'{krause}','{valor1[0]}','{' '.join(valor1[1:])}','{tipo}','{conservacao}','{composicao}','{diametro}','{detalhe}','{anverso}','{reverso}','{venda}','{cadastro}','{foto1}','{foto2}');\n"
                arquivo.write(texto.replace('\n', '')+'\n')
        return contador

    def fechar(self):
        self.conn.close()
        self.cursor.close()

    # def deletemapa(self, caminho, arquivo):
    #     try:
    #         '''
    #         screenshot = 'minha-colecao-a01d5.appspot.com'
    #         banco='minha-colecao-a01d5.appspot.com/Y2hyaXN0aWFuLmNvbGl2ZWlyYUBnbWFpbC5jb20=/bancodados'
    #         '''
    #         # Init firebase with your credentials
    #         cred = credentials.Certificate(
    #             "minha-colecao-a01d5-firebase-adminsdk-ehm8b-b1a0aed377.json")
    #         initialize_app(cred, {'storageBucket': caminho})

    #         # remove image
    #         bucket = storage.bucket()
    #         blob = bucket.blob('screenshot.png')
    #         blob.delete()
    #     except Exception as e:
    #         print(e)

    # def upload(self, caminho, arquivo):
    #     try:
    #         '''
    #         screenshot = 'minha-colecao-a01d5.appspot.com'
    #         banco='minha-colecao-a01d5.appspot.com/Y2hyaXN0aWFuLmNvbGl2ZWlyYUBnbWFpbC5jb20=/bancodados'
    #         '''
    #         # Init firebase with your credentials
    #         try:
    #             cred = credentials.Certificate(
    #                 "minha-colecao-a01d5-firebase-adminsdk-ehm8b-b1a0aed377.json")
    #             initialize_app(cred, {'storageBucket': caminho})
    #         except:
    #             pass

    #         # upload image
    #         fileName = arquivo
    #         bucket = storage.bucket()
    #         blob = bucket.blob(fileName)
    #         blob.upload_from_filename(fileName)

    #         # Opt : if you want to make public access from the URL
    #         blob.make_public()

    #         print("your file url", blob.public_url)

    #         # /Y2hyaXN0aWFuLmNvbGl2ZWlyYUBnbWFpbC5jb20=/bancodados
    #     except Exception as e:
    #         print(e)

    def captura_infos(self, link):
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

                info = soup.find_all('table', class_='coin-info')
                soupinfo = BeautifulSoup(
                    str(info), 'html.parser', from_encoding='utf-8')
                linhasinfo = soupinfo.find_all('tr')

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

                return VENDA, CUNHAGEM, FOTO1, FOTO2, PAIS, ANO, KRAUSE, VALOR, PERIODO, CIRCULACAO, ASSUNTO, SERIE, SOBERANO, COMPOSICAO, BORDA, FORMATO, ALINHAMENTO, PESO, DIAMETRO, ESPESSURA, ANVERSO, REVERSO
                VENDA, CUNHAGEM, FOTO1, FOTO2, CADASTRO, PAIS, ANO, KRAUSE, VALOR, PERIODO, CIRCULACAO, ASSUNTO, SERIE, SOBERANO, COMPOSICAO, BORDA, FORMATO, ALINHAMENTO, PESO, DIAMETRO, ESPESSURA, ANVERSO, REVERSO, CONSERVACAO = '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''


if __name__ == '__main__':
    a = Colecao('db_colecao.db')
    # print(a.buscar('KM# 68'))
    # print(a.buscar_id(2))
    # print(a.exibir_resumo_paises())
    print(a.exibir_resumo())
    a.exportarTXT()

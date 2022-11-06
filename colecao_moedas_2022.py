# compilar usando
# venv\Scripts\pyinstaller.exe -F --console -w --upx-dir=D:\Python Projects\upx-3.96-win64 --distpath .\ --ico .\icone.ico --name "Coleção de Moedas 2022" .\colecao_moedas_2022.py
# C:\Users\Christian\AppData\Roaming\Python\Python310\Scripts\pyinstaller.exe -F --console -w --upx-dir=D:\upx-3.96-win64 --distpath .\ --ico .\icone.ico --name "Coleção de Moedas 2022" .\colecao_moedas_2022.py

from os import link
from pprint import pprint
import sys
from threading import Thread
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

colecao = Colecao('db_colecao.db')


'''
THREADS
'''


class th(Thread):
    # declarar as variaveis que terão interação da funcao com a interface UI
    def __init__(self, imagem1, imagem2, edt1, edt2):
        # variaveis que herdam os componentes
        self.img1 = imagem1
        self.img2 = imagem2
        self.ed1 = edt1
        self.ed2 = edt2

        super().__init__()

    def mostra_fotos(self):
        self.img1.setVisible(True)
        self.img2.setVisible(True)
        pixmap = QPixmap('noimage.jpg')
        pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.img1.setPixmap(pixmap)
        self.img2.setPixmap(pixmap)
        try:
            if self.ed1.text() != '' or self.ed1.text() != ' ':
                with requests.Session() as session:
                    resp_2 = session.get(self.ed1.text(),
                                         headers={'User-Agent': 'Mozilla/5.0'})
                    with open("foto1.jpg", "wb") as f:
                        f.write(resp_2.content)

            #     data = urllib.request.urlopen(self.ed1.text()).read()
            #     print(self.ed1.text())
                        pixmap = QPixmap('foto1.jpg')

                        pixmap = pixmap.scaled(
                            300, 300, QtCore.Qt.KeepAspectRatio)
                        self.img1.setPixmap(pixmap)

        except Exception as e:
            print(e)

        try:
            with requests.Session() as session:
                resp_2 = session.get(self.ed2.text(),
                                     headers={'User-Agent': 'Mozilla/5.0'})
                with open("foto2.jpg", "wb") as f:
                    f.write(resp_2.content)

                    # data = urllib.request.urlopen(self.ed1.text()).read()
                    # print(self.ed1.text())
                    pixmap = QPixmap('foto2.jpg')

                    pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
                    self.img2.setPixmap(pixmap)

        except Exception as e:
            print(e)

    def run(self):
        self.mostra_fotos()


'''
FIM THREADS
'''


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        colecao.criartabela()
        # inicio da aplicacao
        try:
            os.mkdir('backupDB')
        except:
            pass
        pixmap = QPixmap('screenshot.png')
        scaled = pixmap.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
        self.mapa.setPixmap(scaled)

        self.label_ucoin.setVisible(False)
        self.ed_link_ucoin.setVisible(False)
        self.bt_buscar_ucoin.setVisible(False)

        self.actionGerar_Backup.triggered.connect(self.backupBanco)
        # menus
        self.menuResumo.triggered.connect(self.exiberesumo)
        # menu de cadastro de moedas
        self.adicionaMoeda.triggered.connect(
            partial(self.exibe_frame_de_cadastro, tipo='Moeda'))
        # menu de cadastro de notas
        self.adicionaNota.triggered.connect(
            partial(self.exibe_frame_de_cadastro, tipo='Nota'))
        # menu de pesquisa por palavra
        self.pesquisar.triggered.connect(
            partial(self.exibe_frame_de_pesquisa, tipo='pesquisa'))
        # menu que exibe a colecao completa
        self.ColecaoCompleta.triggered.connect(
            partial(self.exibe_frame_de_pesquisa, tipo='Colecao Completa'))
        # menu moedas internacionais
        self.MoedasInternacional.triggered.connect(
            partial(self.exibe_frame_de_pesquisa, tipo='Moeda Internacional'))
        # menu notas internacionais
        self.NotasInternacional.triggered.connect(
            partial(self.exibe_frame_de_pesquisa, tipo='Nota Internacional'))
        # menu moedas nacionais
        self.MoedasNacional.triggered.connect(
            partial(self.exibe_frame_de_pesquisa, tipo='Moeda Nacional'))
        # menu notas nacionais
        self.NotasNacional.triggered.connect(
            partial(self.exibe_frame_de_pesquisa, tipo='Nota Nacional'))
        # menu resumo por pais
        self.listar_por_pais.triggered.connect(
            partial(self.exibe_frame_de_pesquisa, tipo='Resumo Por Pais'))
        # menu atualiza imagem do mapa
        self.Atualizar_Imagem.triggered.connect(partial(self.scrap_img))
        # menu de exportacao do banco sql
        self.Exportar_TXT.triggered.connect(self.exportar_banco_sql)
        # menu de importacao do banco sql parcial
        self.sqlParcial.triggered.connect(
            partial(self.importar_banco_sql, tipo='parcial'))
        # menu de importacao do banco sql total
        self.sqlTotal.triggered.connect(
            partial(self.importar_banco_sql, tipo='total'))
        # menu ultimos registros
        self.ultimos_adicionados.triggered.connect(
            partial(self.exibe_frame_de_pesquisa, tipo='Ultimos Adicionados'))

        # botoes
        # botão cadastrar
        self.bt_cadastrar.clicked.connect(self.fcadastrar)
        # botão pesquisar
        self.bt_localizar.clicked.connect(
            partial(self.exibe_frame_de_pesquisa, tipo='pesquisa'))
        # botao mostrar fotos no frame de cadastro
        self.bt_mostrar_foto.clicked.connect(self.exibeafoto)
        # botao cancelar cadastro
        self.bt_cancelar.clicked.connect(self.cancelar)
        # botao apagar registro
        self.bt_deletar_reg.clicked.connect(self.apagar_registro)

        self.bt_scrap.clicked.connect(self.pega_info_ucoin)

        self.bt_buscar_ucoin.clicked.connect(
            lambda: self.envia_info_cadastro(self.ed_link_ucoin.text()))

        self.exiberesumo()

    def exibeafoto(self):
        t = th(imagem1=self.foto_anverso, imagem2=self.foto_reverso,
               edt1=self.ed_foto1, edt2=self.ed_foto2)
        retorno = t.start()

    def exibelista(self):
        self.frame_cadastro.hide()
        self.frame_listar.show()
        self.frame_resumo.hide()

    def exibecadastro(self):
        self.frame_cadastro.show()
        self.frame_listar.hide()
        self.frame_resumo.hide()

    def exiberesumo(self):
        self.frame_cadastro.hide()
        self.frame_resumo.show()
        self.frame_listar.hide()

        txt_resumo = colecao.exibir_resumo()
        # print(txt_resumo)
        self.resumo.setText(txt_resumo)

    def fcadastrar(self):
        '''funcao para cadastrar um item'''
        pais = self.ed_pais.text().capitalize()
        ano = self.ed_ano.text()
        krause = self.ed_krause.text()
        valor = self.ed_valor.text()
        periodo = self.ed_periodo.text()
        circulacao = self.ed_circulacao.text()
        assunto = self.ed_assunto.text()
        serie = self.ed_serie.text()
        soberano = self.ed_soberano.text()
        cunhagem = self.ed_cunhagem.text()
        composicao = self.ed_composicao.text()
        borda = self.ed_borda.text()
        formato = self.ed_formato.text()
        alinhamento = self.ed_alinhamento.text()
        peso = self.ed_peso.text()
        conservacao = self.ed_conservacao.text()
        diametro = self.ed_diametro.text()
        espessura = self.ed_espessura.text()
        anverso = self.ed_anverso.text()
        reverso = self.ed_reverso.text()
        venda = self.ed_venda.text()
        tipo = self.ed_tipo.text()
        foto1 = self.ed_foto1.text()
        foto2 = self.ed_foto2.text()
        data_atual = date.today()
        data_cadastro = self.lbl_data.text()
        cadastro = data_atual.strftime('%d/%m/%Y')
        id = self.lbl_id.text()
        print(id, type(id))
        if pais and ano and krause and valor:

            # Verifica se os campos nao estao vazios
            if id == '':
                colecao.inserir(venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto,
                                serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao, tipo)

                self.lbl_status_cadastro.setText(
                    'Item cadastrado com sucesso')
                self.limpa_form_cadastro()
                QMessageBox.about(
                    self, 'Cadastro', f'Registro criado com sucesso!\n{ano} {pais} {valor}\n'
                    f'{conservacao} {composicao} {diametro}\n{peso}\n{anverso} {reverso} {valor}')
            else:
                colecao.editar(id, venda, cunhagem, foto1, foto2, data_cadastro, pais, ano, krause, valor, periodo, circulacao, assunto,
                               serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao, tipo)
                self.lbl_status_cadastro.setText(
                    'Item atualizado com sucesso')
                QMessageBox.about(
                    self, 'Cadastro', f'Registro criado com sucesso!\n{ano} {pais} {valor}\n'
                    f'{conservacao} {composicao} {diametro}\n{peso}\n{anverso} {reverso} {valor}')
            self.exiberesumo()
        else:
            QMessageBox.about(self, 'Erro ao Cadastrar',
                              f'É necessário que todos os campos sejam preenchidos!\n')

    def limpa_form_cadastro(self):
        self.lbl_id.setText('')
        self.ed_pais.setText('')
        self.ed_ano.setText('')
        self.ed_krause.setText('')
        self.ed_valor.setText('')
        self.ed_periodo.setText('')
        self.ed_circulacao.setText('')
        self.ed_assunto.setText('')
        self.ed_serie.setText('')
        self.ed_soberano.setText('')
        self.ed_cunhagem.setText('')
        self.ed_composicao.setText('')
        self.ed_borda.setText('')
        self.ed_formato.setText('')
        self.ed_alinhamento.setText('')
        self.ed_peso.setText('')
        self.ed_conservacao.setText('')
        self.ed_diametro.setText('')
        self.ed_espessura.setText('')
        self.ed_anverso.setText('')
        self.ed_reverso.setText('')
        self.ed_foto1.setText('')
        self.ed_foto2.setText('')
        self.ed_venda.setText('')
        self.ed_tipo.setText('')
        self.foto_anverso.setVisible(False)
        self.foto_reverso.setVisible(False)
        self.lbl_status_cadastro.setText('')

    def exibe_moeda(self, id, opcao):
        '''Exibe o item clicado'''
        self.exibecadastro()

        linha = colecao.buscar_id(id)
        self.lbl_id.setText(str(linha[0]))
        self.ed_pais.setText(str(linha[1]))
        self.ed_ano.setText(str(linha[2]))
        self.ed_krause.setText(str(linha[3]))
        self.ed_valor.setText(str(linha[4]))
        self.ed_periodo.setText(str(linha[5]))
        self.ed_circulacao.setText(str(linha[6]))
        self.ed_assunto.setText(str(linha[7]))
        self.ed_serie.setText(str(linha[8]))
        self.ed_soberano.setText(str(linha[9]))
        self.ed_cunhagem.setText(str(linha[10]))
        self.ed_composicao.setText(str(linha[11]))
        self.ed_borda.setText(str(linha[12]))
        self.ed_formato.setText(str(linha[13]))
        self.ed_alinhamento.setText(str(linha[14]))
        self.ed_peso.setText(str(linha[15]))
        self.ed_conservacao.setText(str(linha[16]))
        self.ed_diametro.setText(str(linha[17]))
        self.ed_espessura.setText(str(linha[18]))
        self.ed_anverso.setText(str(linha[19]))
        self.ed_reverso.setText(str(linha[20]))
        self.ed_foto1.setText(str(linha[23]))
        self.ed_foto2.setText(str(linha[24]))
        self.ed_venda.setText(str(linha[21]))
        self.lbl_data.setText(str(linha[22]))
        self.ed_tipo.setText(str(linha[25]))

        self.bt_deletar_reg.setVisible(True)
        self.bt_mostrar_foto.setVisible(False)
        self.bt_cadastrar.setText('Atualizar')

        self.exibeafoto()

    def exibe_frame_de_pesquisa(self, tipo):
        self.limpa_form_cadastro()
        self.exibelista()
        self.list_item.clear()
        self.ed_localizar.setFocus()

        # tela de pesquisa por palavra
        if tipo == 'pesquisa':
            termo = self.ed_localizar.text()
            print(termo)
            if not termo == '':
                self.list_item.clear()
                itens = colecao.buscar(termo)
                self.lbl_titulo_2.setText(
                    'Resultado da pesquisa por: ' + termo.upper())

        # tela de pesquisa por moeda nacional
        elif tipo == 'Moeda Nacional':
            itens = colecao.buscar_tipos(tipo)
            self.lbl_titulo_2.setText(str(tipo))
        # tela de pesquisa por nota nacional
        elif tipo == 'Nota Nacional':
            itens = colecao.buscar_tipos(tipo)
            self.lbl_titulo_2.setText(str(tipo))
        # tela de pesquisa por moeda estrangeira
        elif tipo == 'Moeda Internacional':
            itens = colecao.buscar_tipos(tipo)
            self.lbl_titulo_2.setText(str(tipo))
        # tela de pesquisa por nota estrangeira
        elif tipo == 'Nota Internacional':
            itens = colecao.buscar_tipos(tipo)
            self.lbl_titulo_2.setText(str(tipo))
        # tela de pesquisa da colecao completa
        elif tipo == 'Colecao Completa':
            itens = colecao.buscar_tipos(tipo)
            self.lbl_titulo_2.setText(str(tipo))
        # tela de resumo por pais
        elif tipo == 'Resumo Por Pais':
            itens = colecao.exibir_resumo_paises()
            self.lbl_titulo_2.setText(str(tipo))
        # tela de ultimos cadastrados
        elif tipo == 'Ultimos Adicionados':
            itens = colecao.buscar_tipos(tipo)
            self.lbl_titulo_2.setText(str(tipo))

        # preenche a tela com os dados da pesquisa
        try:

            for item in itens:
                self.list_item.addItem(item)
            if self.list_item.count() == 0:
                self.list_item.clear()
                self.list_item.addItem('Nenhum item encontrado')
                self.lbl_status.setText('')
            else:
                self.lbl_status.setText(
                    f'{self.list_item.count()} itens encontrados')
        except Exception as e:
            print(e)
            self.list_item.clear()
            self.list_item.addItem('Nenhum item encontrado')
            self.lbl_status.setText('')

        def abre_item_selecionado(item):
            '''duplo clique para abrir o item'''
            id = str(item.text()).split(':')[0].strip()
            self.lbl_titulo.setText(f'Atualizar Registro: {id}')

            try:
                self.exibe_moeda(id, 'atualizar')

            except Exception as e:
                print(e)
                self.exibelista()
                self.ed_localizar.setText(id)

                self.bt_localizar.animateClick(10)

        self.list_item.itemDoubleClicked.connect(
            lambda: abre_item_selecionado(item=self.list_item.currentItem()))

    def exibe_frame_de_cadastro(self, tipo):
        '''Exibe o frame de cadastro'''
        self.bt_deletar_reg.setVisible(False)
        self.limpa_form_cadastro()
        self.exibecadastro()
        self.lbl_titulo.setText(f'Cadastrar nova {str(tipo).lower()}')
        self.bt_cadastrar.setText('Cadastrar')
        self.bt_mostrar_foto.setVisible(True)
        self.ed_tipo.setText(tipo)

    def cancelar(self):
        self.exiberesumo()
        self.limpa_form_cadastro()

    def confirma_apagar(self):
        pass

    def apagar_registro(self):
        print('apagar')
        '''Apaga o registro selecionado'''
        ret = QMessageBox.question(
            self, 'ATENÇÃO!!!', f"Tem certeza que deseja apagar o item:\n{self.ed_ano.text()} {self.ed_pais.text()} {self.ed_valor.text()} ", QMessageBox.Yes | QMessageBox.Cancel)

        if ret == QMessageBox.Yes:
            colecao.remover(self.lbl_id.text())
            QMessageBox.about(
                self, 'Apagado', 'Registro apagado com sucesso')
            self.limpa_form_cadastro()
            self.exiberesumo()

    def carregaimagemFundo(self):
        pixmap = QPixmap('screenshot.png')
        scaled = pixmap.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
        self.mapa.setPixmap(scaled)
        self.mapa.setVisible(True)

    def pega_info_ucoin(self):
        self.label_ucoin.setVisible(True)
        self.ed_link_ucoin.setVisible(True)
        self.bt_buscar_ucoin.setVisible(True)

    def envia_info_cadastro(self, link):
        VENDA, CUNHAGEM, FOTO1, FOTO2, PAIS, ANO, KRAUSE, VALOR, PERIODO, CIRCULACAO, ASSUNTO, SERIE, SOBERANO, COMPOSICAO, BORDA, FORMATO, ALINHAMENTO, PESO, DIAMETRO, ESPESSURA, ANVERSO, REVERSO = colecao.captura_infos(
            link)
        self.ed_pais.setText(PAIS)
        self.ed_ano.setText(ANO)
        self.ed_krause.setText(KRAUSE)
        self.ed_valor.setText(VALOR)
        self.ed_periodo.setText(PERIODO)
        self.ed_circulacao.setText(CIRCULACAO)
        self.ed_assunto.setText(ASSUNTO)
        self.ed_serie.setText(SERIE)
        self.ed_soberano.setText(SOBERANO)
        self.ed_cunhagem.setText(CUNHAGEM)
        self.ed_composicao.setText(COMPOSICAO)
        self.ed_borda.setText(BORDA)
        self.ed_formato.setText(FORMATO)
        self.ed_alinhamento.setText(ALINHAMENTO)
        self.ed_peso.setText(PESO)
        self.ed_diametro.setText(DIAMETRO)
        self.ed_espessura.setText(ESPESSURA)
        self.ed_anverso.setText(ANVERSO)
        self.ed_reverso.setText(REVERSO)
        self.ed_foto1.setText(FOTO1)
        self.ed_foto2.setText(FOTO2)
        self.ed_venda.setText(VENDA)
        self.label_ucoin.setVisible(False)
        self.ed_link_ucoin.setVisible(False)
        self.bt_buscar_ucoin.setVisible(False)
        self.ed_link_ucoin.setText('')

    def scrap_img(self):
        QMessageBox.about(
            self, 'Vai demorar....', 'Este processo pode demorar um pouco :/')
        colecao.scrap()
        self.carregaimagemFundo()
        # colecao.deletemapa(caminho='minha-colecao-a01d5.appspot.com',
        #                    arquivo='screenshot.png')
        # colecao.upload(caminho='minha-colecao-a01d5.appspot.com',
        #                arquivo='screenshot.png')

    def exportar_banco_sql(self):
        qtde = colecao.exportarTXT()
        QMessageBox.about(
            self, 'Backup', f'O arquivo TXT com o backup foi gerado com sucesso\n{qtde} registros exportados')
        self.backupBanco()

    def importar_banco_sql(self, tipo):
        with open(f'bancoMoedas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            contador = 0
            for linha in linhas:
                contador += 1

        if tipo == 'parcial':
            ret = QMessageBox.question(
                self, 'MUITA ATENÇÃO!!!', f"Tem certeza que deseja importar o arquivo TXT?\n{contador} registros encontrados", QMessageBox.Yes | QMessageBox.Cancel)
            if ret == QMessageBox.Yes:
                colecao.criartabela()
                qtde = colecao.importarTXT(tipo=tipo)
                QMessageBox.about(
                    self, 'Importação', f'O arquivo TXT com o backup foi importado com sucesso\n{qtde} registros foram importados')
        elif tipo == 'total':
            ret = QMessageBox.question(
                self, 'MUITA ATENÇÃO!!!', f"Tem certeza que deseja apagar TODO o banco e importar o arquivo TXT?\n{contador} registros encontrados", QMessageBox.Yes | QMessageBox.Cancel)
            if ret == QMessageBox.Yes:
                qtde = colecao.importarTXT(tipo=tipo)
                QMessageBox.about(
                    self, 'Importação', f'Registros importados com sucesso!\n{qtde} registros foram importados')

    def backupBanco(self):
        try:
            hoje = datetime.now().strftime('%d-%m-%Y')
            hoje = str(hoje).replace(':', ' ')
            import shutil
            shutil.make_archive(f'backupDB\\db_colecao.db_{hoje}', 'zip',
                                './', 'db_colecao.db')
            QMessageBox.about(
                self, 'Backup', f'O backup foi gerado com sucesso')
        except Exception as e:
            QMessageBox.about(
                self, 'Backup', f'Ocorreu um erro ao gerar o backup\n{e}')


qt = QApplication(sys.argv)

novo = Novo()
novo.show()
qt.exec_()

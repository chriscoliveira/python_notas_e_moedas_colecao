from pprint import pprint
import sys
from threading import Thread
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from layout import *
from functools import partial
from datetime import date
import requests
import urllib
from funcoes import Colecao

colecao = Colecao('db_colecao.db')
colecao.criartabela()
# inicio da aplicacao
app = QtWidgets.QApplication([])

prog = uic.loadUi('layout.ui')
pixmap = QPixmap('screenshot.png')
scaled = pixmap.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
prog.mapa.setPixmap(scaled)


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

            with requests.Session() as session:
                resp_2 = session.get(self.ed1.text(),
                                     headers={'User-Agent': 'Mozilla/5.0'})
                with open("foto1.jpg", "wb") as f:
                    f.write(resp_2.content)

        #     data = urllib.request.urlopen(self.ed1.text()).read()
        #     print(self.ed1.text())
                    pixmap = QPixmap('foto1.jpg')

                    pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
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


def exibeafoto():
    t = th(imagem1=prog.foto_anverso, imagem2=prog.foto_reverso,
           edt1=prog.ed_foto1, edt2=prog.ed_foto2)
    retorno = t.start()


def exibelista():
    prog.frame_cadastro.hide()
    prog.frame_listar.show()
    prog.frame_resumo.hide()


def exibecadastro():
    prog.frame_cadastro.show()
    prog.frame_listar.hide()
    prog.frame_resumo.hide()


def exiberesumo():
    prog.frame_cadastro.hide()
    prog.frame_resumo.show()
    prog.frame_listar.hide()

    txt_resumo = colecao.exibir_resumo()
    prog.resumo.setText(txt_resumo)


def fcadastrar():
    '''funcao para cadastrar um item'''
    pais = prog.ed_pais.text().capitalize()
    ano = prog.ed_ano.text()
    krause = prog.ed_krause.text()
    valor = prog.ed_valor.text()
    periodo = prog.ed_periodo.text()
    circulacao = prog.ed_circulacao.text()
    assunto = prog.ed_assunto.text()
    serie = prog.ed_serie.text()
    soberano = prog.ed_soberano.text()
    cunhagem = prog.ed_cunhagem.text()
    composicao = prog.ed_composicao.text()
    borda = prog.ed_borda.text()
    formato = prog.ed_formato.text()
    alinhamento = prog.ed_alinhamento.text()
    peso = prog.ed_peso.text()
    conservacao = prog.ed_conservacao.text()
    diametro = prog.ed_diametro.text()
    espessura = prog.ed_espessura.text()
    anverso = prog.ed_anverso.text()
    reverso = prog.ed_reverso.text()
    venda = prog.ed_venda.text()
    tipo = prog.ed_tipo.text()
    foto1 = prog.ed_foto1.text()
    foto2 = prog.ed_foto2.text()
    data_atual = date.today()
    data_cadastro = prog.lbl_data.text()
    cadastro = data_atual.strftime('%d/%m/%Y')
    id = prog.lbl_id.text()
    print(id, type(id))
    if pais and ano and krause and valor:

        # Verifica se os campos nao estao vazios
        if id == '':
            colecao.inserir(venda, cunhagem, foto1, foto2, cadastro, pais, ano, krause, valor, periodo, circulacao, assunto,
                            serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao, tipo)

            prog.lbl_status_cadastro.setText(
                'Item cadastrado com sucesso')
            limpa_form_cadastro()
            QMessageBox.about(
                prog, 'Cadastro', f'Registro criado com sucesso!\n{ano} {pais} {valor}\n'
                f'{conservacao} {composicao} {diametro}\n{peso}\n{anverso} {reverso} {valor}')
        else:
            colecao.editar(id, venda, cunhagem, foto1, foto2, data_cadastro, pais, ano, krause, valor, periodo, circulacao, assunto,
                           serie, soberano, composicao, borda, formato, alinhamento, peso, diametro, espessura, anverso, reverso, conservacao, tipo)
            prog.lbl_status_cadastro.setText(
                'Item atualizado com sucesso')
            QMessageBox.about(
                prog, 'Cadastro', f'Registro criado com sucesso!\n{ano} {pais} {valor}\n'
                f'{conservacao} {composicao} {diametro}\n{peso}\n{anverso} {reverso} {valor}')
        exiberesumo()
    else:
        QMessageBox.about(prog, 'Erro ao Cadastrar',
                          f'É necessário que todos os campos sejam preenchidos!\n')


def limpa_form_cadastro():
    prog.lbl_id.setText('')
    prog.ed_pais.setText('')
    prog.ed_ano.setText('')
    prog.ed_krause.setText('')
    prog.ed_valor.setText('')
    prog.ed_periodo.setText('')
    prog.ed_circulacao.setText('')
    prog.ed_assunto.setText('')
    prog.ed_serie.setText('')
    prog.ed_soberano.setText('')
    prog.ed_cunhagem.setText('')
    prog.ed_composicao.setText('')
    prog.ed_borda.setText('')
    prog.ed_formato.setText('')
    prog.ed_alinhamento.setText('')
    prog.ed_peso.setText('')
    prog.ed_conservacao.setText('')
    prog.ed_diametro.setText('')
    prog.ed_espessura.setText('')
    prog.ed_anverso.setText('')
    prog.ed_reverso.setText('')
    prog.ed_foto1.setText('')
    prog.ed_foto2.setText('')
    prog.ed_venda.setText('')
    prog.ed_tipo.setText('')
    prog.foto_anverso.setVisible(False)
    prog.foto_reverso.setVisible(False)
    prog.lbl_status_cadastro.setText('')


def exibe_moeda(id, opcao):
    '''Exibe o item clicado'''
    exibecadastro()

    linha = colecao.buscar_id(id)
    prog.lbl_id.setText(str(linha[0]))
    prog.ed_pais.setText(str(linha[1]))
    prog.ed_ano.setText(str(linha[2]))
    prog.ed_krause.setText(str(linha[3]))
    prog.ed_valor.setText(str(linha[4]))
    prog.ed_periodo.setText(str(linha[5]))
    prog.ed_circulacao.setText(str(linha[6]))
    prog.ed_assunto.setText(str(linha[7]))
    prog.ed_serie.setText(str(linha[8]))
    prog.ed_soberano.setText(str(linha[9]))
    prog.ed_cunhagem.setText(str(linha[10]))
    prog.ed_composicao.setText(str(linha[11]))
    prog.ed_borda.setText(str(linha[12]))
    prog.ed_formato.setText(str(linha[13]))
    prog.ed_alinhamento.setText(str(linha[14]))
    prog.ed_peso.setText(str(linha[15]))
    prog.ed_conservacao.setText(str(linha[16]))
    prog.ed_diametro.setText(str(linha[17]))
    prog.ed_espessura.setText(str(linha[18]))
    prog.ed_anverso.setText(str(linha[19]))
    prog.ed_reverso.setText(str(linha[20]))
    prog.ed_foto1.setText(str(linha[23]))
    prog.ed_foto2.setText(str(linha[24]))
    prog.ed_venda.setText(str(linha[21]))
    prog.lbl_data.setText(str(linha[22]))
    prog.ed_tipo.setText(str(linha[25]))
    # pais = linha[1]
    # ano = linha[2]
    # krause = linha[3]
    # valor = linha[4]
    # periodo = linha[5]
    # circulacao = linha[6]
    # assunto = linha[7]
    # serie = linha[8]
    # soberano = linha[9]
    # cunhagem = linha[10]
    # composicao = linha[11]
    # borda = linha[12]
    # formato = linha[13]
    # alinhamento = linha[14]
    # peso = linha[15]
    # conservacao = linha[16]
    # diametro = linha[17]
    # espessura = linha[18]
    # anverso = linha[19]
    # reverso = linha[20]
    # venda = linha[21]
    # cadastro = linha[22]
    # foto1 = linha[23]
    # foto2 = linha[24]
    prog.bt_deletar_reg.setVisible(True)
    prog.bt_mostrar_foto.setVisible(False)
    prog.bt_cadastrar.setText('Atualizar')
    exibeafoto()


def exibe_frame_de_pesquisa(tipo):
    limpa_form_cadastro()
    exibelista()
    prog.list_item.clear()
    prog.ed_localizar.setFocus()

    # tela de pesquisa por palavra
    if tipo == 'pesquisa':
        termo = prog.ed_localizar.text()
        print(termo)
        if not termo == '':
            prog.list_item.clear()
            itens = colecao.buscar(termo)
            prog.lbl_titulo_2.setText(
                'Resultado da pesquisa por: ' + termo.upper())

    # tela de pesquisa por moeda nacional
    elif tipo == 'Moeda Nacional':
        itens = colecao.buscar_tipos(tipo)
        prog.lbl_titulo_2.setText(str(tipo))
    # tela de pesquisa por nota nacional
    elif tipo == 'Nota Nacional':
        itens = colecao.buscar_tipos(tipo)
        prog.lbl_titulo_2.setText(str(tipo))
    # tela de pesquisa por moeda estrangeira
    elif tipo == 'Moeda Internacional':
        itens = colecao.buscar_tipos(tipo)
        prog.lbl_titulo_2.setText(str(tipo))
    # tela de pesquisa por nota estrangeira
    elif tipo == 'Nota Internacional':
        itens = colecao.buscar_tipos(tipo)
        prog.lbl_titulo_2.setText(str(tipo))
    # tela de pesquisa da colecao completa
    elif tipo == 'Colecao Completa':
        itens = colecao.buscar_tipos(tipo)
        prog.lbl_titulo_2.setText(str(tipo))
    # tela de resumo por pais
    elif tipo == 'Resumo Por Pais':
        itens = colecao.exibir_resumo_paises()
        prog.lbl_titulo_2.setText(str(tipo))
    # tela de ultimos cadastrados
    elif tipo == 'Ultimos Adicionados':
        itens = colecao.buscar_tipos(tipo)
        prog.lbl_titulo_2.setText(str(tipo))

    # preenche a tela com os dados da pesquisa
    try:

        for item in itens:
            prog.list_item.addItem(item)
        if prog.list_item.count() == 0:
            prog.list_item.clear()
            prog.list_item.addItem('Nenhum item encontrado')
            prog.lbl_status.setText('')
        else:
            prog.lbl_status.setText(
                f'{prog.list_item.count()} itens encontrados')
    except Exception as e:
        print(e)
        prog.list_item.clear()
        prog.list_item.addItem('Nenhum item encontrado')
        prog.lbl_status.setText('')

    def abre_item_selecionado(item):
        '''duplo clique para abrir o item'''
        id = str(item.text()).split(':')[0].strip()
        prog.lbl_titulo.setText(f'Atualizar Registro: {id}')

        try:
            exibe_moeda(id, 'atualizar')

        except Exception as e:
            print(e)
            exibelista()
            prog.ed_localizar.setText(id)

            prog.bt_localizar.animateClick(10)

    prog.list_item.itemDoubleClicked.connect(
        abre_item_selecionado)


def exibe_frame_de_cadastro(tipo):
    '''Exibe o frame de cadastro'''
    prog.bt_deletar_reg.setVisible(False)
    limpa_form_cadastro()
    exibecadastro()
    prog.lbl_titulo.setText(f'Cadastrar nova {str(tipo).lower()}')
    prog.bt_cadastrar.setText('Cadastrar')
    prog.bt_mostrar_foto.setVisible(True)
    # prog.ed_tipo.setText(tipo)


def cancelar():
    exiberesumo()
    limpa_form_cadastro()


def confirma_apagar():
    pass


def apagar_registro():
    print('apagar')
    '''Apaga o registro selecionado'''
    ret = QMessageBox.question(
        prog, 'ATENÇÃO!!!', f"Tem certeza que deseja apagar o item:\n{prog.ed_ano.text()} {prog.ed_pais.text()} {prog.ed_valor.text()} ", QMessageBox.Yes | QMessageBox.Cancel)

    if ret == QMessageBox.Yes:
        colecao.remover(prog.lbl_id.text())
        QMessageBox.about(
            prog, 'Apagado', 'Registro apagado com sucesso')
        limpa_form_cadastro()
        exiberesumo()


def carregaimagemFundo():
    pixmap = QPixmap('screenshot.png')
    scaled = pixmap.scaled(600, 400, QtCore.Qt.KeepAspectRatio)
    prog.mapa.setPixmap(scaled)
    prog.mapa.setVisible(True)


def scrap_img():
    QMessageBox.about(
        prog, 'Vai demorar....', 'Este processo pode demorar um pouco :/')
    colecao.scrap()
    carregaimagemFundo()
    # colecao.deletemapa(caminho='minha-colecao-a01d5.appspot.com',
    #                    arquivo='screenshot.png')
    colecao.upload(caminho='minha-colecao-a01d5.appspot.com',
                   arquivo='screenshot.png')


def exportar_banco_sql():
    qtde = colecao.exportarTXT()
    QMessageBox.about(
        prog, 'Backup', f'O arquivo TXT com o backup foi gerado com sucesso\n{qtde} registros exportados')


def importar_banco_sql(tipo):
    with open(f'bancoMoedas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        contador = 0
        for linha in linhas:
            contador += 1

    if tipo == 'parcial':
        ret = QMessageBox.question(
            prog, 'MUITA ATENÇÃO!!!', f"Tem certeza que deseja importar o arquivo TXT?\n{contador} registros encontrados", QMessageBox.Yes | QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            colecao.criartabela()
            qtde = colecao.importarTXT(tipo=tipo)
            QMessageBox.about(
                prog, 'Importação', f'O arquivo TXT com o backup foi importado com sucesso\n{qtde} registros foram importados')
    elif tipo == 'total':
        ret = QMessageBox.question(
            prog, 'MUITA ATENÇÃO!!!', f"Tem certeza que deseja apagar TODO o banco e importar o arquivo TXT?\n{contador} registros encontrados", QMessageBox.Yes | QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
            qtde = colecao.importarTXT(tipo=tipo)
            QMessageBox.about(
                prog, 'Importação', f'Registros importados com sucesso!\n{qtde} registros foram importados')


# menus
# menu de cadastro de moedas
prog.adicionaMoeda.triggered.connect(
    partial(exibe_frame_de_cadastro, tipo='Moeda'))
# menu de cadastro de notas
prog.adicionaNota.triggered.connect(
    partial(exibe_frame_de_cadastro, tipo='Nota'))
# menu de pesquisa por palavra
prog.pesquisar.triggered.connect(
    partial(exibe_frame_de_pesquisa, tipo='pesquisa'))
# menu que exibe a colecao completa
prog.ColecaoCompleta.triggered.connect(
    partial(exibe_frame_de_pesquisa, tipo='Colecao Completa'))
# menu moedas internacionais
prog.MoedasInternacional.triggered.connect(
    partial(exibe_frame_de_pesquisa, tipo='Moeda Internacional'))
# menu notas internacionais
prog.NotasInternacional.triggered.connect(
    partial(exibe_frame_de_pesquisa, tipo='Nota Internacional'))
# menu moedas nacionais
prog.MoedasNacional.triggered.connect(
    partial(exibe_frame_de_pesquisa, tipo='Moeda Nacional'))
# menu notas nacionais
prog.NotasNacional.triggered.connect(
    partial(exibe_frame_de_pesquisa, tipo='Nota Nacional'))
# menu resumo por pais
prog.listar_por_pais.triggered.connect(
    partial(exibe_frame_de_pesquisa, tipo='Resumo Por Pais'))
# menu atualiza imagem do mapa
prog.Atualizar_Imagem.triggered.connect(partial(scrap_img))
# menu de exportacao do banco sql
prog.Exportar_TXT.triggered.connect(exportar_banco_sql)
# menu de importacao do banco sql parcial
prog.sqlParcial.triggered.connect(partial(importar_banco_sql, tipo='parcial'))
# menu de importacao do banco sql total
prog.sqlTotal.triggered.connect(partial(importar_banco_sql, tipo='total'))
# menu ultimos registros
prog.ultimos_adicionados.triggered.connect(
    partial(exibe_frame_de_pesquisa, tipo='Ultimos Adicionados'))

# botoes
# botão cadastrar
prog.bt_cadastrar.clicked.connect(fcadastrar)
# botão pesquisar
prog.bt_localizar.clicked.connect(
    partial(exibe_frame_de_pesquisa, tipo='pesquisa'))
# botao mostrar fotos no frame de cadastro
prog.bt_mostrar_foto.clicked.connect(exibeafoto)
# botao cancelar cadastro
prog.bt_cancelar.clicked.connect(cancelar)
# botao apagar registro
prog.bt_deletar_reg.clicked.connect(apagar_registro)

exiberesumo()

prog.show()
app.exec()

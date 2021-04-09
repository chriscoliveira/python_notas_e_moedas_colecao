import sys
import time

from lib import *
import pandas as pd
'''
executar o comando para criar o .py com o design do QTDESIGN
pyuic5 -o design.py MainWindow.ui 
'''

from PyQt5.QtWidgets import QMainWindow, QApplication

# importa a classe do arquivo design.py
from design import Ui_ColecaoMoedas


# from classes import Funcoes


class MainUi(QMainWindow, Ui_ColecaoMoedas):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        """
        MOEDAS verifica se existe o csv baixado da ucoin
        """
        self.u_lista_total = abrecsv_ucoin()
        self.u_lista_unica = lista_unica(self.u_lista_total)

        '''
        MOEDAS verifica se existe o csv do firebase do google, senao faz o download
        '''
        self.a_lista_total = abrecsv_google_moedas()
        self.a_lista_unica = lista_unica(self.a_lista_total)

        '''
        NOTAS verifica se existe o csv do firebase do google, senao faz o download
        '''
        self.n_lista_total = abrecsv_google_notas()
        self.n_lista_unica = lista_unica(self.n_lista_total)

        # atribui a função ao botao
        self.btn_moeda_ucoin.clicked.connect(self.total_ucoin)
        self.btn_moeda_celular.clicked.connect(self.total_celular)
        self.btn_ucoin_celular.clicked.connect(self.divergencias)
        self.btn_totais_notas.clicked.connect(self.totais_notas)
        self.btn_pesquisar.clicked.connect(self.pesquisa)
        self.btn_update.clicked.connect(self.update_base)

    def update_base(self):
        baixar_CSV_android()
        self.resposta.setText('Dados Atualizados')

    def total_ucoin(self):
        exibe_totais(self.u_lista_unica, self.u_lista_total, 'TOTAL_MOEDA_UCOIN')
        inf = open('TOTAL_MOEDA_UCOIN.txt')
        self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def total_celular(self):
        exibe_totais(self.a_lista_unica, self.a_lista_total, 'TOTAL_MOEDA_ANDROID_APP')
        inf = open('TOTAL_MOEDA_ANDROID_APP.txt')
        self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def divergencias(self):
        exibe_divergencias(self.a_lista_unica, self.a_lista_total, self.u_lista_unica, self.u_lista_total)
        inf = open('DIVERGENCIAS.txt')
        self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def totais_notas(self):
        exibe_totais(self.n_lista_unica, self.n_lista_total, 'TOTAL_NOTAS_ANDROID_APP')
        inf = open('TOTAL_NOTAS_ANDROID_APP.txt')
        self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def pesquisa(self):
        tipo = None
        if self.cb_nota.isChecked():
            tipo = 'bancoNotas.csv'
        if self.cb_moeda.isChecked():
            tipo = 'bancoMoedas.csv'
        termo = self.lineEdit.text()
        if tipo:
            pesquisar(tipo, termo)
        inf = open('resultado.txt')
        self.resposta.setText(str(inf.read()))
        time.sleep(2)


if __name__ == '__main__':
    qt = QApplication(sys.argv)

    # exibe_totais()
    mainui = MainUi()
    mainui.show()
    qt.exec_()

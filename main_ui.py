import sys
import time

'''
executar o comando para criar o .py com o design do QTDESIGN
pyuic5 -o design.py MainWindow.ui 
'''
from lib import *
from pandasmodel import PandasModel
from PyQt5.QtWidgets import QMainWindow, QApplication
from design import Ui_ColecaoMoedas


class MainUi(QMainWindow, Ui_ColecaoMoedas):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.u_lista_total = abrecsv_ucoin()
        self.u_lista_unica = lista_unica(self.u_lista_total)
        self.a_lista_total = abrecsv_google_moedas()
        self.a_lista_unica = lista_unica(self.a_lista_total)
        self.n_lista_total = abrecsv_google_notas()
        self.n_lista_unica = lista_unica(self.n_lista_total)

        # atribui a função ao botao
        self.btn_moeda_ucoin.clicked.connect(self.total_ucoin)
        self.btn_moeda_celular.clicked.connect(self.total_celular)
        self.btn_ucoin_celular.clicked.connect(self.divergencias)
        self.btn_totais_notas.clicked.connect(self.totais_notas)
        self.btn_pesquisar.clicked.connect(self.pesquisa)
        self.btn_update.clicked.connect(self.update_base)
        self.btn_nota.clicked.connect(self.total_nota)
        self.btn_moeda.clicked.connect(self.total_moeda)

    def loadFile(self, arquivo):
        # fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)");
        fileName = arquivo
        # self.pathLE.setText(fileName)
        df = pd.read_csv(fileName)
        model = PandasModel(df)
        self.tabela.setModel(model)

    def update_base(self):
        baixar_CSV_android()
        self.resposta.setText('Dados Atualizados')

    def total_ucoin(self):
        exibe_totais(self.u_lista_unica, self.u_lista_total, 'TOTAL_MOEDA_UCOIN')
        inf = open('TOTAL_MOEDA_UCOIN.txt')
        self.loadFile('_TOTAL_MOEDA_UCOIN.txt')
        # self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def total_celular(self):
        exibe_totais(self.a_lista_unica, self.a_lista_total, 'TOTAL_MOEDA_ANDROID_APP')
        inf = open('TOTAL_MOEDA_ANDROID_APP.txt')
        self.loadFile('_TOTAL_MOEDA_ANDROID_APP.txt')
        # self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def divergencias(self):
        exibe_divergencias(self.a_lista_unica, self.a_lista_total, self.u_lista_unica, self.u_lista_total)
        inf = open('DIVERGENCIAS.txt')
        self.loadFile('_DIVERGENCIAS.txt')
        # self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def totais_notas(self):
        exibe_totais(self.n_lista_unica, self.n_lista_total, 'TOTAL_NOTAS_ANDROID_APP')
        inf = open('TOTAL_NOTAS_ANDROID_APP.txt')
        self.loadFile('_TOTAL_NOTAS_ANDROID_APP.txt')
        # self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def total_nota(self):
        total('bancoNotas.csv')
        inf = open('resultado.txt')
        self.loadFile('_resultado.txt')
        # self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def total_moeda(self):
        total('bancoMoedas.csv')
        inf = open('resultado.txt')
        self.loadFile('_resultado.txt')
        # self.resposta.setText(str(inf.read()))
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
        # self.resposta.setText(str(inf.read()))
        self.loadFile('_resultado.txt')
        time.sleep(2)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('max_colwidth', 100)
    pd.set_option('display.width', None)
    # exibe_totais()
    mainui = MainUi()
    mainui.show()
    qt.exec_()

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

arquivo_txt = 'RESULTADO'

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
        self.btn_moeda_ucoin.clicked.connect(self.total_moeda)
        # self.btn_moeda_celular.clicked.connect(self.total_celular)
        self.btn_ucoin_celular.clicked.connect(self.divergencias)
        self.btn_totais_notas.clicked.connect(self.total_nota)
        self.btn_pesquisar.clicked.connect(self.pesquisa)
        self.btn_update.clicked.connect(self.update_base)
        self.btn_nota.clicked.connect(self.total_nota)
        self.btn_moeda.clicked.connect(self.total_moeda)

    def loadFile(self, arquivo):
        # fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "CSV Files (*.csv)");
        try:
            fileName = arquivo
            # self.pathLE.setText(fileName)
            df = pd.read_csv(fileName)
            model = PandasModel(df)
            self.tabela.setModel(model)
        except:
            pass

    def update_base(self):
        baixar_CSV_android()
        self.resposta.setText('Dados Atualizados')

    def qtd_total_moedas(self):
        quantidade_moedas(self.u_lista_unica, self.a_lista_unica, self.u_lista_total, self.a_lista_total, arquivo_txt)
        inf = open(arquivo_txt+'.txt')
        self.lbl_tipo.setText('Quantidade de Moedas pais por pais')
        self.loadFile('_'+arquivo_txt+'.txt')
        # self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def divergencias(self):
        exibe_divergencias(self.a_lista_unica, self.a_lista_total, self.u_lista_unica, self.u_lista_total)
        inf = open(arquivo_txt+'.txt')
        self.lbl_tipo.setText('Divergencia de Moedas pais por pais')
        self.loadFile('_'+arquivo_txt+'.txt')
        # self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def qtd_total_notas(self):
        quantidade_notas(self.n_lista_unica, self.n_lista_total, arquivo_txt)
        inf = open(arquivo_txt+'.txt')
        self.lbl_tipo.setText('Quantida de Notas pais por pais')
        self.loadFile('_'+arquivo_txt+'.txt')
        # self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def total_nota(self):
        total('bancoNotas.csv')
        inf = open(arquivo_txt+'.txt')
        self.lbl_tipo.setText('Notas da Coleção')
        self.loadFile('_'+arquivo_txt+'.txt')
        # self.resposta.setText(str(inf.read()))
        time.sleep(2)

    def total_moeda(self):
        total('bancoMoedas.csv')
        inf = open(arquivo_txt+'.txt')
        self.lbl_tipo.setText('Moedas da Coleção')
        self.loadFile('_'+arquivo_txt+'.txt')
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
            try:
                pesquisar(tipo, termo)
            except:
                pass

        inf = open(arquivo_txt+'.txt')
        # self.resposta.setText(str(inf.read()))
        self.lbl_tipo.setText('Resultado da pesquisa por: '+termo+' em: '+tipo)

        self.loadFile('_'+arquivo_txt+'.txt')

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

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColecaoMoedas(object):
    def setupUi(self, ColecaoMoedas):
        ColecaoMoedas.setObjectName("ColecaoMoedas")
        ColecaoMoedas.resize(1035, 600)
        self.centralwidget = QtWidgets.QWidget(ColecaoMoedas)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_moeda_ucoin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_moeda_ucoin.setObjectName("btn_moeda_ucoin")
        self.gridLayout.addWidget(self.btn_moeda_ucoin, 0, 0, 1, 1)
        self.btn_moeda_celular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_moeda_celular.setObjectName("btn_moeda_celular")
        self.gridLayout.addWidget(self.btn_moeda_celular, 0, 1, 1, 1)
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setObjectName("btn_update")
        self.gridLayout.addWidget(self.btn_update, 0, 4, 1, 1)
        self.btn_totais_notas = QtWidgets.QPushButton(self.centralwidget)
        self.btn_totais_notas.setObjectName("btn_totais_notas")
        self.gridLayout.addWidget(self.btn_totais_notas, 0, 3, 1, 1)
        self.btn_ucoin_celular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ucoin_celular.setObjectName("btn_ucoin_celular")
        self.gridLayout.addWidget(self.btn_ucoin_celular, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.cb_nota = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_nota.setObjectName("cb_nota")
        self.horizontalLayout_2.addWidget(self.cb_nota)
        self.cb_moeda = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_moeda.setObjectName("cb_moeda")
        self.horizontalLayout_2.addWidget(self.cb_moeda)
        self.btn_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pesquisar.setObjectName("btn_pesquisar")
        self.horizontalLayout_2.addWidget(self.btn_pesquisar)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 5, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1015, 520))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.resposta = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.resposta.setText("")
        self.resposta.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resposta.setObjectName("resposta")
        self.gridLayout_2.addWidget(self.resposta, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 1, 1)
        ColecaoMoedas.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ColecaoMoedas)
        self.statusbar.setObjectName("statusbar")
        ColecaoMoedas.setStatusBar(self.statusbar)

        self.retranslateUi(ColecaoMoedas)
        QtCore.QMetaObject.connectSlotsByName(ColecaoMoedas)

    def retranslateUi(self, ColecaoMoedas):
        _translate = QtCore.QCoreApplication.translate
        ColecaoMoedas.setWindowTitle(_translate("ColecaoMoedas", "Coleção de Moedas e Notas"))
        self.btn_moeda_ucoin.setText(_translate("ColecaoMoedas", "Moedas Ucoin"))
        self.btn_moeda_celular.setText(_translate("ColecaoMoedas", "Moedas Celular"))
        self.btn_update.setText(_translate("ColecaoMoedas", "Atualizar base"))
        self.btn_totais_notas.setText(_translate("ColecaoMoedas", "Notas"))
        self.btn_ucoin_celular.setText(_translate("ColecaoMoedas", "Div. Ucoin x Celular"))
        self.cb_nota.setText(_translate("ColecaoMoedas", "Nota"))
        self.cb_moeda.setText(_translate("ColecaoMoedas", "Moeda"))
        self.btn_pesquisar.setText(_translate("ColecaoMoedas", "Pesquisar"))

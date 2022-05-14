# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'z:\Christian\Python\GitHub\python_notas_e_moedas_colecao\layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 866)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 900))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 122, 204);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_resumo = QtWidgets.QFrame(self.centralwidget)
        self.frame_resumo.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_resumo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_resumo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_resumo.setObjectName("frame_resumo")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_resumo)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mapa = QtWidgets.QLabel(self.frame_resumo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mapa.sizePolicy().hasHeightForWidth())
        self.mapa.setSizePolicy(sizePolicy)
        self.mapa.setText("")
        self.mapa.setScaledContents(False)
        self.mapa.setAlignment(QtCore.Qt.AlignCenter)
        self.mapa.setObjectName("mapa")
        self.verticalLayout_3.addWidget(self.mapa)
        self.resumo = QtWidgets.QLabel(self.frame_resumo)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.resumo.setFont(font)
        self.resumo.setText("")
        self.resumo.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.resumo.setObjectName("resumo")
        self.verticalLayout_3.addWidget(self.resumo)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_resumo)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.frame_cadastro = QtWidgets.QFrame(self.centralwidget)
        self.frame_cadastro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_cadastro.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_cadastro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cadastro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cadastro.setObjectName("frame_cadastro")
        self.formLayout = QtWidgets.QFormLayout(self.frame_cadastro)
        self.formLayout.setObjectName("formLayout")
        self.lbl_titulo = QtWidgets.QLabel(self.frame_cadastro)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.lbl_titulo)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_20 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 10, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.ed_composicao = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_composicao.setObjectName("ed_composicao")
        self.gridLayout.addWidget(self.ed_composicao, 5, 1, 1, 1)
        self.ed_periodo = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_periodo.setObjectName("ed_periodo")
        self.gridLayout.addWidget(self.ed_periodo, 2, 1, 1, 1)
        self.ed_conservacao = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_conservacao.setObjectName("ed_conservacao")
        self.gridLayout.addWidget(self.ed_conservacao, 8, 3, 1, 1)
        self.ed_pais = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_pais.setObjectName("ed_pais")
        self.gridLayout.addWidget(self.ed_pais, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 10, 2, 1, 1)
        self.ed_ano = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_ano.setObjectName("ed_ano")
        self.gridLayout.addWidget(self.ed_ano, 0, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 8, 0, 1, 1)
        self.ed_valor = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_valor.setObjectName("ed_valor")
        self.gridLayout.addWidget(self.ed_valor, 1, 3, 1, 1)
        self.lbl_id = QtWidgets.QLabel(self.frame_cadastro)
        self.lbl_id.setMaximumSize(QtCore.QSize(1, 16777215))
        self.lbl_id.setText("")
        self.lbl_id.setObjectName("lbl_id")
        self.gridLayout.addWidget(self.lbl_id, 12, 2, 1, 1)
        self.lbl_data = QtWidgets.QLabel(self.frame_cadastro)
        self.lbl_data.setText("")
        self.lbl_data.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_data.setObjectName("lbl_data")
        self.gridLayout.addWidget(self.lbl_data, 11, 2, 1, 2)
        self.ed_espessura = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_espessura.setObjectName("ed_espessura")
        self.gridLayout.addWidget(self.ed_espessura, 9, 3, 1, 1)
        self.ed_borda = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_borda.setObjectName("ed_borda")
        self.gridLayout.addWidget(self.ed_borda, 6, 3, 1, 1)
        self.ed_assunto = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_assunto.setObjectName("ed_assunto")
        self.gridLayout.addWidget(self.ed_assunto, 3, 1, 1, 1)
        self.bt_mostrar_foto = QtWidgets.QPushButton(self.frame_cadastro)
        self.bt_mostrar_foto.setObjectName("bt_mostrar_foto")
        self.gridLayout.addWidget(self.bt_mostrar_foto, 12, 0, 1, 1)
        self.foto_anverso = QtWidgets.QLabel(self.frame_cadastro)
        self.foto_anverso.setText("")
        self.foto_anverso.setAlignment(QtCore.Qt.AlignCenter)
        self.foto_anverso.setObjectName("foto_anverso")
        self.gridLayout.addWidget(self.foto_anverso, 12, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 13, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.ed_tipo = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_tipo.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"color: rgb(170, 23, 25);")
        self.ed_tipo.setObjectName("ed_tipo")
        self.gridLayout.addWidget(self.ed_tipo, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.ed_diametro = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_diametro.setObjectName("ed_diametro")
        self.gridLayout.addWidget(self.ed_diametro, 8, 1, 1, 1)
        self.ed_anverso = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_anverso.setObjectName("ed_anverso")
        self.gridLayout.addWidget(self.ed_anverso, 9, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 9, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 7, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_cadastrar = QtWidgets.QPushButton(self.frame_cadastro)
        self.bt_cadastrar.setObjectName("bt_cadastrar")
        self.horizontalLayout.addWidget(self.bt_cadastrar)
        self.bt_deletar_reg = QtWidgets.QPushButton(self.frame_cadastro)
        self.bt_deletar_reg.setObjectName("bt_deletar_reg")
        self.horizontalLayout.addWidget(self.bt_deletar_reg)
        self.bt_cancelar = QtWidgets.QPushButton(self.frame_cadastro)
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.horizontalLayout.addWidget(self.bt_cancelar)
        self.bt_scrap = QtWidgets.QPushButton(self.frame_cadastro)
        self.bt_scrap.setObjectName("bt_scrap")
        self.horizontalLayout.addWidget(self.bt_scrap)
        self.gridLayout.addLayout(self.horizontalLayout, 15, 0, 1, 5)
        self.ed_circulacao = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_circulacao.setObjectName("ed_circulacao")
        self.gridLayout.addWidget(self.ed_circulacao, 3, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 7, 2, 1, 1)
        self.ed_formato = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_formato.setObjectName("ed_formato")
        self.gridLayout.addWidget(self.ed_formato, 6, 1, 1, 1)
        self.ed_reverso = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_reverso.setObjectName("ed_reverso")
        self.gridLayout.addWidget(self.ed_reverso, 10, 3, 1, 1)
        self.lbl_status_cadastro = QtWidgets.QLabel(self.frame_cadastro)
        self.lbl_status_cadastro.setText("")
        self.lbl_status_cadastro.setObjectName("lbl_status_cadastro")
        self.gridLayout.addWidget(self.lbl_status_cadastro, 16, 0, 1, 5)
        self.ed_serie = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_serie.setObjectName("ed_serie")
        self.gridLayout.addWidget(self.ed_serie, 4, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 11, 0, 1, 2)
        self.ed_cunhagem = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_cunhagem.setObjectName("ed_cunhagem")
        self.gridLayout.addWidget(self.ed_cunhagem, 5, 3, 1, 1)
        self.ed_venda = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_venda.setObjectName("ed_venda")
        self.gridLayout.addWidget(self.ed_venda, 10, 1, 1, 1)
        self.conservacao = QtWidgets.QLabel(self.frame_cadastro)
        self.conservacao.setObjectName("conservacao")
        self.gridLayout.addWidget(self.conservacao, 8, 2, 1, 1)
        self.foto_reverso = QtWidgets.QLabel(self.frame_cadastro)
        self.foto_reverso.setText("")
        self.foto_reverso.setAlignment(QtCore.Qt.AlignCenter)
        self.foto_reverso.setObjectName("foto_reverso")
        self.gridLayout.addWidget(self.foto_reverso, 12, 3, 1, 1)
        self.ed_foto1 = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_foto1.setObjectName("ed_foto1")
        self.gridLayout.addWidget(self.ed_foto1, 13, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 13, 0, 1, 1)
        self.ed_foto2 = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_foto2.setObjectName("ed_foto2")
        self.gridLayout.addWidget(self.ed_foto2, 13, 3, 1, 1)
        self.ed_alinhamento = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_alinhamento.setObjectName("ed_alinhamento")
        self.gridLayout.addWidget(self.ed_alinhamento, 7, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)
        self.ed_soberano = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_soberano.setObjectName("ed_soberano")
        self.gridLayout.addWidget(self.ed_soberano, 4, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 2, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 2, 1, 1)
        self.ed_peso = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_peso.setObjectName("ed_peso")
        self.gridLayout.addWidget(self.ed_peso, 7, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 9, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.ed_krause = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_krause.setObjectName("ed_krause")
        self.gridLayout.addWidget(self.ed_krause, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame_cadastro)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 0, 1, 1)
        self.label_ucoin = QtWidgets.QLabel(self.frame_cadastro)
        self.label_ucoin.setObjectName("label_ucoin")
        self.gridLayout.addWidget(self.label_ucoin, 14, 0, 1, 1)
        self.ed_link_ucoin = QtWidgets.QLineEdit(self.frame_cadastro)
        self.ed_link_ucoin.setObjectName("ed_link_ucoin")
        self.gridLayout.addWidget(self.ed_link_ucoin, 14, 1, 1, 2)
        self.bt_buscar_ucoin = QtWidgets.QPushButton(self.frame_cadastro)
        self.bt_buscar_ucoin.setObjectName("bt_buscar_ucoin")
        self.gridLayout.addWidget(self.bt_buscar_ucoin, 14, 3, 1, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.gridLayout)
        self.gridLayout_2.addWidget(self.frame_cadastro, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.frame_listar = QtWidgets.QFrame(self.centralwidget)
        self.frame_listar.setEnabled(True)
        self.frame_listar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_listar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_listar.setAutoFillBackground(False)
        self.frame_listar.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.frame_listar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_listar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_listar.setObjectName("frame_listar")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_listar)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl_status = QtWidgets.QLabel(self.frame_listar)
        self.lbl_status.setText("")
        self.lbl_status.setObjectName("lbl_status")
        self.gridLayout_3.addWidget(self.lbl_status, 3, 0, 1, 1)
        self.list_item = QtWidgets.QListWidget(self.frame_listar)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.list_item.setFont(font)
        self.list_item.setObjectName("list_item")
        self.gridLayout_3.addWidget(self.list_item, 2, 0, 1, 3)
        self.lbl_titulo_2 = QtWidgets.QLabel(self.frame_listar)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_titulo_2.setFont(font)
        self.lbl_titulo_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_titulo_2.setObjectName("lbl_titulo_2")
        self.gridLayout_3.addWidget(self.lbl_titulo_2, 0, 0, 1, 3)
        self.ed_localizar = QtWidgets.QLineEdit(self.frame_listar)
        self.ed_localizar.setObjectName("ed_localizar")
        self.gridLayout_3.addWidget(self.ed_localizar, 1, 1, 1, 1)
        self.bt_localizar = QtWidgets.QPushButton(self.frame_listar)
        self.bt_localizar.setObjectName("bt_localizar")
        self.gridLayout_3.addWidget(self.bt_localizar, 1, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_listar)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_listar, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastrar = QtWidgets.QMenu(self.menubar)
        self.menuCadastrar.setObjectName("menuCadastrar")
        self.menuNacional = QtWidgets.QMenu(self.menuCadastrar)
        self.menuNacional.setObjectName("menuNacional")
        self.menuEstrangeiro = QtWidgets.QMenu(self.menuCadastrar)
        self.menuEstrangeiro.setObjectName("menuEstrangeiro")
        self.menuCadastrar_Novo = QtWidgets.QMenu(self.menubar)
        self.menuCadastrar_Novo.setObjectName("menuCadastrar_Novo")
        self.menuConfigura_o = QtWidgets.QMenu(self.menubar)
        self.menuConfigura_o.setObjectName("menuConfigura_o")
        self.menuImportar = QtWidgets.QMenu(self.menuConfigura_o)
        self.menuImportar.setEnabled(False)
        self.menuImportar.setObjectName("menuImportar")
        self.menuResumo = QtWidgets.QMenu(self.menubar)
        self.menuResumo.setObjectName("menuResumo")
        MainWindow.setMenuBar(self.menubar)
        self.NotasNacional = QtWidgets.QAction(MainWindow)
        self.NotasNacional.setObjectName("NotasNacional")
        self.MoedasNacional = QtWidgets.QAction(MainWindow)
        self.MoedasNacional.setObjectName("MoedasNacional")
        self.NotasInternacional = QtWidgets.QAction(MainWindow)
        self.NotasInternacional.setObjectName("NotasInternacional")
        self.MoedasInternacional = QtWidgets.QAction(MainWindow)
        self.MoedasInternacional.setObjectName("MoedasInternacional")
        self.ColecaoCompleta = QtWidgets.QAction(MainWindow)
        self.ColecaoCompleta.setObjectName("ColecaoCompleta")
        self.listar_por_pais = QtWidgets.QAction(MainWindow)
        self.listar_por_pais.setObjectName("listar_por_pais")
        self.pesquisar = QtWidgets.QAction(MainWindow)
        self.pesquisar.setObjectName("pesquisar")
        self.adicionaNota = QtWidgets.QAction(MainWindow)
        self.adicionaNota.setObjectName("adicionaNota")
        self.adicionaMoeda = QtWidgets.QAction(MainWindow)
        self.adicionaMoeda.setObjectName("adicionaMoeda")
        self.Exportar_TXT = QtWidgets.QAction(MainWindow)
        self.Exportar_TXT.setObjectName("Exportar_TXT")
        self.sqlParcial = QtWidgets.QAction(MainWindow)
        self.sqlParcial.setObjectName("sqlParcial")
        self.sqlTotal = QtWidgets.QAction(MainWindow)
        self.sqlTotal.setObjectName("sqlTotal")
        self.ultimos_adicionados = QtWidgets.QAction(MainWindow)
        self.ultimos_adicionados.setObjectName("ultimos_adicionados")
        self.Atualizar_Imagem = QtWidgets.QAction(MainWindow)
        self.Atualizar_Imagem.setObjectName("Atualizar_Imagem")
        self.actionResumo = QtWidgets.QAction(MainWindow)
        self.actionResumo.setObjectName("actionResumo")
        self.menuNacional.addAction(self.NotasNacional)
        self.menuNacional.addAction(self.MoedasNacional)
        self.menuEstrangeiro.addAction(self.NotasInternacional)
        self.menuEstrangeiro.addAction(self.MoedasInternacional)
        self.menuCadastrar.addAction(self.pesquisar)
        self.menuCadastrar.addSeparator()
        self.menuCadastrar.addAction(self.menuNacional.menuAction())
        self.menuCadastrar.addAction(self.menuEstrangeiro.menuAction())
        self.menuCadastrar.addSeparator()
        self.menuCadastrar.addAction(self.ColecaoCompleta)
        self.menuCadastrar.addSeparator()
        self.menuCadastrar.addAction(self.listar_por_pais)
        self.menuCadastrar.addAction(self.ultimos_adicionados)
        self.menuCadastrar_Novo.addAction(self.adicionaNota)
        self.menuCadastrar_Novo.addAction(self.adicionaMoeda)
        self.menuImportar.addAction(self.sqlParcial)
        self.menuImportar.addAction(self.sqlTotal)
        self.menuConfigura_o.addAction(self.Exportar_TXT)
        self.menuConfigura_o.addAction(self.menuImportar.menuAction())
        self.menuConfigura_o.addAction(self.Atualizar_Imagem)
        self.menuResumo.addAction(self.actionResumo)
        self.menubar.addAction(self.menuResumo.menuAction())
        self.menubar.addAction(self.menuCadastrar.menuAction())
        self.menubar.addAction(self.menuCadastrar_Novo.menuAction())
        self.menubar.addAction(self.menuConfigura_o.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.ed_pais, self.ed_ano)
        MainWindow.setTabOrder(self.ed_ano, self.ed_krause)
        MainWindow.setTabOrder(self.ed_krause, self.ed_valor)
        MainWindow.setTabOrder(self.ed_valor, self.ed_periodo)
        MainWindow.setTabOrder(self.ed_periodo, self.ed_tipo)
        MainWindow.setTabOrder(self.ed_tipo, self.ed_assunto)
        MainWindow.setTabOrder(self.ed_assunto, self.ed_circulacao)
        MainWindow.setTabOrder(self.ed_circulacao, self.ed_soberano)
        MainWindow.setTabOrder(self.ed_soberano, self.ed_serie)
        MainWindow.setTabOrder(self.ed_serie, self.ed_composicao)
        MainWindow.setTabOrder(self.ed_composicao, self.ed_cunhagem)
        MainWindow.setTabOrder(self.ed_cunhagem, self.ed_formato)
        MainWindow.setTabOrder(self.ed_formato, self.ed_borda)
        MainWindow.setTabOrder(self.ed_borda, self.ed_peso)
        MainWindow.setTabOrder(self.ed_peso, self.ed_alinhamento)
        MainWindow.setTabOrder(self.ed_alinhamento, self.ed_diametro)
        MainWindow.setTabOrder(self.ed_diametro, self.ed_conservacao)
        MainWindow.setTabOrder(self.ed_conservacao, self.ed_anverso)
        MainWindow.setTabOrder(self.ed_anverso, self.ed_espessura)
        MainWindow.setTabOrder(self.ed_espessura, self.ed_venda)
        MainWindow.setTabOrder(self.ed_venda, self.ed_reverso)
        MainWindow.setTabOrder(self.ed_reverso, self.ed_foto1)
        MainWindow.setTabOrder(self.ed_foto1, self.ed_foto2)
        MainWindow.setTabOrder(self.ed_foto2, self.bt_cadastrar)
        MainWindow.setTabOrder(self.bt_cadastrar, self.bt_deletar_reg)
        MainWindow.setTabOrder(self.bt_deletar_reg, self.bt_cancelar)
        MainWindow.setTabOrder(self.bt_cancelar, self.bt_mostrar_foto)
        MainWindow.setTabOrder(self.bt_mostrar_foto, self.ed_localizar)
        MainWindow.setTabOrder(self.ed_localizar, self.bt_localizar)
        MainWindow.setTabOrder(self.bt_localizar, self.list_item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coleção de Moedas e Notas 2022"))
        self.lbl_titulo.setText(_translate("MainWindow", "Cadastrar Item"))
        self.label_20.setText(_translate("MainWindow", "Valor Venda R$"))
        self.label_9.setText(_translate("MainWindow", "Soberano"))
        self.label_25.setText(_translate("MainWindow", "Reverso"))
        self.label_18.setText(_translate("MainWindow", "Diametro"))
        self.bt_mostrar_foto.setText(_translate("MainWindow", "Mostrar Fotos"))
        self.label_15.setText(_translate("MainWindow", "Link foto2"))
        self.label_4.setText(_translate("MainWindow", "Periodo"))
        self.label_2.setText(_translate("MainWindow", "Ano"))
        self.label_11.setText(_translate("MainWindow", "Composicao"))
        self.label_24.setText(_translate("MainWindow", "Espessura"))
        self.label_17.setText(_translate("MainWindow", "Peso"))
        self.label_12.setText(_translate("MainWindow", "Borda"))
        self.label_6.setText(_translate("MainWindow", "Circulacao"))
        self.bt_cadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.bt_deletar_reg.setText(_translate("MainWindow", "Deletar Item"))
        self.bt_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.bt_cancelar.setShortcut(_translate("MainWindow", "Esc"))
        self.bt_scrap.setText(_translate("MainWindow", "Scrap Ucoin"))
        self.label_22.setText(_translate("MainWindow", "Alinhamento"))
        self.label_23.setText(_translate("MainWindow", "Cadastrado em:"))
        self.conservacao.setText(_translate("MainWindow", "Conservacao"))
        self.label_13.setText(_translate("MainWindow", "Formato"))
        self.label_14.setText(_translate("MainWindow", "Link foto1"))
        self.label_5.setText(_translate("MainWindow", "Valor"))
        self.label_21.setText(_translate("MainWindow", "Tipo"))
        self.label_10.setText(_translate("MainWindow", "Cunhagem"))
        self.label_19.setText(_translate("MainWindow", "Anverso"))
        self.label_27.setText(_translate("MainWindow", "País"))
        self.label_8.setText(_translate("MainWindow", "Serie"))
        self.label_7.setText(_translate("MainWindow", "Assunto"))
        self.label_26.setText(_translate("MainWindow", "Krause"))
        self.label_ucoin.setText(_translate("MainWindow", "Link Ucoin"))
        self.bt_buscar_ucoin.setText(_translate("MainWindow", "Buscar"))
        self.lbl_titulo_2.setText(_translate("MainWindow", "Pesquisar Item"))
        self.bt_localizar.setText(_translate("MainWindow", "Pesquisar"))
        self.label_16.setText(_translate("MainWindow", "Digite a palavra que deseja buscar"))
        self.menuCadastrar.setTitle(_translate("MainWindow", "Filtrar"))
        self.menuNacional.setTitle(_translate("MainWindow", "Nacional"))
        self.menuEstrangeiro.setTitle(_translate("MainWindow", "Internacional"))
        self.menuCadastrar_Novo.setTitle(_translate("MainWindow", "Cadastrar Novo"))
        self.menuConfigura_o.setTitle(_translate("MainWindow", "Configuração"))
        self.menuImportar.setTitle(_translate("MainWindow", "Importar"))
        self.menuResumo.setTitle(_translate("MainWindow", "Home"))
        self.NotasNacional.setText(_translate("MainWindow", "Notas"))
        self.NotasNacional.setShortcut(_translate("MainWindow", "F2"))
        self.MoedasNacional.setText(_translate("MainWindow", "Moedas"))
        self.MoedasNacional.setShortcut(_translate("MainWindow", "F3"))
        self.NotasInternacional.setText(_translate("MainWindow", "Notas"))
        self.NotasInternacional.setShortcut(_translate("MainWindow", "F4"))
        self.MoedasInternacional.setText(_translate("MainWindow", "Moedas"))
        self.MoedasInternacional.setShortcut(_translate("MainWindow", "F5"))
        self.ColecaoCompleta.setText(_translate("MainWindow", "Coleção Completa"))
        self.ColecaoCompleta.setShortcut(_translate("MainWindow", "F6"))
        self.listar_por_pais.setText(_translate("MainWindow", "Listar por país"))
        self.listar_por_pais.setShortcut(_translate("MainWindow", "F7"))
        self.pesquisar.setText(_translate("MainWindow", "Pesquisar"))
        self.pesquisar.setShortcut(_translate("MainWindow", "F1"))
        self.adicionaNota.setText(_translate("MainWindow", "Nota"))
        self.adicionaNota.setShortcut(_translate("MainWindow", "F8"))
        self.adicionaMoeda.setText(_translate("MainWindow", "Moeda"))
        self.adicionaMoeda.setShortcut(_translate("MainWindow", "F9"))
        self.Exportar_TXT.setText(_translate("MainWindow", "Exportar TXT"))
        self.sqlParcial.setText(_translate("MainWindow", "Parcial"))
        self.sqlTotal.setText(_translate("MainWindow", "Total"))
        self.ultimos_adicionados.setText(_translate("MainWindow", "Últimos Adicionados"))
        self.ultimos_adicionados.setShortcut(_translate("MainWindow", "F10"))
        self.Atualizar_Imagem.setText(_translate("MainWindow", "Atualizar Imagem"))
        self.actionResumo.setText(_translate("MainWindow", "Resumo"))

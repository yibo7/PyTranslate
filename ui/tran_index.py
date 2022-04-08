# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tran_index.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(862, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_folder_patch = QLineEdit(self.centralwidget)
        self.txt_folder_patch.setObjectName(u"txt_folder_patch")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_folder_patch.sizePolicy().hasHeightForWidth())
        self.txt_folder_patch.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.txt_folder_patch)

        self.btn_sel_folder = QPushButton(self.centralwidget)
        self.btn_sel_folder.setObjectName(u"btn_sel_folder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_sel_folder.sizePolicy().hasHeightForWidth())
        self.btn_sel_folder.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.btn_sel_folder)

        self.txtHz = QLineEdit(self.centralwidget)
        self.txtHz.setObjectName(u"txtHz")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txtHz.sizePolicy().hasHeightForWidth())
        self.txtHz.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.txtHz)

        self.btnSearchFiles = QPushButton(self.centralwidget)
        self.btnSearchFiles.setObjectName(u"btnSearchFiles")
        sizePolicy1.setHeightForWidth(self.btnSearchFiles.sizePolicy().hasHeightForWidth())
        self.btnSearchFiles.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.btnSearchFiles)

        self.cbIsFy = QCheckBox(self.centralwidget)
        self.cbIsFy.setObjectName(u"cbIsFy")
        self.cbIsFy.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.cbIsFy)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tb_datas = QTableWidget(self.centralwidget)
        self.tb_datas.setObjectName(u"tb_datas")
        self.tb_datas.setShowGrid(True)
        self.tb_datas.setSortingEnabled(False)
        self.tb_datas.setWordWrap(True)
        self.tb_datas.setRowCount(0)
        self.tb_datas.setColumnCount(0)

        self.verticalLayout_2.addWidget(self.tb_datas)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.widget.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_soure = QTextEdit(self.widget)
        self.txt_soure.setObjectName(u"txt_soure")
        self.txt_soure.setAcceptRichText(False)

        self.verticalLayout.addWidget(self.txt_soure)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_fy = QPushButton(self.widget)
        self.btn_fy.setObjectName(u"btn_fy")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_fy.sizePolicy().hasHeightForWidth())
        self.btn_fy.setSizePolicy(sizePolicy3)
        self.btn_fy.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.btn_fy)

        self.btn_save = QPushButton(self.widget)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.txt_rz = QTextEdit(self.widget)
        self.txt_rz.setObjectName(u"txt_rz")
        self.txt_rz.setAcceptRichText(False)

        self.verticalLayout.addWidget(self.txt_rz)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 862, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.btn_fy.clicked.connect(MainWindow.tran_en)
        self.btnSearchFiles.clicked.connect(MainWindow.seach_files)
        self.btn_sel_folder.clicked.connect(MainWindow.sel_folder)
        self.tb_datas.cellDoubleClicked.connect(MainWindow.openfile)
        self.btn_save.clicked.connect(MainWindow.save_file)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u7ffb\u8bd1\u673a", None))
        self.btn_sel_folder.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76ee\u5f55", None))
        self.txtHz.setInputMask("")
        self.txtHz.setText(QCoreApplication.translate("MainWindow", u".txt", None))
        self.btnSearchFiles.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u6587\u4ef6", None))
        self.cbIsFy.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1", None))
        self.txt_soure.setDocumentTitle("")
        self.txt_soure.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6\u540e\u8bfb\u53d6\u6e90\u6587\u672c", None))
        self.btn_fy.setText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.txt_rz.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u7ffb\u8bd1\u540e\u7684\u7ed3\u679c", None))
    # retranslateUi


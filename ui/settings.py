# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 615)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tb_header = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb_header.setGeometry(QtCore.QRect(-1, 0, 711, 111))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.tb_header.setFont(font)
        self.tb_header.setObjectName("tb_header")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 241, 181))
        self.groupBox.setObjectName("groupBox")
        self.small_font = QtWidgets.QRadioButton(self.groupBox)
        self.small_font.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.small_font.setObjectName("small_font")
        self.middle_font = QtWidgets.QRadioButton(self.groupBox)
        self.middle_font.setGeometry(QtCore.QRect(20, 80, 95, 20))
        self.middle_font.setObjectName("middle_font")
        self.big_font = QtWidgets.QRadioButton(self.groupBox)
        self.big_font.setGeometry(QtCore.QRect(20, 120, 95, 20))
        self.big_font.setObjectName("big_font")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 320, 241, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.chanel_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.chanel_2.setGeometry(QtCore.QRect(20, 40, 181, 20))
        self.chanel_2.setObjectName("chanel_2")
        self.chanel_0 = QtWidgets.QRadioButton(self.groupBox_2)
        self.chanel_0.setGeometry(QtCore.QRect(20, 100, 181, 20))
        self.chanel_0.setObjectName("chanel_0")
        self.chanel_1 = QtWidgets.QRadioButton(self.groupBox_2)
        self.chanel_1.setGeometry(QtCore.QRect(20, 160, 181, 20))
        self.chanel_1.setObjectName("chanel_1")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(600, 490, 93, 81))
        self.back_button.setObjectName("back_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 26))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_edit = QtWidgets.QMenu(self.menubar)
        self.menu_edit.setObjectName("menu_edit")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_window = QtWidgets.QMenu(self.menubar)
        self.menu_window.setObjectName("menu_window")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_window.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tb_header.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#d0ecf8\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">   </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:600;\">JsfReader</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">   Настойки</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Размер шрифта"))
        self.small_font.setText(_translate("MainWindow", "Маленький"))
        self.middle_font.setText(_translate("MainWindow", "Средний"))
        self.big_font.setText(_translate("MainWindow", "Большой"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Изображение"))
        self.chanel_2.setText(_translate("MainWindow", "Строить с двух каналов"))
        self.chanel_0.setText(_translate("MainWindow", "Строить с канала 0"))
        self.chanel_1.setText(_translate("MainWindow", "Строить с канала 1"))
        self.back_button.setText(_translate("MainWindow", "<-"))
        self.menu_file.setTitle(_translate("MainWindow", "Файл"))
        self.menu_edit.setTitle(_translate("MainWindow", "Правка"))
        self.menu.setTitle(_translate("MainWindow", "Вид"))
        self.menu_window.setTitle(_translate("MainWindow", "Окно"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.action_open.setText(_translate("MainWindow", "Открыть"))
        self.action_save.setText(_translate("MainWindow", "Сохранить"))
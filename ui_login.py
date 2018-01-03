# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import Korisnik
import ui_ShoppingApp
import ui_registracija

class Ui_Prijava(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(586, 436)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 110, 301, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblKorisnickoIme = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblKorisnickoIme.setObjectName("lblKorisnickoIme")
        self.verticalLayout.addWidget(self.lblKorisnickoIme)
        self.lblLozinka = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lblLozinka.setObjectName("lblLozinka")
        self.verticalLayout.addWidget(self.lblLozinka)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditKorisnickoIme = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditKorisnickoIme.setObjectName("lineEditKorisnickoIme")
        self.verticalLayout_2.addWidget(self.lineEditKorisnickoIme)
        self.lineEditLozinka = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditLozinka.setObjectName("lineEditLozinka")
        self.lineEditLozinka.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.lineEditLozinka)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(130, 210, 301, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.provjeraKorisnika)
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.otvoriui_registracija)
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.lblKorisnickoIme.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Prijava"))
        self.lblKorisnickoIme.setText(_translate("Dialog", "Korisničko ime: "))
        self.lblLozinka.setText(_translate("Dialog", "Lozinka"))
        self.pushButton.setText(_translate("Dialog", "Prijava"))
        self.pushButton_2.setText(_translate("Dialog", "Registracija"))

    def provjeraKorisnika(self):
        korisnik = Korisnik.Korisnik()
        korisnickoIme = self.lineEditKorisnickoIme.text()
        lozinka = self.lineEditLozinka.text()
        korisnikID = korisnik.prijavaProvjeriKorisnika(korisnickoIme, lozinka)
        if korisnikID:
            self.ShoppingApp = ui_ShoppingApp.Ui_frmGlavna(korisnikID)
            self.ShoppingApp.show()
            self.close()
        else:
            self.prikaziUpozorenje('Warning', 'Netočno korisničko ime ili lozinka')


    def otvoriui_registracija(self):
        self.registracija = ui_registracija.Ui_Registracija()
        self.registracija.show()
        self.close()

    def prikaziUpozorenje(self, naziv, poruka):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(naziv)
        msgBox.setText(poruka)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IzmjenaKorisnika.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Korisnik
import WigetAdministracijaKorisnika

class Ui_frmIzmjenaKorisnika(QtWidgets.QWidget):
    def __init__(self, podaciOKorisniku):
        QtWidgets.QWidget.__init__(self)
        self.podaciOKorisniku = podaciOKorisniku
        self.setupUi(self)


    def setupUi(self, frmIzmjenaKorisnika):
        frmIzmjenaKorisnika.setObjectName("frmIzmjenaKorisnika")
        frmIzmjenaKorisnika.resize(699, 529)
        self.horizontalLayout = QtWidgets.QHBoxLayout(frmIzmjenaKorisnika)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutIzmjenaKorisnika = QtWidgets.QVBoxLayout()
        self.verticalLayoutIzmjenaKorisnika.setObjectName("verticalLayoutIzmjenaKorisnika")
        self.labelIzmjenaKorisnika = QtWidgets.QLabel(frmIzmjenaKorisnika)
        self.labelIzmjenaKorisnika.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelIzmjenaKorisnika.setFont(font)
        self.labelIzmjenaKorisnika.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIzmjenaKorisnika.setObjectName("labelIzmjenaKorisnika")
        self.verticalLayoutIzmjenaKorisnika.addWidget(self.labelIzmjenaKorisnika)
        self.horizontalLayoutKorisnickoIme = QtWidgets.QHBoxLayout()
        self.horizontalLayoutKorisnickoIme.setObjectName("horizontalLayoutKorisnickoIme")
        self.labelKorisnickoIme = QtWidgets.QLabel(frmIzmjenaKorisnika)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelKorisnickoIme.setFont(font)
        self.labelKorisnickoIme.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelKorisnickoIme.setObjectName("labelKorisnickoIme")
        self.horizontalLayoutKorisnickoIme.addWidget(self.labelKorisnickoIme)
        self.lineEditKorisnickoIme = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditKorisnickoIme.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditKorisnickoIme.setText(self.podaciOKorisniku[1])
        self.lineEditKorisnickoIme.setObjectName("lineEditKorisnickoIme")
        self.horizontalLayoutKorisnickoIme.addWidget(self.lineEditKorisnickoIme)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutKorisnickoIme.addItem(spacerItem)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutKorisnickoIme)
        self.horizontalLayoutLozinka = QtWidgets.QHBoxLayout()
        self.horizontalLayoutLozinka.setObjectName("horizontalLayoutLozinka")
        self.labelLozinka = QtWidgets.QLabel(frmIzmjenaKorisnika)
        self.labelLozinka.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelLozinka.setFont(font)
        self.labelLozinka.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelLozinka.setObjectName("labelLozinka")
        self.horizontalLayoutLozinka.addWidget(self.labelLozinka)
        self.lineEditLozinka = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditLozinka.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditLozinka.setText(self.podaciOKorisniku[2])
        self.lineEditLozinka.setObjectName("lineEditLozinka")
        self.horizontalLayoutLozinka.addWidget(self.lineEditLozinka)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutLozinka.addItem(spacerItem1)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutLozinka)
        self.horizontalLayoutIme = QtWidgets.QHBoxLayout()
        self.horizontalLayoutIme.setObjectName("horizontalLayoutIme")
        self.labelIme = QtWidgets.QLabel(frmIzmjenaKorisnika)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelIme.setFont(font)
        self.labelIme.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelIme.setObjectName("labelIme")
        self.horizontalLayoutIme.addWidget(self.labelIme)
        self.lineEditIme = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditIme.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditIme.setText(self.podaciOKorisniku[3])
        self.lineEditIme.setObjectName("lineEditIme")
        self.horizontalLayoutIme.addWidget(self.lineEditIme)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutIme.addItem(spacerItem2)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutIme)
        self.horizontalLayoutPrezime = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPrezime.setObjectName("horizontalLayoutPrezime")
        self.labelPrezime = QtWidgets.QLabel(frmIzmjenaKorisnika)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelPrezime.setFont(font)
        self.labelPrezime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPrezime.setObjectName("labelPrezime")
        self.horizontalLayoutPrezime.addWidget(self.labelPrezime)
        self.lineEditPrezime = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditPrezime.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditPrezime.setText(self.podaciOKorisniku[4])
        self.lineEditPrezime.setObjectName("lineEditPrezime")
        self.horizontalLayoutPrezime.addWidget(self.lineEditPrezime)
        spacerItem3 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutPrezime.addItem(spacerItem3)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutPrezime)
        self.horizontalLayoutEmail = QtWidgets.QHBoxLayout()
        self.horizontalLayoutEmail.setObjectName("horizontalLayoutEmail")
        self.labelEmail = QtWidgets.QLabel(frmIzmjenaKorisnika)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelEmail.setFont(font)
        self.labelEmail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelEmail.setObjectName("labelEmail")
        self.horizontalLayoutEmail.addWidget(self.labelEmail)
        self.lineEditEmail = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditEmail.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditEmail.setText(self.podaciOKorisniku[5])
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.horizontalLayoutEmail.addWidget(self.lineEditEmail)
        spacerItem4 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutEmail.addItem(spacerItem4)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutEmail)
        self.horizontalLayoutBrojTelefona = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBrojTelefona.setObjectName("horizontalLayoutBrojTelefona")
        self.labelBrojTelefona = QtWidgets.QLabel(frmIzmjenaKorisnika)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelBrojTelefona.setFont(font)
        self.labelBrojTelefona.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBrojTelefona.setObjectName("labelBrojTelefona")
        self.horizontalLayoutBrojTelefona.addWidget(self.labelBrojTelefona)
        self.lineEditBrojTelefona = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditBrojTelefona.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditBrojTelefona.setText(self.podaciOKorisniku[6])
        self.lineEditBrojTelefona.setObjectName("lineEditBrojTelefona")
        self.horizontalLayoutBrojTelefona.addWidget(self.lineEditBrojTelefona)
        spacerItem5 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutBrojTelefona.addItem(spacerItem5)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutBrojTelefona)
        self.horizontalLayoutBrojKartice = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBrojKartice.setObjectName("horizontalLayoutBrojKartice")
        self.labelBrojKartice = QtWidgets.QLabel(frmIzmjenaKorisnika)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelBrojKartice.setFont(font)
        self.labelBrojKartice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelBrojKartice.setObjectName("labelBrojKartice")
        self.horizontalLayoutBrojKartice.addWidget(self.labelBrojKartice)
        self.lineEditBrojKartice = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditBrojKartice.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditBrojKartice.setText(self.podaciOKorisniku[7])
        self.lineEditBrojKartice.setObjectName("lineEditBrojKartice")
        self.horizontalLayoutBrojKartice.addWidget(self.lineEditBrojKartice)
        spacerItem6 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutBrojKartice.addItem(spacerItem6)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutBrojKartice)
        self.horizontalLayoutAdresa = QtWidgets.QHBoxLayout()
        self.horizontalLayoutAdresa.setObjectName("horizontalLayoutAdresa")
        self.labelAdresa = QtWidgets.QLabel(frmIzmjenaKorisnika)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAdresa.setFont(font)
        self.labelAdresa.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAdresa.setObjectName("labelAdresa")
        self.horizontalLayoutAdresa.addWidget(self.labelAdresa)
        self.lineEditAdresa = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditAdresa.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditAdresa.setText(self.podaciOKorisniku[8])
        self.lineEditAdresa.setObjectName("lineEditAdresa")
        self.horizontalLayoutAdresa.addWidget(self.lineEditAdresa)
        spacerItem7 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutAdresa.addItem(spacerItem7)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutAdresa)
        self.horizontalLayoutDrzava = QtWidgets.QHBoxLayout()
        self.horizontalLayoutDrzava.setObjectName("horizontalLayoutDrzava")
        self.labelDrzava = QtWidgets.QLabel(frmIzmjenaKorisnika)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelDrzava.setFont(font)
        self.labelDrzava.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDrzava.setObjectName("labelDrzava")
        self.horizontalLayoutDrzava.addWidget(self.labelDrzava)
        self.lineEditDrzava = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditDrzava.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditDrzava.setText(self.podaciOKorisniku[9])
        self.lineEditDrzava.setObjectName("lineEditDrzava")
        self.horizontalLayoutDrzava.addWidget(self.lineEditDrzava)
        spacerItem8 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutDrzava.addItem(spacerItem8)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutDrzava)
        #postanski broj
        self.horizontalLayoutPostanskiBroj = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPostanskiBroj.setObjectName("horizontalLayoutPostanskiBroj")
        self.labelPostanskiBroj = QtWidgets.QLabel(frmIzmjenaKorisnika)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelPostanskiBroj.setFont(font)
        self.labelPostanskiBroj.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPostanskiBroj.setObjectName("labelPostanskiBroj")
        self.horizontalLayoutPostanskiBroj.addWidget(self.labelPostanskiBroj)
        self.lineEditPostanskiBroj = QtWidgets.QLineEdit(frmIzmjenaKorisnika)
        self.lineEditPostanskiBroj.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditPostanskiBroj.setText(self.podaciOKorisniku[10])
        self.lineEditPostanskiBroj.setObjectName("lineEditPostanskiBroj")
        self.horizontalLayoutPostanskiBroj.addWidget(self.lineEditPostanskiBroj)
        spacerItem9 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutPostanskiBroj.addItem(spacerItem9)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayoutPostanskiBroj)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.actionIzmjeniKorisnika = QtWidgets.QPushButton(frmIzmjenaKorisnika)
        self.actionIzmjeniKorisnika.setMinimumSize(QtCore.QSize(0, 30))
        self.actionIzmjeniKorisnika.setObjectName("actionIzmjeniKorisnika")
        self.actionIzmjeniKorisnika.setText("Izmjeni Korisnika")
        self.actionIzmjeniKorisnika.released.connect(self.izmjenaKorisnika)
        self.horizontalLayout_2.addWidget(self.actionIzmjeniKorisnika)
        spacerItem11 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.verticalLayoutIzmjenaKorisnika.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayoutIzmjenaKorisnika)

        self.retranslateUi(frmIzmjenaKorisnika)
        QtCore.QMetaObject.connectSlotsByName(frmIzmjenaKorisnika)

    def retranslateUi(self, frmIzmjenaKorisnika):
        _translate = QtCore.QCoreApplication.translate
        frmIzmjenaKorisnika.setWindowTitle(_translate("frmIzmjenaKorisnika", "Form"))
        self.labelIzmjenaKorisnika.setText(_translate("frmIzmjenaKorisnika", "Izmjena Korisnika"))
        self.labelKorisnickoIme.setText(_translate("frmIzmjenaKorisnika", "Korisničko ime: "))
        self.labelLozinka.setText(_translate("frmIzmjenaKorisnika", "Lozinka: "))
        self.labelIme.setText(_translate("frmIzmjenaKorisnika", "Ime: "))
        self.labelPrezime.setText(_translate("frmIzmjenaKorisnika", "Prezime: "))
        self.labelEmail.setText(_translate("frmIzmjenaKorisnika", "Email: "))
        self.labelBrojTelefona.setText(_translate("frmIzmjenaKorisnika", "Broj telefona: "))
        self.labelBrojKartice.setText(_translate("frmIzmjenaKorisnika", "Broj Kartice: "))
        self.labelAdresa.setText(_translate("frmIzmjenaKorisnika", "Adresa: "))
        self.labelDrzava.setText(_translate("frmIzmjenaKorisnika", "Drzava: "))
        self.labelPostanskiBroj.setText(_translate("frmIzmjenaKorisnika", "Postanski Broj: "))

    def izmjenaKorisnika(self):
        korisnik = Korisnik.Korisnik()
        korisnickoIme = self.lineEditKorisnickoIme.text()
        lozinka = self.lineEditLozinka.text()
        ime = self.lineEditIme.text()
        prezime = self.lineEditPrezime.text()
        email = self.lineEditEmail.text()
        brojTelefona = self.lineEditBrojTelefona.text()
        brojKartice = self.lineEditBrojKartice.text()
        adresa = self.lineEditAdresa.text()
        drzava = self.lineEditDrzava.text()
        postanskiBroj = self.lineEditPostanskiBroj.text()
        korisnikID = self.podaciOKorisniku[0]
        korisnik.izmjeniKorisnika(korisnikID, korisnickoIme, lozinka, ime, prezime, email, brojTelefona, brojKartice, adresa, drzava, postanskiBroj)
        self.close()



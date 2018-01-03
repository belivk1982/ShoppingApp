# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_AdministracijaOdjeca.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Odjeca
import os
import shutil

class Ui_AdministracijaOdjeca(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.ispisOdjeca()


    def setupUi(self, AdministracijaOdjeca):
        AdministracijaOdjeca.setObjectName("AdministracijaOdjeca")
        AdministracijaOdjeca.resize(632, 646)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AdministracijaOdjeca)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutTableForm = QtWidgets.QVBoxLayout()
        self.verticalLayoutTableForm.setObjectName("verticalLayoutTableForm")
        self.tableWidgetOdjeca = QtWidgets.QTableWidget(AdministracijaOdjeca)
        self.tableWidgetOdjeca.setMaximumSize(QtCore.QSize(450, 16777215))
        self.tableWidgetOdjeca.setRowCount(5)
        self.tableWidgetOdjeca.setColumnCount(5)
        self.tableWidgetOdjeca.setObjectName("tableWidgetKorisnici")
        self.verticalLayoutTableForm.addWidget(self.tableWidgetOdjeca)
        self.horizontalLayoutNaziv = QtWidgets.QHBoxLayout()
        self.horizontalLayoutNaziv.setContentsMargins(10, -1, 0, -1)
        self.horizontalLayoutNaziv.setSpacing(6)
        self.horizontalLayoutNaziv.setObjectName("horizontalLayoutNaziv")
        self.labelNaziv = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelNaziv.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNaziv.setFont(font)
        self.labelNaziv.setObjectName("labelNaziv")
        self.horizontalLayoutNaziv.addWidget(self.labelNaziv)
        self.lineEditNaziv = QtWidgets.QLineEdit(AdministracijaOdjeca)
        self.lineEditNaziv.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditNaziv.setObjectName("lineEditNaziv")
        self.horizontalLayoutNaziv.addWidget(self.lineEditNaziv)
        self.labelEmpty2 = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelEmpty2.setObjectName("labelEmpty2")
        self.horizontalLayoutNaziv.addWidget(self.labelEmpty2)
        self.verticalLayoutTableForm.addLayout(self.horizontalLayoutNaziv)
        self.horizontalCijena = QtWidgets.QHBoxLayout()
        self.horizontalCijena.setContentsMargins(10, -1, -1, -1)
        self.horizontalCijena.setObjectName("horizontalCijena")
        self.labelCijena = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelCijena.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCijena.setFont(font)
        self.labelCijena.setObjectName("labelCijena")
        self.horizontalCijena.addWidget(self.labelCijena)
        self.lineEditCijena = QtWidgets.QLineEdit(AdministracijaOdjeca)
        self.lineEditCijena.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditCijena.setObjectName("lineEditCijena")
        self.horizontalCijena.addWidget(self.lineEditCijena)
        self.label = QtWidgets.QLabel(AdministracijaOdjeca)
        self.label.setObjectName("label")
        self.horizontalCijena.addWidget(self.label)
        self.verticalLayoutTableForm.addLayout(self.horizontalCijena)
        self.horizontalSnizenje = QtWidgets.QHBoxLayout()
        self.horizontalSnizenje.setContentsMargins(10, -1, -1, -1)
        self.horizontalSnizenje.setObjectName("horizontalSnizenje")
        self.labelSnizenje = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelSnizenje.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSnizenje.setFont(font)
        self.labelSnizenje.setObjectName("labelSnizenje")
        self.horizontalSnizenje.addWidget(self.labelSnizenje)
        self.comboBoxSnizenje = QtWidgets.QComboBox(AdministracijaOdjeca)
        self.comboBoxSnizenje.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBoxSnizenje.setObjectName("comboBoxSnizenje")
        self.comboBoxSnizenje.addItem("0")
        self.comboBoxSnizenje.addItem("10%")
        self.comboBoxSnizenje.addItem("20%")
        self.comboBoxSnizenje.addItem("30%")
        self.comboBoxSnizenje.addItem("40%")
        self.comboBoxSnizenje.addItem("50%")
        self.comboBoxSnizenje.addItem("60%")
        self.comboBoxSnizenje.addItem("70%")
        self.horizontalSnizenje.addWidget(self.comboBoxSnizenje)
        self.label_2 = QtWidgets.QLabel(AdministracijaOdjeca)
        self.label_2.setObjectName("label_2")
        self.horizontalSnizenje.addWidget(self.label_2)
        self.verticalLayoutTableForm.addLayout(self.horizontalSnizenje)
        self.horizontalLayoutSpol = QtWidgets.QHBoxLayout()
        self.horizontalLayoutSpol.setContentsMargins(10, -1, 0, -1)
        self.horizontalLayoutSpol.setObjectName("horizontalLayoutSpol")
        self.labelSpol = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelSpol.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSpol.setFont(font)
        self.labelSpol.setObjectName("labelSpol")
        self.horizontalLayoutSpol.addWidget(self.labelSpol)
        self.radioButtonMuski = QtWidgets.QRadioButton(AdministracijaOdjeca)
        self.radioButtonMuski.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButtonMuski.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButtonMuski.setObjectName("radioButtonMuski")
        self.horizontalLayoutSpol.addWidget(self.radioButtonMuski)
        self.radioButtonZenski = QtWidgets.QRadioButton(AdministracijaOdjeca)
        self.radioButtonZenski.setObjectName("radioButtonZenski")
        self.radioButtonZenski.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButtonZenski.setMinimumSize(QtCore.QSize(100, 0))
        self.horizontalLayoutSpol.addWidget(self.radioButtonZenski)
        self.radioButtonDjecja = QtWidgets.QRadioButton(AdministracijaOdjeca)
        self.radioButtonDjecja.setObjectName("radioButtonDjecja")
        self.radioButtonDjecja.setText("Za djecu")
        self.horizontalLayoutSpol.addWidget(self.radioButtonDjecja)
        self.verticalLayoutTableForm.addLayout(self.horizontalLayoutSpol)
        self.horizontalLayoutSlika = QtWidgets.QHBoxLayout()
        self.horizontalLayoutSlika.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayoutSlika.setObjectName("horizontalLayoutSlika")
        self.labelSlika = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelSlika.setMinimumSize(QtCore.QSize(98, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSlika.setFont(font)
        self.labelSlika.setObjectName("labelSlika")
        self.horizontalLayoutSlika.addWidget(self.labelSlika)
        self.lineEditSlika = QtWidgets.QLineEdit(AdministracijaOdjeca)
        self.lineEditSlika.setObjectName("lineEdit")
        self.horizontalLayoutSlika.addWidget(self.lineEditSlika)
        self.actionOdaberiSliku = QtWidgets.QPushButton(AdministracijaOdjeca)
        self.actionOdaberiSliku.setObjectName("actionOdaberiSliku")
        self.actionOdaberiSliku.released.connect(self.odabirSike)
        self.horizontalLayoutSlika.addWidget(self.actionOdaberiSliku)
        self.verticalLayoutTableForm.addLayout(self.horizontalLayoutSlika)
        self.horizontalLayoutNazivSlike = QtWidgets.QHBoxLayout()
        self.horizontalLayoutNazivSlike.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayoutNazivSlike.setObjectName("horizontalLayoutNazivSlike")
        self.labelNazivSlike = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelNazivSlike.setMinimumSize(QtCore.QSize(98, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelNazivSlike.setFont(font)
        self.labelNazivSlike.setObjectName("labelNazivSlike")
        self.labelNazivSlike.setText("Naziv Slike: ")
        self.horizontalLayoutNazivSlike.addWidget(self.labelNazivSlike)
        self.lineEditNazivSlike = QtWidgets.QLineEdit(AdministracijaOdjeca)
        self.lineEditNazivSlike.setObjectName("lineEditNazivSlike")
        self.horizontalLayoutNazivSlike.addWidget(self.lineEditNazivSlike)
        self.label_3 = QtWidgets.QLabel(AdministracijaOdjeca)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutNazivSlike.addWidget(self.label_3)
        self.verticalLayoutTableForm.addLayout(self.horizontalLayoutNazivSlike)
        self.horizontalLayoutKolicina = QtWidgets.QHBoxLayout()
        self.horizontalLayoutKolicina.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayoutKolicina.setObjectName("horizontalLayoutKolicina")
        self.labelKolicina = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelKolicina.setMinimumSize(QtCore.QSize(97, 0))
        self.labelKolicina.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelKolicina.setFont(font)
        self.labelKolicina.setObjectName("labelKolicina")
        self.horizontalLayoutKolicina.addWidget(self.labelKolicina)
        self.lineEditKolicina = QtWidgets.QLineEdit(AdministracijaOdjeca)
        self.lineEditKolicina.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditKolicina.setObjectName("lineEditKolicina")
        self.horizontalLayoutKolicina.addWidget(self.lineEditKolicina)
        self.labelEmpty = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelEmpty.setObjectName("labelEmpty")
        self.horizontalLayoutKolicina.addWidget(self.labelEmpty)
        self.verticalLayoutTableForm.addLayout(self.horizontalLayoutKolicina)
        self.horizontalLayoutVelicina = QtWidgets.QHBoxLayout()
        self.horizontalLayoutVelicina.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayoutVelicina.setObjectName("horizontalLayoutVelicina")
        self.labelVelicina = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelVelicina.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelVelicina.setFont(font)
        self.labelVelicina.setObjectName("labelVelicina")
        self.horizontalLayoutVelicina.addWidget(self.labelVelicina)
        self.comboBoxVelicina = QtWidgets.QComboBox(AdministracijaOdjeca)
        self.comboBoxVelicina.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBoxVelicina.setObjectName("comboBoxVelicina")
        self.comboBoxVelicina.addItem("")
        self.comboBoxVelicina.addItem("")
        self.comboBoxVelicina.addItem("")
        self.comboBoxVelicina.addItem("")
        self.comboBoxVelicina.addItem("")
        self.horizontalLayoutVelicina.addWidget(self.comboBoxVelicina)
        self.labelEmpty3 = QtWidgets.QLabel(AdministracijaOdjeca)
        self.labelEmpty3.setObjectName("labelEmpty3")
        self.horizontalLayoutVelicina.addWidget(self.labelEmpty3)
        self.verticalLayoutTableForm.addLayout(self.horizontalLayoutVelicina)
        self.horizontalLayoutButtonUnesiUredi = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtonUnesiUredi.setContentsMargins(50, -1, -1, -1)
        self.horizontalLayoutButtonUnesiUredi.setObjectName("horizontalLayoutButtonUnesiUredi")
        self.actionUnesiOdjecu = QtWidgets.QPushButton(AdministracijaOdjeca)
        self.actionUnesiOdjecu.setMinimumSize(QtCore.QSize(0, 35))
        self.actionUnesiOdjecu.setObjectName("actionUnesiOdjecu")
        self.actionUnesiOdjecu.released.connect(self.unesiOdjecu)
        self.horizontalLayoutButtonUnesiUredi.addWidget(self.actionUnesiOdjecu)
        self.actionUrediOdjecu = QtWidgets.QPushButton(AdministracijaOdjeca)
        self.actionUrediOdjecu.setMinimumSize(QtCore.QSize(0, 35))
        self.actionUrediOdjecu.released.connect(self.dodajKolicinuOdjece)
        self.actionUrediOdjecu.setObjectName("actionUrediOdjecu")
        self.horizontalLayoutButtonUnesiUredi.addWidget(self.actionUrediOdjecu)
        self.verticalLayoutTableForm.addLayout(self.horizontalLayoutButtonUnesiUredi)
        self.horizontalLayout.addLayout(self.verticalLayoutTableForm)
        self.verticalLayoutUrediObrisi = QtWidgets.QVBoxLayout()
        self.verticalLayoutUrediObrisi.setObjectName("verticalLayoutUrediObrisi")
        self.actionOdaberiOdjecu = QtWidgets.QPushButton(AdministracijaOdjeca)
        self.actionOdaberiOdjecu.setMinimumSize(QtCore.QSize(140, 50))
        self.actionOdaberiOdjecu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.actionOdaberiOdjecu.setObjectName("actionOdaberiOdjecu")
        self.actionOdaberiOdjecu.released.connect(self.odaberiPostojecuOdjecu)
        self.verticalLayoutUrediObrisi.addWidget(self.actionOdaberiOdjecu)
        self.actionBrisiOdjecu = QtWidgets.QPushButton(AdministracijaOdjeca)
        self.actionBrisiOdjecu.setMinimumSize(QtCore.QSize(0, 50))
        self.actionBrisiOdjecu.setObjectName("actionBrisiOdjecu")
        self.actionBrisiOdjecu.released.connect(self.obrisiOdjecu)
        self.verticalLayoutUrediObrisi.addWidget(self.actionBrisiOdjecu)
        spacerItem = QtWidgets.QSpacerItem(20, 384, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayoutUrediObrisi.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayoutUrediObrisi)

        self.retranslateUi(AdministracijaOdjeca)
        QtCore.QMetaObject.connectSlotsByName(AdministracijaOdjeca)

    def retranslateUi(self, AdministracijaOdjeca):
        _translate = QtCore.QCoreApplication.translate
        AdministracijaOdjeca.setWindowTitle(_translate("AdministracijaOdjeca", "Form"))
        self.labelNaziv.setText(_translate("AdministracijaOdjeca", "Naziv: "))
        self.labelEmpty2.setText(_translate("AdministracijaOdjeca", " "))
        self.labelCijena.setText(_translate("AdministracijaOdjeca", "Cijena: "))
        self.label.setText(_translate("AdministracijaOdjeca", ",00 kn"))
        self.labelSnizenje.setText(_translate("AdministracijaOdjeca", "Sniženje: "))
        self.labelSpol.setText(_translate("AdministracijaOdjeca", "Spol: "))
        self.radioButtonMuski.setText(_translate("AdministracijaOdjeca", "Muški"))
        self.radioButtonZenski.setText(_translate("AdministracijaOdjeca", "Ženski"))
        self.labelSlika.setText(_translate("AdministracijaOdjeca", "Slika: "))
        self.actionOdaberiSliku.setText(_translate("AdministracijaOdjeca", "Odabir slike"))
        self.labelKolicina.setText(_translate("AdministracijaOdjeca", "Količina: "))
        self.labelEmpty.setText(_translate("AdministracijaOdjeca", " "))
        self.labelVelicina.setText(_translate("AdministracijaOdjeca", "Veličina: "))
        self.comboBoxVelicina.setItemText(0, _translate("AdministracijaOdjeca", "XS"))
        self.comboBoxVelicina.setItemText(1, _translate("AdministracijaOdjeca", "S"))
        self.comboBoxVelicina.setItemText(2, _translate("AdministracijaOdjeca", "M"))
        self.comboBoxVelicina.setItemText(3, _translate("AdministracijaOdjeca", "L"))
        self.comboBoxVelicina.setItemText(4, _translate("AdministracijaOdjeca", "XL"))
        self.comboBoxVelicina.setItemText(4, _translate("AdministracijaOdjeca", "XXL"))
        self.labelEmpty3.setText(_translate("AdministracijaOdjeca", " "))
        self.actionUnesiOdjecu.setText(_translate("AdministracijaOdjeca", "Unesi novu odjeću"))
        self.actionUrediOdjecu.setText(_translate("AdministracijaOdjeca", "Dodaj količinu"))
        self.actionOdaberiOdjecu.setText(_translate("AdministracijaOdjeca", "Odaberi odjeću"))
        self.actionBrisiOdjecu.setText(_translate("AdministracijaOdjeca", "Obriši"))


    def ispisOdjeca(self):
        self.tableWidgetOdjeca.clear()
        odjeca = Odjeca.Odjeca()
        popisOdjece = odjeca.dohvatiOdjecu()
        self.tableWidgetOdjeca.setRowCount(0)
        for brojReda, podaciPoRedu in enumerate(popisOdjece):
            self.tableWidgetOdjeca.insertRow(brojReda)
            for brojStupca, podaciPoStupcu in enumerate(podaciPoRedu):
                self.tableWidgetOdjeca.setItem(brojReda, brojStupca, QtWidgets.QTableWidgetItem(str(podaciPoStupcu)))

    def dohvatiOdjecu(self):
        listaPodatakaOOdjeci = []
        for i in range(5):
            listaPodatakaOOdjeci.append(self.tableWidgetOdjeca.item(self.tableWidgetOdjeca.currentRow(), i).text())
        return  listaPodatakaOOdjeci

    def obrisiOdjecu(self):
        odjeca = Odjeca.Odjeca()
        lista = self.dohvatiOdjecu()
        odjeca.obrisiOdjecu(int(lista[0]))
        self.ispisOdjeca()

    def odabirSike(self):
        putanjaDoSlike = QtWidgets.QFileDialog.getOpenFileName(self, 'Picture', '', '*.png *.jpeg *.jpg')
        self.lineEditSlika.setText(putanjaDoSlike[0])

    def unesiOdjecu(self):

        odjeca = Odjeca.Odjeca()

        naziv = self.lineEditNaziv.text()
        cijena = self.lineEditCijena.text()
        kolicina = self.lineEditKolicina.text()
        snizenje = self.comboBoxSnizenje.currentText()
        velicina = self.comboBoxVelicina.currentText()
        spol = self.odaberiSpol()
        snizenjeID = self.izracunajSnizenjeID(snizenje)
        velicinaID = self.odaberiVelicinu(velicina)

        if self.lineEditSlika.text():
            prethodnaPutanja = self.lineEditSlika.text()
            datoteka, ekstenzija = os.path.splitext(prethodnaPutanja)
            novaPutanja = os.path.dirname(__file__)
            novaPutanja = os.path.join(novaPutanja, 'Slikeodjece' + '/' + self.lineEditNazivSlike.text() + ekstenzija)
            slikaBaza = 'Slikeodjece' + '/' + self.lineEditNazivSlike.text() + ekstenzija
            shutil.move(prethodnaPutanja, novaPutanja)
        else:
            slikaBaza = " "
        odjeca.unesiOdjecu(cijena, naziv, snizenjeID, spol, slikaBaza , velicinaID, kolicina)
        self.ispisOdjeca()


    def odaberiPostojecuOdjecu(self):
        lista = self.dohvatiOdjecu()
        self.lineEditNaziv.setText(lista[2])
        self.lineEditCijena.setText(lista[1])
        self.lineEditNaziv.setEnabled(False)
        self.lineEditCijena.setEnabled(False)
        self.lineEditSlika.setEnabled(False)
        self.comboBoxSnizenje.setEnabled(False)
        self.radioButtonMuski.setEnabled(False)
        self.radioButtonZenski.setEnabled(False)
        self.radioButtonDjecja.setEnabled(False)
        self.lineEditSlika.setEnabled(False)
        self.lineEditNazivSlike.setEnabled(False)
        self.idOdjeca = lista[0]

    def dodajKolicinuOdjece(self):
        odjecaIzmjenjena = False
        odjeca = Odjeca.Odjeca()
        kolicina = int(self.lineEditKolicina.text())
        velicina = self.comboBoxVelicina.currentText()
        velicinaID = self.odaberiVelicinu(velicina)
        listaUnesenihVelicina = odjeca.dohvatiVelicineOdjece()
        for index, velicinaOdjece in enumerate(listaUnesenihVelicina):
            if int(velicinaOdjece[0]) == int(self.idOdjeca) and int(velicinaOdjece[1]) == int(velicinaID):
                if velicinaOdjece[2] is not None:
                    kolicina = kolicina + int(velicinaOdjece[2])
                odjeca.izmjeniKolicinu(kolicina, velicinaOdjece[0], int(velicinaOdjece[1]))
                odjecaIzmjenjena = True
        if odjecaIzmjenjena == False:
            odjeca.unesiVelicinuIKolicinuOdjece(self.idOdjeca, velicinaID, kolicina)
        self.ispisOdjeca()


    def izracunajSnizenjeID(self, snizenje):
        if snizenje == "0":
            return 10
        else:
            if snizenje == "10%":
                return 1
            if snizenje == "20%":
                return 2
            if snizenje == "30%":
                return 3
            if snizenje == "40%":
                return 4
            if snizenje == "50%":
                return 5
            if snizenje == "60%":
                return 6
            if snizenje == "70%":
                return 7

    def odaberiSpol(self):
        if self.radioButtonZenski.isChecked():
            return 2
        if self.radioButtonMuski.isChecked():
            return 1
        if self.radioButtonDjecja.isChecked():
            return 3

    def odaberiVelicinu(self, velicina):
        if velicina == "S":
            return 1
        if velicina == "XS":
            return 2
        if velicina == "M":
            return 3
        if velicina == "L":
            return 4
        if velicina == "XL":
            return 5
        if velicina == "XXL":
            return 6






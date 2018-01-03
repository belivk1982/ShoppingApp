# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShoppingApp2.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import sys
import Odjeca
import VertikalniTab
import Kosarica
import ui_comboOdabir
import ui_login
import ui_AdministracijaOdjeca
import WigetAdministracijaKorisnika


class Ui_frmGlavna(QtWidgets.QWidget):
    def __init__(self, korisnikID):
        QtWidgets.QWidget.__init__(self)
        self.korisnik = korisnikID
        print(self.korisnik)
        self.korisnikID = int(korisnikID[0][0])
        self.setupUi(self)



    def setupUi(self, frmGlavna):
        frmGlavna.setObjectName("frmGlavna")
        frmGlavna.resize(965, 800)
        frmGlavna.setMaximumSize(QtCore.QSize(965, 16777215))

        self.layGlavnaForma = QtWidgets.QHBoxLayout(frmGlavna)
        self.layGlavnaForma.setObjectName("layGlavnaForma")
        self.layGlavnaFormaVertikalno = QtWidgets.QVBoxLayout()
        self.layGlavnaFormaVertikalno.setObjectName("layGlavnaFormaVertikalno")
        self.layZaglavlje = QtWidgets.QHBoxLayout()
        self.layZaglavlje.setContentsMargins(-1, -1, -1, 0)
        self.layZaglavlje.setObjectName("layZaglavlje")
        self.lblNazivAplikacije = QtWidgets.QLabel(frmGlavna)
        self.lblNazivAplikacije.setMinimumSize(QtCore.QSize(700, 123))
        self.lblNazivAplikacije.setMaximumSize(QtCore.QSize(800, 150))
        self.lblNazivAplikacije.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNazivAplikacije.setObjectName("lblNazivAplikacije")
        self.layZaglavlje.addWidget(self.lblNazivAplikacije)
        self.actionOdjava = QtWidgets.QPushButton(frmGlavna)
        self.actionOdjava.setMinimumSize(QtCore.QSize(0, 35))
        self.actionOdjava.setMaximumSize(QtCore.QSize(60, 36))
        self.actionOdjava.setSizeIncrement(QtCore.QSize(0, 0))
        self.actionOdjava.setObjectName("actionOdjava")
        self.actionOdjava.released.connect(self.odjava)
        self.layZaglavlje.addWidget(self.actionOdjava)
        self.layGlavnaFormaVertikalno.addLayout(self.layZaglavlje)
        if self.korisnikID == 1:
            self.actionKorisnici = QtWidgets.QPushButton(frmGlavna)
            self.actionKorisnici.setObjectName("actionKorisnici")
            self.actionKorisnici.setText("Korisnici")
            self.actionKorisnici.released.connect(self.prikaziKorisnike)
            self.layZaglavlje.addWidget(self.actionKorisnici)
            self.actionOdjeca = QtWidgets.QPushButton(frmGlavna)
            self.actionOdjeca.setObjectName("actionOdjeca")
            self.actionOdjeca.setText("Odjeća")
            self.actionOdjeca.released.connect(self.prikaziOdjecu)
            self.actionOdjeca.released.connect(self.prikaziOdjecu)
            self.layZaglavlje.addWidget(self.actionOdjeca)
        self.layTijeloAplikacije = QtWidgets.QHBoxLayout()
        self.layTijeloAplikacije.setObjectName("layTijeloAplikacije")
        self.tbWidgetPopisOdjece = QtWidgets.QTabWidget(frmGlavna)
        self.tbWidgetPopisOdjece.setMinimumSize(QtCore.QSize(712, 500))
        self.tbWidgetPopisOdjece.setMaximumSize(QtCore.QSize(743, 600))
        self.tbWidgetPopisOdjece.setObjectName("tbWidgetPopisOdjece")
        self.tbWidgetPopisOdjece.setTabBar(VertikalniTab.VertikalniTab(width=100, height=50))

        # Aktualno
        self.Aktualno = QtWidgets.QWidget()
        self.Aktualno.setObjectName("Aktualno")
        self.horizontalLayoutAktualno = QtWidgets.QHBoxLayout(self.Aktualno)
        self.horizontalLayoutAktualno.setObjectName("horizontalLayoutAktualno")
        self.kreirajWidgetOdjecaAktualno()
        # Zenska odjeca
        self.Zenska = QtWidgets.QWidget()
        self.Zenska.setObjectName("Zenska")
        self.horizontalLayoutZenska = QtWidgets.QHBoxLayout(self.Zenska)
        self.horizontalLayoutZenska.setObjectName("horizontalLayoutZenska")
        self.kreirajWidgetOdjecaZenska()
        # Muska odjeca
        self.Muska = QtWidgets.QWidget()
        self.Muska.setObjectName("Muska")
        self.horizontalLayoutMuska = QtWidgets.QHBoxLayout(self.Muska)
        self.horizontalLayoutMuska.setObjectName("horizontalLayoutMuska")
        self.kreirajWidgetOdjecaMuska()
        # Djecija odjeca
        self.Djecja = QtWidgets.QWidget()
        self.Djecja.setObjectName("Djecja")
        self.horizontalLayoutDjeca = QtWidgets.QHBoxLayout(self.Djecja)
        self.horizontalLayoutDjeca.setObjectName("horizontalLayoutDjeca")
        self.kreirajWidgetOdjecaDjeca()

        self.tbWidgetPopisOdjece.addTab(self.Aktualno, "Aktualno")
        self.tbWidgetPopisOdjece.addTab(self.Muska, "Muška Odjeća")
        self.tbWidgetPopisOdjece.addTab(self.Djecja, "Dječja odjeća")
        self.tbWidgetPopisOdjece.addTab(self.Zenska, "Ženska odjeća")
        self.tbWidgetPopisOdjece.setTabPosition(QtWidgets.QTabWidget.West)
        self.tbWidgetPopisOdjece.setCurrentIndex(0)



        self.kreirajKosaricu(frmGlavna)

        self.layGlavnaFormaVertikalno.addLayout(self.layTijeloAplikacije)
        self.layGlavnaForma.addLayout(self.layGlavnaFormaVertikalno)

        self.retranslateUi(frmGlavna)
        self.tbWidgetPopisOdjece.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmGlavna)


    def retranslateUi(self, frmGlavna):
        _translate = QtCore.QCoreApplication.translate
        frmGlavna.setWindowTitle(_translate("frmGlavna", "Form"))
        self.lblNazivAplikacije.setText(_translate("frmGlavna", "<html><head/><body><p><span style=\" font-size:26pt;\">Shopping App</span></p></body></html>"))
        self.actionOdjava.setText(_translate("frmGlavna", "Odjava"))
        self.lblKosarica.setText(_translate("frmGlavna", "<html><head/><body><p><span style=\" font-size:22pt;\">Košarica</span></p></body></html>"))

    def kreirajWidgetOdjecaMuska(self):
        self.scrollAreaMuska = QtWidgets.QScrollArea(self.Muska)
        self.scrollAreaMuska.setWidgetResizable(True)
        self.scrollAreaMuska.setObjectName("scrollArea")
        self.scrollAreaMuskiWidget = QtWidgets.QWidget()
        self.scrollAreaMuskiWidget.setGeometry(QtCore.QRect(0, 0, 586, 554))
        self.scrollAreaMuskiWidget.setObjectName("scrollAreaMuski")
        self.verticalLayoutMuski = QtWidgets.QVBoxLayout(self.scrollAreaMuskiWidget)
        self.verticalLayoutMuski.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutMuski.setObjectName("verticalLayoutMuski")
        self.gridLayoutMuski = QtWidgets.QGridLayout()
        self.gridLayoutMuski.setObjectName("gridLayoutMuski")
        self.prikaziOdjecuMuska()
        self.verticalLayoutMuski.addLayout(self.gridLayoutMuski)
        self.scrollAreaMuska.setWidget(self.scrollAreaMuskiWidget)
        self.horizontalLayoutMuska.addWidget(self.scrollAreaMuska)

    def kreirajWidgetOdjecaZenska(self):
        self.scrollAreaZenska = QtWidgets.QScrollArea(self.Zenska)
        self.scrollAreaZenska.setWidgetResizable(True)
        self.scrollAreaZenska.setObjectName("scrollAreaZenska")
        self.scrollAreaZenskiWidget = QtWidgets.QWidget()
        self.scrollAreaZenskiWidget.setGeometry(QtCore.QRect(0, 0, 586, 554))
        self.scrollAreaZenskiWidget.setObjectName("scrollAreaZenski")
        self.verticalLayoutZenski = QtWidgets.QVBoxLayout(self.scrollAreaZenskiWidget)
        self.verticalLayoutZenski.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutZenski.setObjectName("verticalLayoutZenski")
        self.gridLayoutZenski = QtWidgets.QGridLayout()
        self.gridLayoutZenski.setObjectName("gridLayoutZenski")
        self.prikaziOdjecuZenska()
        self.verticalLayoutZenski.addLayout(self.gridLayoutZenski)
        self.scrollAreaZenska.setWidget(self.scrollAreaZenskiWidget)
        self.horizontalLayoutZenska.addWidget(self.scrollAreaZenska)

    def kreirajWidgetOdjecaDjeca(self):
        self.scrollAreaDjeca = QtWidgets.QScrollArea(self.Djecja)
        self.scrollAreaDjeca.setWidgetResizable(True)
        self.scrollAreaDjeca.setObjectName("scrollArea")
        self.scrollAreaDjecaWidget = QtWidgets.QWidget()
        self.scrollAreaDjecaWidget.setGeometry(QtCore.QRect(0, 0, 586, 554))
        self.scrollAreaDjecaWidget.setObjectName("scrollAreaDjeca")
        self.verticalLayoutDjeca = QtWidgets.QVBoxLayout(self.scrollAreaDjecaWidget)
        self.verticalLayoutDjeca.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutDjeca.setObjectName("verticalLayoutDjeca")
        self.gridLayoutDjeca = QtWidgets.QGridLayout()
        self.gridLayoutDjeca.setObjectName("gridLayoutDjeca")
        self.prikaziOdjecuDjeca()
        self.verticalLayoutDjeca.addLayout(self.gridLayoutDjeca)
        self.scrollAreaDjeca.setWidget(self.scrollAreaDjecaWidget)
        self.horizontalLayoutDjeca.addWidget(self.scrollAreaDjeca)
        self.layTijeloAplikacije.addWidget(self.tbWidgetPopisOdjece)

    def kreirajWidgetOdjecaAktualno(self):
        self.scrollAreaAktualno = QtWidgets.QScrollArea(self.Aktualno)
        self.scrollAreaAktualno.setWidgetResizable(True)
        self.scrollAreaAktualno.setObjectName("scrollAreaAktualno")
        self.scrollAreaAktualnoWidget = QtWidgets.QWidget()
        self.scrollAreaAktualnoWidget.setGeometry(QtCore.QRect(0, 0, 586, 554))
        self.scrollAreaAktualnoWidget.setObjectName("scrollAreaAktualno")
        self.verticalLayoutAktualno = QtWidgets.QVBoxLayout(self.scrollAreaAktualnoWidget)
        self.verticalLayoutAktualno.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutAktualno.setObjectName("verticalLayoutAktualno")
        self.gridLayoutAktualno = QtWidgets.QGridLayout()
        self.gridLayoutAktualno.setObjectName("gridLayoutAktualno")
        self.prikaziAktualnuOdjecu()
        self.verticalLayoutAktualno.addLayout(self.gridLayoutAktualno)
        self.scrollAreaAktualno.setWidget(self.scrollAreaAktualnoWidget)
        self.horizontalLayoutAktualno.addWidget(self.scrollAreaAktualno)

    def kreirajKosaricu(self, frmGlavna):
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblKosarica = QtWidgets.QLabel(frmGlavna)
        self.lblKosarica.setMaximumSize(QtCore.QSize(300, 35))
        self.lblKosarica.setMinimumSize(QtCore.QSize(300, 35))
        self.lblKosarica.setAlignment(QtCore.Qt.AlignCenter)
        self.lblKosarica.setObjectName("lblKosarica")
        self.verticalLayout_3.addWidget(self.lblKosarica)
        self.listWidget = QtWidgets.QListWidget(frmGlavna)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_3.addWidget(self.listWidget)
        self.actionKupi = QtWidgets.QPushButton(frmGlavna)
        self.actionKupi.setMinimumSize(QtCore.QSize(0, 40))
        self.actionKupi.setObjectName("actionKupi")
        self.actionKupi.setText("Kupi")
        self.actionKupi.released.connect(self.kupi)
        self.verticalLayout_3.addWidget(self.actionKupi)
        self.actionObrisiSve = QtWidgets.QPushButton(frmGlavna)
        self.actionObrisiSve.setMinimumSize(QtCore.QSize(0, 40))
        self.actionObrisiSve.setObjectName("actionObrisiSve")
        self.actionObrisiSve.setText("Obrisi")
        self.actionObrisiSve.released.connect(self.izbrisiSve)
        self.verticalLayout_3.addWidget(self.actionObrisiSve)
        self.layTijeloAplikacije.addLayout(self.verticalLayout_3)


    def prikaziOdjecuZenska(self):
        self.odjeca = Odjeca.Odjeca()
        zenskaOdjeca = self.odjeca.dohvatiOdjecuSpol(2)
        red = 0
        for komadOdjece in zenskaOdjeca:
            kolicinaOdjece = self.odjeca.dohvatiRaspolozivuKolicinuKomadaOdjece(komadOdjece[0])
            self.ispisiOdjecuZenska(komadOdjece, kolicinaOdjece[0][0])
            self.gridLayoutZenski.addWidget(self.widget1, red, 0, 1, 1)
            red +=1

    def prikaziOdjecuMuska(self):
        self.odjeca = Odjeca.Odjeca()
        muskaOdjeca = self.odjeca.dohvatiOdjecuSpol(1)
        red = 0
        for komadOdjece in muskaOdjeca:
            kolicinaOdjece = self.odjeca.dohvatiRaspolozivuKolicinuKomadaOdjece(komadOdjece[0])
            self.ispisiOdjecuMuska(komadOdjece, kolicinaOdjece[0][0])
            self.gridLayoutMuski.addWidget(self.widget2, red, 0, 1, 1)
            red += 1

    def prikaziOdjecuDjeca(self):
        self.odjeca = Odjeca.Odjeca()
        djecjaOdjeca = self.odjeca.dohvatiOdjecuSpol(3)
        red = 0
        poljeWidget3 = []
        for komadOdjece in djecjaOdjeca:
            kolicinaOdjece = self.odjeca.dohvatiRaspolozivuKolicinuKomadaOdjece(komadOdjece[0])
            self.ispisiOdjecuDjeca(komadOdjece, kolicinaOdjece[0][0])
            self.gridLayoutDjeca.addWidget(self.widget3, red, 0, 1, 1)
            red += 1
            poljeWidget3.append(self.widget3)

    def prikaziAktualnuOdjecu(self):
        self.odjeca = Odjeca.Odjeca()
        aktualnaOdjeca = self.odjeca.dohvatiAktualnePodatke()
        red = 0
        for komadOdjece in aktualnaOdjeca:
            kolicinaOdjece = self.odjeca.dohvatiRaspolozivuKolicinuKomadaOdjece(komadOdjece[0])
            self.ispisiOdjecuAktualna(komadOdjece, kolicinaOdjece[0][0])
            self.gridLayoutAktualno.addWidget(self.widget4, red, 0, 1, 1)
            red += 1

    def ispisiOdjecuZenska (self, komadOdjece, kolicina):
        self.widget1 = QtWidgets.QWidget(self.scrollAreaZenskiWidget)
        self.widget1.setMinimumSize(QtCore.QSize(566, 220))
        self.widget1.setMaximumSize(QtCore.QSize(566, 220))
        self.widget1.setObjectName("widget1")
        self.horizontalLayoutZenskaOdjeca = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayoutZenskaOdjeca.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutZenskaOdjeca.setObjectName("horizontalLayout_7")
        self.horizontalLayoutwidget1 = QtWidgets.QHBoxLayout()
        self.horizontalLayoutwidget1.setObjectName("horizontalLayoutwidget1")
        self.labelslikawidget1 = QtWidgets.QLabel(self.widget1)
        self.labelslikawidget1.setMinimumSize(QtCore.QSize(300, 200))
        self.labelslikawidget1.setMaximumSize(QtCore.QSize(300, 200))
        self.labelslikawidget1.setObjectName("labelslikawidget1")
        pixmap = QPixmap(komadOdjece[5])
        self.labelslikawidget1.setPixmap(pixmap)
        self.horizontalLayoutwidget1.addWidget(self.labelslikawidget1)
        self.verticalLayoutwidget1 = QtWidgets.QVBoxLayout()
        self.verticalLayoutwidget1.setObjectName("verticalLayoutwidget1")
        self.horizontalLayoutZenskaOdjecaCijenaPopust = QtWidgets.QHBoxLayout()
        self.horizontalLayoutZenskaOdjecaCijenaPopust.setObjectName("horizontalLayout_4")
        self.lblCijenaWidget1 = QtWidgets.QLabel(self.widget1)
        self.lblCijenaWidget1.setMinimumSize(QtCore.QSize(115, 50))
        self.lblCijenaWidget1.setMaximumSize(QtCore.QSize(115, 50))
        self.lblCijenaWidget1.setObjectName("lblCijenaWidget1")
        self.lblCijenaWidget1.setText(str(komadOdjece[1]) + ",00 kn")
        self.horizontalLayoutZenskaOdjecaCijenaPopust.addWidget(self.lblCijenaWidget1)
        self.lblPopustWidget1 = QtWidgets.QLabel(self.widget1)
        self.lblPopustWidget1.setMaximumSize(QtCore.QSize(115, 50))
        self.lblPopustWidget1.setSizeIncrement(QtCore.QSize(115, 50))
        self.lblPopustWidget1.setObjectName("lblPopustWidget1")
        if komadOdjece[3] != 10:
            self.lblPopustWidget1.setText("-" + str(komadOdjece[3] * 10) + "%")
        self.horizontalLayoutZenskaOdjecaCijenaPopust.addWidget(self.lblPopustWidget1)
        self.verticalLayoutwidget1.addLayout(self.horizontalLayoutZenskaOdjecaCijenaPopust)
        self.lblNazivWidget1 = QtWidgets.QLabel(self.widget1)
        self.lblNazivWidget1.setMinimumSize(QtCore.QSize(238, 53))
        self.lblNazivWidget1.setMaximumSize(QtCore.QSize(238, 53))
        self.lblNazivWidget1.setObjectName("lblNazivWidget1")
        self.lblNazivWidget1.setText(komadOdjece[2])
        self.verticalLayoutwidget1.addWidget(self.lblNazivWidget1)
        self.lblRaspolozivaKolicinaWidget1 = QtWidgets.QLabel(self.widget1)
        self.lblRaspolozivaKolicinaWidget1.setMinimumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaKolicinaWidget1.setMaximumSize(QtCore.QSize(238, 52))
        if kolicina == 0:
            self.lblRaspolozivaKolicinaWidget1.setText("Trenutno nema odjeće na skladištu")
            self.lblRaspolozivaKolicinaWidget1.setStyleSheet('color: rgb(255, 0, 0);')

        else:
            self.lblRaspolozivaKolicinaWidget1.setText("Raspoloziva kolicina: " + str(kolicina))
            self.lblRaspolozivaKolicinaWidget1.setStyleSheet('color: rgb(0, 200, 50);')
        self.lblRaspolozivaKolicinaWidget1.setObjectName("lblRaspolozivaKolicinaWidget1")
        self.verticalLayoutwidget1.addWidget(self.lblRaspolozivaKolicinaWidget1)
        self.lblRaspolozivaVelicinaWidget1 = QtWidgets.QLabel(self.widget1)
        self.lblRaspolozivaVelicinaWidget1.setMinimumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaVelicinaWidget1.setMaximumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaVelicinaWidget1.setObjectName("lblRaspolozivaKolicinaWidget1")

        odjeca = Odjeca.Odjeca()

        raspoloziveVelicine = odjeca.dohvatiRaspoloziveKolicine(komadOdjece[0])
        raspolozivaVelicina = "Raspoloziva veličina: "
        t = 0
        for i in raspoloziveVelicine:
            raspolozivaVelicina += " ".join(raspoloziveVelicine[t]) + " "
            t += 1
        self.lblRaspolozivaVelicinaWidget1.setText(raspolozivaVelicina)
        self.verticalLayoutwidget1.addWidget(self.lblRaspolozivaVelicinaWidget1)
        self.actionDodajUKosaricuWidget1 = QtWidgets.QPushButton("Dodaj u košaricu",self.widget1)
        self.actionDodajUKosaricuWidget1.setMinimumSize(QtCore.QSize(238, 23))
        self.actionDodajUKosaricuWidget1.setMaximumSize(QtCore.QSize(238, 23))
        self.actionDodajUKosaricuWidget1.setObjectName(str(komadOdjece[0]))
        self.actionDodajUKosaricuWidget1.released.connect(self.dodajUListuKosarica)
        self.actionOdaberiVelicinuWidget1 = QtWidgets.QPushButton("Odaberi veličinu", self.widget1)
        self.actionOdaberiVelicinuWidget1.setObjectName(str(komadOdjece[0]))
        self.actionOdaberiVelicinuWidget1.released.connect(self.odaberiKolicinu)
        self.verticalLayoutwidget1.addWidget(self.actionOdaberiVelicinuWidget1)
        self.verticalLayoutwidget1.addWidget(self.actionDodajUKosaricuWidget1)
        self.horizontalLayoutwidget1.addLayout(self.verticalLayoutwidget1)
        self.horizontalLayoutZenskaOdjeca.addLayout(self.horizontalLayoutwidget1)



    def ispisiOdjecuMuska(self, komadOdjece, kolicina):
        self.widget2 = QtWidgets.QWidget(self.scrollAreaMuskiWidget)
        self.widget2.setMinimumSize(QtCore.QSize(566, 220))
        self.widget2.setMaximumSize(QtCore.QSize(566, 220))
        self.widget2.setObjectName("widget2")

        self.horizontalLayoutMuskaOdjeca = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayoutMuskaOdjeca.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutMuskaOdjeca.setObjectName("horizontalLayoutMuskaOdjeca")
        self.horizontalLayoutwidget2 = QtWidgets.QHBoxLayout()
        self.horizontalLayoutwidget2.setObjectName("horizontalLayoutwidget1")
        self.labelslikawidget2 = QtWidgets.QLabel(self.widget2)
        self.labelslikawidget2.setMinimumSize(QtCore.QSize(300, 200))
        self.labelslikawidget2.setMaximumSize(QtCore.QSize(300, 200))
        self.labelslikawidget2.setObjectName("labelslikawidget2")
        pixmap = QPixmap(komadOdjece[5])
        self.labelslikawidget2.setPixmap(pixmap)
        self.horizontalLayoutwidget2.addWidget(self.labelslikawidget2)
        self.verticalLayoutwidget2 = QtWidgets.QVBoxLayout()
        self.verticalLayoutwidget2.setObjectName("verticalLayoutwidget1")
        self.horizontalLayoutMuskaOdjecaCijenaPopust = QtWidgets.QHBoxLayout()
        self.horizontalLayoutMuskaOdjecaCijenaPopust.setObjectName("horizontalLayoutCP")
        self.lblCijenaWidget2 = QtWidgets.QLabel(self.widget2)
        self.lblCijenaWidget2.setMinimumSize(QtCore.QSize(115, 50))
        self.lblCijenaWidget2.setMaximumSize(QtCore.QSize(115, 50))
        self.lblCijenaWidget2.setObjectName("lblCijenaWidget1")
        self.lblCijenaWidget2.setText(str(komadOdjece[1]) + ",00 kn")
        self.horizontalLayoutMuskaOdjecaCijenaPopust.addWidget(self.lblCijenaWidget2)
        self.lblPopustWidget2 = QtWidgets.QLabel(self.widget2)
        self.lblPopustWidget2.setMaximumSize(QtCore.QSize(115, 50))
        self.lblPopustWidget2.setSizeIncrement(QtCore.QSize(115, 50))
        self.lblPopustWidget2.setObjectName("lblPopustWidget1")
        self.horizontalLayoutMuskaOdjecaCijenaPopust.addWidget(self.lblPopustWidget2)
        self.verticalLayoutwidget2.addLayout(self.horizontalLayoutMuskaOdjecaCijenaPopust)
        self.lblNazivWidget2 = QtWidgets.QLabel(self.widget2)
        self.lblNazivWidget2.setText(komadOdjece[2])
        self.lblNazivWidget2.setMinimumSize(QtCore.QSize(238, 53))
        self.lblNazivWidget2.setMaximumSize(QtCore.QSize(238, 53))
        self.lblNazivWidget2.setObjectName("lblNazivWidget1")
        if komadOdjece[3] != 10:
            self.lblPopustWidget2.setText("-" + str(komadOdjece[3] * 10) + "%")
        self.verticalLayoutwidget2.addWidget(self.lblNazivWidget2)
        self.lblRaspolozivaKolicinaWidget2 = QtWidgets.QLabel(self.widget2)
        self.lblRaspolozivaKolicinaWidget2.setMinimumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaKolicinaWidget2.setMaximumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaKolicinaWidget2.setObjectName("lblRaspolozivaKolicinaWidget2")
        if kolicina == 0:
            self.lblRaspolozivaKolicinaWidget2.setText("Trenutno nema odjeće na skladištu")
            self.lblRaspolozivaKolicinaWidget2.setStyleSheet('color: rgb(255, 0, 0);')

        else:
            self.lblRaspolozivaKolicinaWidget2.setText("Raspoloziva kolicina: " + str(kolicina))
            self.lblRaspolozivaKolicinaWidget2.setStyleSheet('color: rgb(0, 200, 50);')
        self.verticalLayoutwidget2.addWidget(self.lblRaspolozivaKolicinaWidget2)
        self.lblRaspolozivaVelicinaWidget2 = QtWidgets.QLabel(self.widget2)
        self.lblRaspolozivaVelicinaWidget2.setMinimumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaVelicinaWidget2.setMaximumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaVelicinaWidget2.setObjectName("lblRaspolozivaKolicinaWidget1")
        odjeca = Odjeca.Odjeca()

        raspoloziveVelicine = odjeca.dohvatiRaspoloziveKolicine(komadOdjece[0])
        raspolozivaVelicina = "Raspoloziva veličina: "
        t = 0
        for i in raspoloziveVelicine:
            raspolozivaVelicina += " ".join(raspoloziveVelicine[t]) + " "
            t += 1
        self.lblRaspolozivaVelicinaWidget2.setText(raspolozivaVelicina)
        self.verticalLayoutwidget2.addWidget(self.lblRaspolozivaVelicinaWidget2)
        self.actionDodajUKosaricuWidget2 = QtWidgets.QPushButton("Dodaj u košaricu",self.widget2)
        self.actionDodajUKosaricuWidget2.setMinimumSize(QtCore.QSize(238, 23))
        self.actionDodajUKosaricuWidget2.setMaximumSize(QtCore.QSize(238, 23))
        self.actionDodajUKosaricuWidget2.setObjectName(str(komadOdjece[0]))
        self.actionDodajUKosaricuWidget2.released.connect(self.dodajUListuKosarica)
        self.actionOdaberiVelicinuWidget2 = QtWidgets.QPushButton("Odaberi veličinu", self.widget2)
        self.actionOdaberiVelicinuWidget2.setObjectName(str(komadOdjece[0]))
        self.actionOdaberiVelicinuWidget2.released.connect(self.odaberiKolicinu)
        self.verticalLayoutwidget2.addWidget(self.actionOdaberiVelicinuWidget2)
        self.verticalLayoutwidget2.addWidget(self.actionDodajUKosaricuWidget2)
        self.horizontalLayoutwidget2.addLayout(self.verticalLayoutwidget2)
        self.horizontalLayoutMuskaOdjeca.addLayout(self.horizontalLayoutwidget2)

    def ispisiOdjecuDjeca(self, komadOdjece, kolicina):
        self.widget3 = QtWidgets.QWidget(self.scrollAreaDjecaWidget)
        self.widget3.setMinimumSize(QtCore.QSize(566, 220))
        self.widget3.setMaximumSize(QtCore.QSize(566, 220))
        self.widget3.setObjectName("widget3")
        self.horizontalLayoutDjecaOdjeca = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayoutDjecaOdjeca.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutDjecaOdjeca.setObjectName("horizontalLayoutMuskaOdjeca")
        self.horizontalLayoutwidget3 = QtWidgets.QHBoxLayout()
        self.horizontalLayoutwidget3.setObjectName("horizontalLayoutwidget1")
        self.labelslikawidget3 = QtWidgets.QLabel(self.widget3)
        self.labelslikawidget3.setMinimumSize(QtCore.QSize(300, 200))
        self.labelslikawidget3.setMaximumSize(QtCore.QSize(300, 200))
        self.labelslikawidget3.setObjectName("labelslikawidget2")
        pixmap = QPixmap(komadOdjece[5])
        self.labelslikawidget3.setPixmap(pixmap)
        self.horizontalLayoutwidget3.addWidget(self.labelslikawidget3)
        self.verticalLayoutwidget3 = QtWidgets.QVBoxLayout()
        self.verticalLayoutwidget3.setObjectName("verticalLayoutwidget1")
        self.horizontalLayoutMuskaOdjecaCijenaPopust = QtWidgets.QHBoxLayout()
        self.horizontalLayoutMuskaOdjecaCijenaPopust.setObjectName("horizontalLayoutCP")
        self.lblCijenaWidget3 = QtWidgets.QLabel(self.widget3)
        self.lblCijenaWidget3.setMinimumSize(QtCore.QSize(115, 50))
        self.lblCijenaWidget3.setMaximumSize(QtCore.QSize(115, 50))
        self.lblCijenaWidget3.setObjectName("lblCijenaWidget1")
        self.lblCijenaWidget3.setText(str(komadOdjece[1])+ ",00 kn")
        self.horizontalLayoutMuskaOdjecaCijenaPopust.addWidget(self.lblCijenaWidget3)
        self.lblPopustWidget3 = QtWidgets.QLabel(self.widget3)
        self.lblPopustWidget3.setMaximumSize(QtCore.QSize(115, 50))
        self.lblPopustWidget3.setSizeIncrement(QtCore.QSize(115, 50))
        self.lblPopustWidget3.setObjectName("lblPopustWidget1")
        if komadOdjece[3] != 10:
            self.lblPopustWidget3.setText("-" + str(komadOdjece[3] * 10) + "%")
        self.horizontalLayoutMuskaOdjecaCijenaPopust.addWidget(self.lblPopustWidget3)
        self.verticalLayoutwidget3.addLayout(self.horizontalLayoutMuskaOdjecaCijenaPopust)
        self.lblNazivWidget3 = QtWidgets.QLabel(self.widget3)
        self.lblNazivWidget3.setMinimumSize(QtCore.QSize(238, 53))
        self.lblNazivWidget3.setMaximumSize(QtCore.QSize(238, 53))
        self.lblNazivWidget3.setObjectName("lblNazivWidget1")
        self.lblNazivWidget3.setText(komadOdjece[2])
        self.verticalLayoutwidget3.addWidget(self.lblNazivWidget3)
        self.lblRaspolozivaKolicinaWidget3 = QtWidgets.QLabel(self.widget3)
        self.lblRaspolozivaKolicinaWidget3.setMinimumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaKolicinaWidget3.setMaximumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaKolicinaWidget3.setObjectName("lblRaspolozivaKolicinaWidget3")
        if kolicina == 0:
            self.lblRaspolozivaKolicinaWidget3.setText("Trenutno nema odjeće na skladištu")
            self.lblRaspolozivaKolicinaWidget3.setStyleSheet('color: rgb(255, 0, 0);')
        else:
            self.lblRaspolozivaKolicinaWidget3.setText("Raspoloziva kolicina: " + str(kolicina))
            self.lblRaspolozivaKolicinaWidget3.setStyleSheet('color: rgb(0, 200, 50);')
        self.verticalLayoutwidget3.addWidget(self.lblRaspolozivaKolicinaWidget3)
        self.lblRaspolozivaVelicinaWidget3 = QtWidgets.QLabel(self.widget3)
        self.lblRaspolozivaVelicinaWidget3.setMinimumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaVelicinaWidget3.setMaximumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaVelicinaWidget3.setObjectName("lblRaspolozivaKolicinaWidget1")
        odjeca = Odjeca.Odjeca()

        raspolozivaKolicina = odjeca.dohvatiRaspoloziveKolicine(komadOdjece[0])
        raspolozivaVelicina = "Raspoloziva veličina: "
        t = 0
        for i in raspolozivaKolicina:
            raspolozivaVelicina+= " ".join(raspolozivaKolicina[t]) + " "
            t += 1
        self.lblRaspolozivaVelicinaWidget3.setText(raspolozivaVelicina)
        self.verticalLayoutwidget3.addWidget(self.lblRaspolozivaVelicinaWidget3)
        self.actionDodajUKosaricuWidget3 = QtWidgets.QPushButton("Dodaj u košaricu",self.widget3)
        self.actionDodajUKosaricuWidget3.setMinimumSize(QtCore.QSize(238, 23))
        self.actionDodajUKosaricuWidget3.setMaximumSize(QtCore.QSize(238, 23))
        self.actionDodajUKosaricuWidget3.setObjectName(str(komadOdjece[0]))
        self.actionDodajUKosaricuWidget3.released.connect(self.dodajUListuKosarica)
        self.actionOdaberiVelicinuWidget3 = QtWidgets.QPushButton("Odaberi veličinu", self.widget3)
        self.actionOdaberiVelicinuWidget3.setObjectName(str(komadOdjece[0]))
        self.actionOdaberiVelicinuWidget3.released.connect(self.odaberiKolicinu)
        self.verticalLayoutwidget3.addWidget(self.actionOdaberiVelicinuWidget3)
        self.verticalLayoutwidget3.addWidget(self.actionDodajUKosaricuWidget3)
        self.horizontalLayoutwidget3.addLayout(self.verticalLayoutwidget3)
        self.horizontalLayoutDjecaOdjeca.addLayout(self.horizontalLayoutwidget3)

    def ispisiOdjecuAktualna(self, komadOdjece, kolicina):
        self.widget4 = QtWidgets.QWidget(self.scrollAreaAktualnoWidget)
        self.widget4.setMinimumSize(QtCore.QSize(566, 220))
        self.widget4.setMaximumSize(QtCore.QSize(566, 220))
        self.widget4.setObjectName("widget4")
        self.horizontalLayoutAktualnoOdjeca = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayoutAktualnoOdjeca.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutAktualnoOdjeca.setObjectName("horizontalLayoutAktualnoOdjeca")
        self.horizontalLayoutwidget4 = QtWidgets.QHBoxLayout()
        self.horizontalLayoutwidget4.setObjectName("horizontalLayoutwidget1")
        self.labelslikawidget4 = QtWidgets.QLabel(self.widget4)
        self.labelslikawidget4.setMinimumSize(QtCore.QSize(300, 200))
        self.labelslikawidget4.setMaximumSize(QtCore.QSize(300, 200))
        self.labelslikawidget4.setObjectName("labelslikawidget4")
        pixmap = QPixmap(komadOdjece[5])
        self.labelslikawidget4.setPixmap(pixmap)
        self.horizontalLayoutwidget4.addWidget(self.labelslikawidget4)
        self.verticalLayoutwidget4 = QtWidgets.QVBoxLayout()
        self.verticalLayoutwidget4.setObjectName("verticalLayoutwidget4")
        self.horizontalLayoutAktualnoOdjecaCijenaPopust = QtWidgets.QHBoxLayout()
        self.horizontalLayoutAktualnoOdjecaCijenaPopust.setObjectName("horizontalLayoutCP4")
        self.lblCijenaWidget4 = QtWidgets.QLabel(self.widget4)
        self.lblCijenaWidget4.setMinimumSize(QtCore.QSize(115, 50))
        self.lblCijenaWidget4.setMaximumSize(QtCore.QSize(115, 50))
        self.lblCijenaWidget4.setObjectName("lblCijenaWidget4")
        self.lblCijenaWidget4.setText(str(komadOdjece[1]) + ",00 kn")
        self.horizontalLayoutAktualnoOdjecaCijenaPopust.addWidget(self.lblCijenaWidget4)
        self.lblPopustWidget4 = QtWidgets.QLabel(self.widget4)
        self.lblPopustWidget4.setMaximumSize(QtCore.QSize(115, 50))
        self.lblPopustWidget4.setSizeIncrement(QtCore.QSize(115, 50))
        self.lblPopustWidget4.setObjectName("lblPopustWidget1")
        if komadOdjece[3] != 10:
            self.lblPopustWidget4.setText("-" + str(komadOdjece[3] * 10) + "%")
        self.horizontalLayoutAktualnoOdjecaCijenaPopust.addWidget(self.lblPopustWidget4)
        self.verticalLayoutwidget4.addLayout(self.horizontalLayoutAktualnoOdjecaCijenaPopust)
        self.lblNazivWidget4 = QtWidgets.QLabel(self.widget4)
        self.lblNazivWidget4.setMinimumSize(QtCore.QSize(238, 53))
        self.lblNazivWidget4.setMaximumSize(QtCore.QSize(238, 53))
        self.lblNazivWidget4.setObjectName("lblNazivWidget4")
        self.lblNazivWidget4.setText(komadOdjece[2])
        self.verticalLayoutwidget4.addWidget(self.lblNazivWidget4)
        self.lblRaspolozivaKolicinaWidget4 = QtWidgets.QLabel(self.widget4)
        self.lblRaspolozivaKolicinaWidget4.setMinimumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaKolicinaWidget4.setMaximumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaKolicinaWidget4.setObjectName("lblRaspolozivaKolicinaWidget4")
        if kolicina == 0:
            self.lblRaspolozivaKolicinaWidget4.setText("Trenutno nema odjeće na skladištu")
            self.lblRaspolozivaKolicinaWidget4.setStyleSheet('color: rgb(255, 0, 0);')

        else:
            self.lblRaspolozivaKolicinaWidget4.setText("Raspoloziva kolicina: " + str(kolicina))
            self.lblRaspolozivaKolicinaWidget4.setStyleSheet('color: rgb(0, 200, 50);')
        self.verticalLayoutwidget4.addWidget(self.lblRaspolozivaKolicinaWidget4)
        self.lblRaspolozivaVelicinaWidget4 = QtWidgets.QLabel(self.widget4)
        self.lblRaspolozivaVelicinaWidget4.setMinimumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaVelicinaWidget4.setMaximumSize(QtCore.QSize(238, 52))
        self.lblRaspolozivaVelicinaWidget4.setObjectName("lblRaspolozivaVelicinaWidget4")
        odjeca = Odjeca.Odjeca()

        raspolozivaKolicina = odjeca.dohvatiRaspoloziveKolicine(komadOdjece[0])
        raspolozivaVelicina = "Raspoloziva veličina: "
        t = 0
        for i in raspolozivaKolicina:
            raspolozivaVelicina += " ".join(raspolozivaKolicina[t]) + " "
            t += 1
        self.lblRaspolozivaVelicinaWidget4.setText(raspolozivaVelicina)
        self.verticalLayoutwidget4.addWidget(self.lblRaspolozivaVelicinaWidget4)
        self.actionDodajUKosaricuWidget4 = QtWidgets.QPushButton("Dodaj u košaricu", self.widget4)
        self.actionDodajUKosaricuWidget4.setMinimumSize(QtCore.QSize(238, 23))
        self.actionDodajUKosaricuWidget4.setMaximumSize(QtCore.QSize(238, 23))
        self.actionDodajUKosaricuWidget4.setObjectName(str(komadOdjece[0]))
        self.actionDodajUKosaricuWidget4.released.connect(self.dodajUListuKosarica)
        self.actionOdaberiVelicinuWidget4 = QtWidgets.QPushButton("Odaberi veličinu", self.widget4)
        self.actionOdaberiVelicinuWidget4.setObjectName(str(komadOdjece[0]))
        self.actionOdaberiVelicinuWidget4.released.connect(self.odaberiKolicinu)
        self.verticalLayoutwidget4.addWidget(self.actionOdaberiVelicinuWidget4)

        self.verticalLayoutwidget4.addWidget(self.actionDodajUKosaricuWidget4)
        self.horizontalLayoutwidget4.addLayout(self.verticalLayoutwidget4)
        self.horizontalLayoutAktualnoOdjeca.addLayout(self.horizontalLayoutwidget4)

    def odaberiKolicinu(self):
        #zabrani prikazivanje ako nema dovoljno komada odjece!
        odjeca = Odjeca.Odjeca()
        sending_button = self.sender()
        odjecaID = int(sending_button.objectName())
        raspolozivaKolicina = odjeca.dohvatiRaspolozivuKolicinuKomadaOdjece(odjecaID)
        if int(raspolozivaKolicina[0][0]) > 0:
            global odabirVelicine
            odabirVelicine = ui_comboOdabir.Ui_frmOdabirVelicine(odjecaID, self.korisnikID)
            odabirVelicine.show()
        else:
            self.nemaRaspoloziveKolicine()


    def dodajUListuKosarica(self):
        odjeca = Odjeca.Odjeca()
        kursor = odjeca.dohvatiSveIzKosarice(self.korisnikID)
        self.listWidget.clear()
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        for i in range(kursor.rowcount):
            row = kursor.fetchone()
            item = QtWidgets.QListWidgetItem()
            str1 = row[0]
            str2 = str(row[1]) + ",00 kn"
            str3 = row[2]
            str4 = str(row[3])
            item.setText(str1 + "  " + str2 + "    " + str3 + "    " + str4)
            self.listWidget.addItem(item)


    def izbrisiSve(self):
        kosarica = Kosarica.Kosarica()
        kosarica.IzbrisiSveIzKosarice(self.korisnikID)
        self.listWidget.clear()

    def odjava(self):
        global prijava
        prijava = ui_login.Ui_Prijava()
        prijava.show()
        self.close()

    def prikaziKorisnike(self):
        global korisnici
        korisnici = WigetAdministracijaKorisnika.WidgetAdministracijaKorisnika()
        korisnici.show()

    def prikaziOdjecu(self):
        global odjeca
        odjeca = ui_AdministracijaOdjeca.Ui_AdministracijaOdjeca()
        odjeca.show()


    def kupi(self):
        if(self.listWidget.count() != 0):
            odjeca = Odjeca.Odjeca()
            self.kupljeno()
            odjeca.unesiKupovinu(self.korisnikID)
            self.izbrisiSve()
            self.osvjeziAplikaciju()
        else:
            self.praznaKosarica()


    def kupljeno(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIconPixmap(QPixmap("success.png"))
        msgBox.setWindowTitle("Čestitam")
        msgBox.setText("Hvala vam na kupnji!")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def praznaKosarica(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle("Upozorenje")
        msgBox.setText("Nemate ništa u košarici!")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def kolicinaNijeOdabrana(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Upozorenje")
        msgBox.setText("Niste odabrali veličinu")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def nemaRaspoloziveKolicine(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Upozorenje")
        msgBox.setText("Trenutno nema raspoložive veličine na skladištu")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


    def osvjeziAplikaciju(self):
        self.scrollAreaAktualno.hide()
        self.scrollAreaDjeca.hide()
        self.scrollAreaMuska.hide()
        self.scrollAreaZenska.hide()
        self.lblKosarica.hide()
        self.listWidget.hide()
        self.actionKupi.hide()
        self.actionObrisiSve.hide()
        self.kreirajWidgetOdjecaMuska()
        self.kreirajWidgetOdjecaZenska()
        self.kreirajWidgetOdjecaDjeca()
        self.kreirajWidgetOdjecaAktualno()
        self.kreirajKosaricu(self)



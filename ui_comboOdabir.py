# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comboBox.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Odjeca
import ui_ShoppingApp
import Kosarica


class Ui_frmOdabirVelicine(QtWidgets.QWidget):
    def __init__(self, odjecaID, korisnikID):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.odjecaID = odjecaID
        self.korisnikID = korisnikID
        self.dohvatiVelicine()
    def setupUi(self, frmOdabirVelicine):
        frmOdabirVelicine.setObjectName("frmOdabirVelicine")
        frmOdabirVelicine.resize(203, 153)
        frmOdabirVelicine.setMinimumSize(QtCore.QSize(203, 153))
        frmOdabirVelicine.setMaximumSize(QtCore.QSize(203, 153))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(frmOdabirVelicine)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblOdabitVelicine = QtWidgets.QLabel(frmOdabirVelicine)
        self.lblOdabitVelicine.setObjectName("lblOdabitVelicine")
        self.horizontalLayout.addWidget(self.lblOdabitVelicine)
        self.cboxOdabirVelicine = QtWidgets.QComboBox(frmOdabirVelicine)
        self.cboxOdabirVelicine.setObjectName("cboxOdabirVelicine")
        self.horizontalLayout.addWidget(self.cboxOdabirVelicine)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.actionDodajUKosaricu = QtWidgets.QPushButton(frmOdabirVelicine)
        self.actionDodajUKosaricu.setObjectName("actionDodajUKosaricu")
        self.actionDodajUKosaricu.released.connect(self.odaberiVelicinu)
        self.verticalLayout.addWidget(self.actionDodajUKosaricu)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(frmOdabirVelicine)
        QtCore.QMetaObject.connectSlotsByName(frmOdabirVelicine)

    def retranslateUi(self, frmOdabirVelicine):
        _translate = QtCore.QCoreApplication.translate
        frmOdabirVelicine.setWindowTitle(_translate("frmOdabirVelicine", "Odabir veličine"))
        self.lblOdabitVelicine.setText(_translate("frmOdabirVelicine", "Odaberi veličinu: "))
        self.actionDodajUKosaricu.setText(_translate("frmOdabirVelicine", "Dodaj u košaricu"))

    def dohvatiVelicine(self):
        odjeca = Odjeca.Odjeca()
        raspolozivaVelicina = odjeca.dohvatiRaspoloziveKolicine(self.odjecaID)
        t = 0
        for i in raspolozivaVelicina:
            self.cboxOdabirVelicine.addItem(" ".join(raspolozivaVelicina[t]))
            t += 1

    def odaberiVelicinu(self):
        velicina = str(self.cboxOdabirVelicine.currentText())
        kosarica = Kosarica.Kosarica()
        odjeca = Odjeca.Odjeca()
        raspolozivaKolicinaOdjece = odjeca.dohvatiRaspolozivuKolicinuKomadaOdjecePoPojedinojVelicini(velicina, self.odjecaID)
        kolicinaUKosarici = kosarica.provjeriKolicinuOdjecePoVelicini(self.odjecaID, velicina)
        if kolicinaUKosarici:
            if int(raspolozivaKolicinaOdjece[0][0]) > int(kolicinaUKosarici[0][0]):
                kosarica.dodajUKosaricu(self.korisnikID, self.odjecaID, velicina)
            else:
                print("Nema dovoljno robe na skladistu")
        else:
            kosarica.dodajUKosaricu(self.korisnikID, self.odjecaID, velicina)

        self.close()

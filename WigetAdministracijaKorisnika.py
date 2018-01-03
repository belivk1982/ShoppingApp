from PyQt5 import QtWidgets, QtGui, QtCore
import  Korisnik
import ui_IzmjenaKorisnika

class WidgetAdministracijaKorisnika(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, AdministracijaKorisnika):
        AdministracijaKorisnika.setObjectName("AdministracijaKorisnika")
        AdministracijaKorisnika.resize(1176, 646)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AdministracijaKorisnika)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidgetKorisnici = QtWidgets.QTableWidget(AdministracijaKorisnika)
        self.tableWidgetKorisnici.setRowCount(5)
        self.tableWidgetKorisnici.setColumnCount(11)
        self.tableWidgetKorisnici.setObjectName("tableWidgetKorisnici")
        self.verticalLayout.addWidget(self.tableWidgetKorisnici)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonUredi = QtWidgets.QPushButton(AdministracijaKorisnika)
        self.pushButtonUredi.setObjectName("pushButtonUredi")
        self.pushButtonUredi.released.connect(self.promjeniKorisnika)
        self.horizontalLayout_2.addWidget(self.pushButtonUredi)
        self.pushButtonObrisi = QtWidgets.QPushButton(AdministracijaKorisnika)
        self.pushButtonObrisi.setObjectName("pushButtonObrisi")
        self.pushButtonObrisi.released.connect(self.obrisiKorisnika)
        self.horizontalLayout_2.addWidget(self.pushButtonObrisi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(AdministracijaKorisnika)
        QtCore.QMetaObject.connectSlotsByName(AdministracijaKorisnika)

        self.ispisKorisinka()

    def retranslateUi(self, AdministracijaKorisnika):
        _translate = QtCore.QCoreApplication.translate
        AdministracijaKorisnika.setWindowTitle(_translate("AdministracijaKorisnika", "Form"))
        self.pushButtonUredi.setText(_translate("AdministracijaKorisnika", "Uredi"))
        self.pushButtonObrisi.setText(_translate("AdministracijaKorisnika", "Obriši"))

    def ispisKorisinka(self):
        korisnik = Korisnik.Korisnik()
        sviKorsinici = korisnik.dohvatiSveKorisinike()
        self.tableWidgetKorisnici.setRowCount(0)
        for brojReda, podaciPoRedu in enumerate(sviKorsinici):
            self.tableWidgetKorisnici.insertRow(brojReda)
            for brojStupca, podaciPoStupcu in enumerate(podaciPoRedu):
                self.tableWidgetKorisnici.setItem(brojReda, brojStupca, QtWidgets.QTableWidgetItem(str(podaciPoStupcu)))
                print(str(podaciPoStupcu))

    def dohvatiKorisnike(self):
        listaPodatakaOKorisniku = []
        for i in range(11):
            listaPodatakaOKorisniku.append(self.tableWidgetKorisnici.item(self.tableWidgetKorisnici.currentRow(), i).text())
        return  listaPodatakaOKorisniku

    def obrisiKorisnika(self):
        korisnik = Korisnik.Korisnik()
        lista = self.dohvatiKorisnike()
        korisnik.obrisiKorisnika(int(lista[0]))
        self.ispisKorisinka()

    def promjeniKorisnika(self):
        global frmIzmjenaKorisnika
        frmIzmjenaKorisnika = ui_IzmjenaKorisnika.Ui_frmIzmjenaKorisnika(self.dohvatiKorisnike())
        frmIzmjenaKorisnika.show()


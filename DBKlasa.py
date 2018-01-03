#!/bin/python2
import MySQLdb
import Odjeca

class DBKlasa:
    def __init__(self):
        self.bazaPodataka = MySQLdb.connect(host = "localhost", user = "root", passwd = "root" ,db = "onlineshopping")
        self.kursor = self.bazaPodataka.cursor()

    def dohvatiPodatke(self, upit):
        self.upit = upit
        try:
            self.kursor.execute(self.upit)
            self.rezultat = self.kursor.fetchall()
            return self.rezultat
        except self.bazaPodataka.Error as e:
            print(e)
            self.rezultat = self.kursor.fetchone()
            return None
        #finally:
            #self.kursor.close()


    def UnesiPodatke(self, upit):
        kursor = self.bazaPodataka.cursor()
        self.upit = upit
        kursor.execute(self.upit)
        self.bazaPodataka.commit()
        kursor.close()

    def UnesiPodatkeOdjeca(self, upit):
        kursor = self.bazaPodataka.cursor()
        self.upit = upit
        kursor.execute(self.upit)
        idOdjeca = self.bazaPodataka.insert_id()
        self.bazaPodataka.commit()
        kursor.close()
        return idOdjeca

    def PrikaziPodatkeNaListi(self, upit):
        self.upit = upit
        kursor = self.bazaPodataka.cursor()
        kursor.execute(self.upit)
        return kursor

    def Izbrisi(self, upit):
        self.upit = upit
        kursor = self.bazaPodataka.cursor()
        kursor.execute(self.upit)
        self.bazaPodataka.commit()
        kursor.close()

    def unesiUTablicuKupioOdjecu(self, upit):
        odjeca = Odjeca.Odjeca()
        self.upit = upit
        kursor = self.bazaPodataka.cursor()
        kursor.execute(self.upit)

        for i in range(kursor.rowcount):
            kursor2 = self.bazaPodataka.cursor()
            row = kursor.fetchone()
            str1 = str(row[3])
            str2 = str(row[4])
            unos = "INSERT INTO kupio_odjecu VALUES("+str1+","+str2+",DEFAULT);"
            velicinaOdjece = odjeca.dohvatiVelicinuKupljeneOdjece(row[1])
            kolicina = 'UPDATE velicina_odjece SET kolicina = kolicina - '+ str(row[2]) +' WHERE odjecaID = ' + str(row[4]) + ' AND velicinaID = '+str(velicinaOdjece[0][0])+';'
            print(kolicina)
            kursor2.execute(unos)
            kursor2.execute(kolicina)
            self.bazaPodataka.commit()
        kursor.close()
        kursor2.close()








import DBKlasa

class Kosarica():
    def __init__(self):
        self.konekcijaNaBazu = DBKlasa.DBKlasa()

    def dodajUKosaricu(self, korisnikID, odjecaID, velicina):
        self.kID = korisnikID
        self.oID = odjecaID
        self.velicina = velicina
        self.upitProvjera = "SELECT 1 FROM kosarica WHERE korisnikID = "+str(self.kID)+" AND odjecaID ="+str(self.oID)+" AND velicina = "+"'"+self.velicina+"'"+";"
        provjera = self.konekcijaNaBazu.dohvatiPodatke(self.upitProvjera)
        if provjera:
            self.upit = 'UPDATE kosarica SET kolicina = kolicina + 1 WHERE odjecaID = '+str(self.oID)+' AND korisnikID = '+str(self.kID)+' AND velicina = '+'"'+self.velicina+'"'+';'
            self.konekcijaNaBazu.UnesiPodatke(self.upit)
        else:
            self.upit = 'INSERT INTO kosarica(korisnikID, odjecaID, velicina, kolicina) VALUES('+str(self.kID)+','+str(self.oID)+','+'"'+self.velicina+'",1'+');'
            self.konekcijaNaBazu.UnesiPodatke(self.upit)

    def IzbrisiSveIzKosarice(self, korisnikID):
        upit = 'DELETE FROM kosarica WHERE korisnikID = '+str(korisnikID)+';'
        self.konekcijaNaBazu.Izbrisi(upit)

    def provjeriKolicinuOdjecePoVelicini(self, odjecaID, velicina):
        upit = 'SELECT CAST(kolicina AS signed) FROM kosarica WHERE odjecaID = ' + str(odjecaID) + ' AND velicina = ' + '"' + velicina + '"' + ';'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita


import DBKlasa

class Odjeca():
    def __init__(self):
        self.konekcijaNaBazu = DBKlasa.DBKlasa()

    def dohvatiOdjecuSpol(self, spol):
        self.spol = spol
        upit = 'SELECT * FROM odjeca WHERE spolID = ' + str(self.spol) +';'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita

    def dohvatiAktualnePodatke(self):
        upit = 'SELECT * FROM odjeca WHERE snizenjeID != 10;'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita

    def dohvatiRaspoloziveKolicine(self, IDodjece):
        idOdjece = IDodjece
        upit = 'SELECT velicina.velicina FROM velicina JOIN velicina_odjece ON IDvelicina' \
               ' = velicinaID WHERE odjecaID = ' + str(idOdjece) + ' AND kolicina != 0;'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita

    def dohvatiOdjecuPoIdu(self, ID):
        idOdjece = ID
        upit = 'SELECT naziv, cijena FROM odjeca WHERE IDodjeca = '+ str(idOdjece) +';'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita

    def dohvatiSveIzKosarice(self, korisnikID):
        korID = korisnikID
        upit = 'SELECT odjeca.naziv, odjeca.cijena, kosarica.velicina , kosarica.kolicina FROM odjeca JOIN kosarica ' \
               'ON odjecaID = IDodjeca WHERE korisnikID = '+str(korID)+';'
        kursor = self.konekcijaNaBazu.PrikaziPodatkeNaListi(upit)
        return kursor

    def unesiKupovinu(self, korisnikID):
        upit = "SELECT * FROM kosarica WHERE korisnikID ="+str(korisnikID)+";"
        self.konekcijaNaBazu.unesiUTablicuKupioOdjecu(upit)

    def dohvatiOdjecu(self):
        upit = "SELECT odjeca.IDodjeca, odjeca.naziv, odjeca.cijena, odjeca.snizenjeID, (SELECT SUM(velicina_odjece.kolicina) FROM velicina_odjece WHERE velicina_odjece.odjecaID = odjeca.IDodjeca) AS kolicina FROM odjeca WHERE odjeca.odjecaObrisana = 0;"
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita

    def obrisiOdjecu(self, odjecaID):
        upit = "UPDATE odjeca set odjecaObrisana = 1 WHERE IDodjeca = " + str(odjecaID) + ";"
        self.konekcijaNaBazu.Izbrisi(upit)

    def unesiOdjecu(self, cijena, naziv, snizenjeID, spolID, slika, velicinaID, kolicina):
        upit = 'INSERT INTO odjeca VALUES(default,'+str(cijena)+','+'"'+str(naziv)+'"'+','+str(snizenjeID)+','+str(spolID)+','+'"'+str(slika)+'",'"0"');'
        idOdjeca = self.konekcijaNaBazu.UnesiPodatkeOdjeca(upit)
        self.unesiVelicinuIKolicinuOdjece(idOdjeca, velicinaID, kolicina)

    def unesiVelicinuIKolicinuOdjece(self, id, velicinaID, kolicina):
        upit = 'INSERT INTO velicina_odjece VALUES(' + str(id) + ',' + str(velicinaID) + ',' + str(kolicina) + ');'
        self.konekcijaNaBazu.UnesiPodatke(upit)

    def dohvatiVelicineOdjece(self):
        upit = 'SELECT * FROM velicina_odjece;'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita

    def izmjeniKolicinu(self, kolicina, odjecaID, velicinaID):
        upit = 'UPDATE velicina_odjece SET kolicina = '+str(kolicina)+' WHERE odjecaID = '+str(odjecaID)+' AND velicinaID = ' +str(velicinaID)+';'
        self.konekcijaNaBazu.UnesiPodatke(upit)


    def dohvatiRaspolozivuKolicinuKomadaOdjece(self, odjecaID):
        upit = 'SELECT CAST(SUM(kolicina) AS signed) FROM velicina_odjece WHERE odjecaID = '+str(odjecaID)+';'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita


    def dohvatiRaspolozivuKolicinuKomadaOdjecePoPojedinojVelicini(self, velicina, odjecaID):
        upit = 'SELECT CAST(IDvelicina AS signed) FROM velicina WHERE velicina = ' + '"' + velicina + '"' + ';'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        upit2 = 'SELECT CAST(kolicina AS signed) FROM velicina_odjece WHERE odjecaID = '+str(odjecaID)+' AND velicinaID = ' + '"' + str(rezultatUpita[0][0]) + '"' + ';'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit2)
        return rezultatUpita

    def izbrisiKupljenuKolicinu(self, odjecaID):
        upit = 'UPDATE velicina_odjece SET kolicina = kolicina - 1 WHERE odjecaID = '+str(odjecaID)+';'
        self.konekcijaNaBazu.UnesiPodatke(upit)

    def dohvatiVelicinuKupljeneOdjece(self, velicina):
        upit = 'SELECT IDvelicina FROM velicina WHERE velicina = ' + '"' + velicina + '"' + ';'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita

from PyQt5 import QtCore, QtWidgets, QtGui

import sys, DBKlasa

class Korisnik():
    def __init__(self):
        self.konekcijaNaBazu = DBKlasa.DBKlasa()

    def prijavaProvjeriKorisnika(self, korIme, lozinka):
        k = korIme
        l = lozinka
        upit = 'SELECT IDkorisnik FROM korisnik WHERE korisnickoIme = '+'"'+str(k)+'"'+' AND lozinka = '+'"'+str(l)+'"'+';'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)

        return rezultatUpita

    def registracijaKorisnika(self, korIme, lozinka, ime, prezime, email, drzava, postanskiBroj, brTel, brKart, adresa):
        upit = 'INSERT INTO korisnik VALUES(default,'+'"'+str(korIme)+'"'+','+'"'+str(lozinka)+'"'+','+'"'+str(ime)+'"'+','+'"'+str(prezime)+'"'+','+'"'+str(email)+'"'+','+'"'+str(brTel)+'"'+','+'"'+str(brKart)+'"'+','+'"'+str(adresa)+'"'+','+'"'+str(drzava)+'"'+','+'"'+str(postanskiBroj)+'"'+','"2"',"0");'
        self.konekcijaNaBazu.UnesiPodatke(upit)

    def dohvatiSveKorisinike(self):
        upit = 'SELECT * FROM korisnik WHERE korisnikIzbrisan = 0;'
        rezultatUpita = self.konekcijaNaBazu.dohvatiPodatke(upit)
        return rezultatUpita

    def obrisiKorisnika(self, korisnikID):
        upit = "UPDATE korisnik set korisnikIzbrisan = 1 WHERE IDkorisnik = "+str(korisnikID)+";"
        self.konekcijaNaBazu.Izbrisi(upit)

    def izmjeniKorisnika(self, korisnikID, korisnickoIme, lozinka, ime, prezime, email, brojTelefona, brojKartice, adresa, drzava, postanskiBroj):

        upit = 'UPDATE korisnik SET korisnickoIme ='+'"'+str(korisnickoIme)+'",'\
               + 'lozinka = '+'"'+str(lozinka)+'",'\
               + 'ime = '+'"'+str(ime)+'",'\
               + 'prezime = '+'"'+str(prezime)+'",'\
               + 'email = '+'"'+str(email)+'",'\
               + 'brojTelefona = '+'"'+str(brojTelefona)+'",'\
               + 'brojKartice = '+'"'+str(brojKartice)+'",'\
               + 'adresa = '+'"'+str(adresa)+'",'\
               + 'drzava = '+'"'+str(drzava)+'",'\
               + 'postanskiBroj = '+'"'+str(postanskiBroj)+'" ' + ' WHERE IDkorisnik = '+str(korisnikID)+';'
        self.konekcijaNaBazu.UnesiPodatke(upit)

-- MySQL dump 10.13  Distrib 5.7.19, for Win64 (x86_64)
--
-- Host: localhost    Database: onlineshopping
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `korisnik`
--

DROP TABLE IF EXISTS `korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `korisnik` (
  `IDkorisnik` int(11) NOT NULL AUTO_INCREMENT,
  `korisnickoIme` varchar(45) NOT NULL,
  `lozinka` varchar(45) NOT NULL,
  `ime` varchar(45) NOT NULL,
  `prezime` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `brojTelefona` varchar(45) NOT NULL,
  `brojKartice` varchar(45) NOT NULL,
  `adresa` varchar(45) NOT NULL,
  `drzava` varchar(45) NOT NULL,
  `postanskiBroj` int(11) NOT NULL,
  `tipKorisnikaID` int(11) NOT NULL,
  `korisnikIzbrisan` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`IDkorisnik`),
  KEY `fk_Korisnik_Tip_Korisnika1_idx` (`tipKorisnikaID`),
  CONSTRAINT `fk_Korisnik_Tip_Korisnika1` FOREIGN KEY (`tipKorisnikaID`) REFERENCES `tip_korisnika` (`IDtipKorisnika`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik`
--

LOCK TABLES `korisnik` WRITE;
/*!40000 ALTER TABLE `korisnik` DISABLE KEYS */;
INSERT INTO `korisnik` VALUES (1,'admin','admin','ime','prezime','email@gmail.com','09912127722','HR11111111111','adresaAdmin','drzavaAdmin',99999,1,0),(2,'josbijeli','12345678','Josip','Bijelic','josbijeli@foi.hr','0997546599','HR22222222222','Vjekoslava Spincica 26','Hrvatska',42000,2,0),(3,'Mija','87654321','Mia','Simunic','msimunic@foi.hr','0922124245','HR33333333333','Duga 21','Hrvatska',32100,2,1),(5,'korime','lozinka','ime','prezime','email','brtel','brkart','adresa','drzava',23111,2,1),(10,'Tomo','2468','Tomislav','Đalto','td@gmail.com','0998762222','HR12345678910','Moja','Hrvatska',23,2,1),(14,'korime','lozinka123','Ime','Prezime','email@email.com','+3852958822','HR844208420394','Adresa','Hrvatska',42000,2,1),(15,'jami','miajenaj','Mia','Simunic','mia.0411@hotmail.com','0994035994','HR1923824723','duga 79','hrvatska',42000,2,1),(16,'Korisnik1','lozinka1','ime1','prezime1','email1','brojtelefona1','brojkartice1','adresa1','drzava1',23213,2,1),(17,'deniSimunic','deni123','Deni','Simunic','dsimunic@foi.hr','0996248822','HR1234566776','Duga Ulica 22','Hrvatska',65999,2,1);
/*!40000 ALTER TABLE `korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kosarica`
--

DROP TABLE IF EXISTS `kosarica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kosarica` (
  `IDkosarica` int(11) NOT NULL AUTO_INCREMENT,
  `velicina` varchar(45) DEFAULT NULL,
  `kolicina` int(11) DEFAULT NULL,
  `korisnikID` int(11) NOT NULL,
  `odjecaID` int(11) NOT NULL,
  PRIMARY KEY (`IDkosarica`),
  KEY `fk_kosarica_Korisnik1_idx` (`korisnikID`),
  KEY `fk_kosarica_Odjeca1_idx` (`odjecaID`),
  CONSTRAINT `fk_kosarica_Korisnik1` FOREIGN KEY (`korisnikID`) REFERENCES `korisnik` (`IDkorisnik`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_kosarica_Odjeca1` FOREIGN KEY (`odjecaID`) REFERENCES `odjeca` (`IDodjeca`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kosarica`
--

LOCK TABLES `kosarica` WRITE;
/*!40000 ALTER TABLE `kosarica` DISABLE KEYS */;
/*!40000 ALTER TABLE `kosarica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kupio_odjecu`
--

DROP TABLE IF EXISTS `kupio_odjecu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kupio_odjecu` (
  `korisnikID` int(11) NOT NULL,
  `odjecaID` int(11) NOT NULL,
  `IDkupovina` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`IDkupovina`),
  KEY `fk_Kupio_Odjecu_Korisnik_idx` (`korisnikID`),
  KEY `fk_Kupio_Odjecu_Odjeca1_idx` (`odjecaID`),
  CONSTRAINT `fk_Kupio_Odjecu_Korisnik` FOREIGN KEY (`korisnikID`) REFERENCES `korisnik` (`IDkorisnik`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Kupio_Odjecu_Odjeca1` FOREIGN KEY (`odjecaID`) REFERENCES `odjeca` (`IDodjeca`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kupio_odjecu`
--

LOCK TABLES `kupio_odjecu` WRITE;
/*!40000 ALTER TABLE `kupio_odjecu` DISABLE KEYS */;
/*!40000 ALTER TABLE `kupio_odjecu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `odjeca`
--

DROP TABLE IF EXISTS `odjeca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `odjeca` (
  `IDodjeca` int(11) NOT NULL AUTO_INCREMENT,
  `cijena` int(11) DEFAULT NULL,
  `naziv` varchar(45) DEFAULT NULL,
  `snizenjeID` int(11) NOT NULL,
  `spolID` int(11) NOT NULL,
  `slika` char(100) DEFAULT NULL,
  `odjecaObrisana` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`IDodjeca`),
  KEY `fk_Odjeca_Snizenje1_idx` (`snizenjeID`),
  KEY `fk_Odjeca_Spol1_idx` (`spolID`),
  CONSTRAINT `fk_Odjeca_Snizenje1` FOREIGN KEY (`snizenjeID`) REFERENCES `snizenje` (`IDsnizenje`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Odjeca_Spol1` FOREIGN KEY (`spolID`) REFERENCES `spol` (`IDspol`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `odjeca`
--

LOCK TABLES `odjeca` WRITE;
/*!40000 ALTER TABLE `odjeca` DISABLE KEYS */;
INSERT INTO `odjeca` VALUES (1,200,'Mini haljina Roly',10,2,'Slikeodjece/MiniHaljina1.jpg',0),(2,170,'Mini haljina Clarita',2,2,'Slikeodjece/MiniHaljina2.jpg',0),(3,219,'Maxi haljina Nadia',4,2,'Slikeodjece/MiniHaljina3.jpg',0),(4,219,'Elegantna haljina Eudora',6,2,'Slikeodjece/ElegantnaHaljina.jpg',0),(5,249,'Kaput Kaipo',10,2,'Slikeodjece/Kaput.jpg',0),(6,149,'Bluza Milaca',10,2,'Slikeodjece/Bluza.jpg',1),(7,320,'Hlace Royal',10,1,'Slikeodjece/hlaceRoyal.jpg',0),(8,120,'T-Shirt',2,1,'Slikeodjece/TShirt.jpg',0),(9,400,'Jakna Hennis',3,1,'Slikeodjece/JaknaHennis.jpg',0),(10,700,'Jakna Nike tusson',4,1,'Slikeodjece/JaknNike.jpg',0),(11,250,'Rifle jeans',10,1,'Slikeodjece/rifleJeans.jpg',0),(12,100,'Rifle SudioPackt',10,1,'Slikeodjece/RifleSudio.jpg',0),(13,120,'Doodles rifle',10,3,'Slikeodjece/DjecjeRifle.jpg',0),(14,70,'Nike kids majica',10,3,'Slikeodjece/NikeKids.jpg',0),(15,100,'Kids T-shirt',2,3,'Slikeodjece/KidsTShirt.jpg',0),(16,100,'Trenerka Kd',5,3,'Slikeodjece/TrenerkaDjeca.jpg',0),(32,200,'Rifle u boji',10,1,'Slikeodjece/ObojeneRifle.jpg',0),(33,200,'Bijela bluza',10,2,'Slikeodjece/BijelaBluza.jpg',0),(34,22,'sad',3,1,'Slikeodjece/sad.jpg',1);
/*!40000 ALTER TABLE `odjeca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `snizenje`
--

DROP TABLE IF EXISTS `snizenje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `snizenje` (
  `IDsnizenje` int(11) NOT NULL AUTO_INCREMENT,
  `snizenje` float DEFAULT NULL,
  `snizenjePostotak` int(11) DEFAULT NULL,
  PRIMARY KEY (`IDsnizenje`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `snizenje`
--

LOCK TABLES `snizenje` WRITE;
/*!40000 ALTER TABLE `snizenje` DISABLE KEYS */;
INSERT INTO `snizenje` VALUES (1,0.1,10),(2,0.2,20),(3,0.3,30),(4,0.4,40),(5,0.5,50),(6,0.6,60),(7,0.7,70),(10,0,0);
/*!40000 ALTER TABLE `snizenje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spol`
--

DROP TABLE IF EXISTS `spol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `spol` (
  `IDspol` int(11) NOT NULL,
  `spol` varchar(45) NOT NULL,
  PRIMARY KEY (`IDspol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spol`
--

LOCK TABLES `spol` WRITE;
/*!40000 ALTER TABLE `spol` DISABLE KEYS */;
INSERT INTO `spol` VALUES (1,'Muska odjeca'),(2,'Zenska odjeca'),(3,'Djecja odjeca');
/*!40000 ALTER TABLE `spol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tip_korisnika`
--

DROP TABLE IF EXISTS `tip_korisnika`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tip_korisnika` (
  `IDtipKorisnika` int(11) NOT NULL AUTO_INCREMENT,
  `tipKorisnika` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`IDtipKorisnika`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tip_korisnika`
--

LOCK TABLES `tip_korisnika` WRITE;
/*!40000 ALTER TABLE `tip_korisnika` DISABLE KEYS */;
INSERT INTO `tip_korisnika` VALUES (1,'administrator'),(2,'registrirani korisnik');
/*!40000 ALTER TABLE `tip_korisnika` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `velicina`
--

DROP TABLE IF EXISTS `velicina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `velicina` (
  `IDvelicina` int(11) NOT NULL AUTO_INCREMENT,
  `velicina` varchar(45) NOT NULL,
  PRIMARY KEY (`IDvelicina`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `velicina`
--

LOCK TABLES `velicina` WRITE;
/*!40000 ALTER TABLE `velicina` DISABLE KEYS */;
INSERT INTO `velicina` VALUES (1,'S'),(2,'XS'),(3,'M'),(4,'L'),(5,'XL'),(6,'XXL');
/*!40000 ALTER TABLE `velicina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `velicina_odjece`
--

DROP TABLE IF EXISTS `velicina_odjece`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `velicina_odjece` (
  `odjecaID` int(11) NOT NULL,
  `velicinaID` int(11) NOT NULL,
  `kolicina` int(11) DEFAULT NULL,
  PRIMARY KEY (`odjecaID`,`velicinaID`),
  KEY `fk_Velicina_Odjece_Odjeca1_idx` (`odjecaID`),
  KEY `fk_Velicina_Odjece_Velicina1_idx` (`velicinaID`),
  CONSTRAINT `fk_Velicina_Odjece_Odjeca1` FOREIGN KEY (`odjecaID`) REFERENCES `odjeca` (`IDodjeca`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Velicina_Odjece_Velicina1` FOREIGN KEY (`velicinaID`) REFERENCES `velicina` (`IDvelicina`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `velicina_odjece`
--

LOCK TABLES `velicina_odjece` WRITE;
/*!40000 ALTER TABLE `velicina_odjece` DISABLE KEYS */;
INSERT INTO `velicina_odjece` VALUES (1,1,33),(1,2,31),(1,3,31),(1,4,31),(2,1,0),(2,2,3),(2,3,14),(2,4,5),(3,1,0),(3,2,0),(3,4,0),(3,5,0),(4,1,0),(4,2,0),(4,3,23),(4,5,0),(4,6,0),(5,1,0),(5,2,1),(5,3,1),(5,4,1),(5,5,1),(5,6,1),(6,1,1),(6,2,1),(6,4,1),(6,6,1),(7,1,1),(7,2,3),(7,3,3),(8,2,2),(8,3,2),(8,4,2),(8,6,2),(9,1,0),(9,2,0),(9,3,0),(9,4,0),(9,5,0),(9,6,0),(10,1,0),(10,3,0),(10,4,0),(11,1,1),(11,2,1),(11,3,1),(11,4,1),(11,5,1),(11,6,1),(12,1,1),(12,2,1),(12,4,1),(12,6,1),(13,1,0),(13,3,0),(13,5,0),(14,1,0),(14,2,0),(14,3,0),(15,1,0),(15,2,0),(15,3,0),(15,4,0),(15,5,0),(16,1,0),(16,2,1),(16,3,1),(16,4,1),(16,5,1),(16,6,1),(32,1,1),(32,4,1),(33,1,1),(33,2,1),(33,3,1),(34,3,2);
/*!40000 ALTER TABLE `velicina_odjece` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-03 19:38:23

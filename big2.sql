-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: big2
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.14.04.1

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
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `player` (
  `id` int(11) NOT NULL,
  `username` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `create_date` date DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
INSERT INTO `player` VALUES (0,'PinLiang','GOD','2014-10-11',2),(1,'Hank','GOD2','2014-10-11',2),(2,'Hank1','GOD2','2014-10-11',2),(3,'Hank3','GOD2','2014-11-17',2),(4,'Hank2','GOD2','2014-11-17',1);
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tables`
--

DROP TABLE IF EXISTS `tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tables` (
  `id` int(11) NOT NULL,
  `titles` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `player1` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `player2` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `player3` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `player4` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `permission` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `check1` int(11) DEFAULT NULL,
  `check2` int(11) DEFAULT NULL,
  `check3` int(11) DEFAULT NULL,
  `check4` int(11) DEFAULT NULL,
  `remind1` int(11) DEFAULT NULL,
  `remind2` int(11) DEFAULT NULL,
  `remind3` int(11) DEFAULT NULL,
  `remind4` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `cards1` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cards2` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cards3` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cards4` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tables`
--

LOCK TABLES `tables` WRITE;
/*!40000 ALTER TABLE `tables` DISABLE KEYS */;
INSERT INTO `tables` VALUES (0,'超人桌','PinLiang','empty','empty','empty','empty',0,0,0,0,0,0,0,0,0,NULL,NULL,NULL,NULL),(1,'豬頭桌','PinLiang','empty','empty','empty','empty',0,0,0,0,0,0,0,0,0,NULL,NULL,NULL,NULL),(2,'國王桌','PinLiang','empty','empty','empty','empty',0,0,0,0,0,0,0,0,0,NULL,NULL,NULL,NULL),(3,'測試桌','PinLiang','empty','empty','empty','empty',0,0,0,0,0,0,0,0,0,NULL,NULL,NULL,NULL),(4,'超級大老二','PinLiang','empty','empty','empty','empty',0,0,0,0,0,0,0,0,0,NULL,NULL,NULL,NULL),(5,'超級大老二3','PinLiang','Hank1','Hank3','Hank','empty',0,0,0,1,13,13,13,13,1,'s9,d10,c4,c9,s7,c2,d7,s13,h13,c7,d1,h3,d2','d9,s11,s3,h11,c1,h10,s12,s8,s6,d6,s1,c5,s4','d5,s2,d11,d13,c6,s10,c12,c10,c3,c13,d4,h8,h7','d3,d12,d8,h4,h6,h2,h1,h12,c11,s5,h5,h9,c8'),(6,'超級大老二2','PinLiang','empty','empty','empty','empty',1,0,0,0,0,0,0,0,0,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `tables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `week_history`
--

DROP TABLE IF EXISTS `week_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `week_history` (
  `id` int(11) NOT NULL,
  `winner` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `winderpoint` int(11) DEFAULT NULL,
  `loser` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `loserpoint` int(11) DEFAULT NULL,
  `battle_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `week_history`
--

LOCK TABLES `week_history` WRITE;
/*!40000 ALTER TABLE `week_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `week_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-26 17:50:01

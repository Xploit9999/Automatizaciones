/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.6.22-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: testing
-- ------------------------------------------------------
-- Server version	10.6.22-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vulnerabilidades`
--

DROP TABLE IF EXISTS `vulnerabilidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `vulnerabilidades` (
  `servidor` varchar(50) DEFAULT NULL,
  `categoria` varchar(100) DEFAULT NULL,
  `cantidad` int(11) NOT NULL,
  `so` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vulnerabilidades`
--

LOCK TABLES `vulnerabilidades` WRITE;
/*!40000 ALTER TABLE `vulnerabilidades` DISABLE KEYS */;
INSERT INTO `vulnerabilidades` VALUES ('itunix','Paquetes y Software',3,'RedHat'),('itunix','Integridad del Sistema',3,'RedHat'),('itunix','Políticas de Seguridad',1,'RedHat'),('itunix','Particionamiento y Archivos',6,'RedHat'),('itunix','Privilegios de Usuario',4,'RedHat'),('itunix','Autenticación y Acceso',1,'RedHat'),('itunix','Mensajes de Advertencia',2,'RedHat'),('itunix','Contraseñas y Autenticación',23,'RedHat'),('itunix','Otros',118,'RedHat'),('itunix','Kernel y Sistema',3,'RedHat'),('itunix','Servicios',4,'RedHat'),('itunix','NTP',1,'RedHat'),('itunix','SSH y Seguridad',16,'RedHat');
/*!40000 ALTER TABLE `vulnerabilidades` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-07 13:51:30

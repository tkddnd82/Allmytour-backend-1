-- MySQL dump 10.13  Distrib 8.0.26, for macos11.3 (x86_64)
--
-- Host: localhost    Database: allmytour
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `codes`
--

DROP TABLE IF EXISTS `codes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `codes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `upper_code` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `code_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `used` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codes`
--

LOCK TABLES `codes` WRITE;
/*!40000 ALTER TABLE `codes` DISABLE KEYS */;
INSERT INTO `codes` VALUES (1,'0','운전면허증','Y'),(2,'0','한국관광통역안내사','Y'),(3,'0','기타자격증','Y'),(4,'1','영어','Y'),(5,'1','중국어(표준어)','Y'),(6,'1','중국어(광동어','Y'),(7,'1','일본어','Y'),(8,'1','기타언어','Y'),(9,'2','5인','Y'),(10,'2','9인','Y'),(11,'2','12인','Y'),(12,'2','15인','Y'),(13,'2','기타인승','Y'),(14,'3','Adventure','Y'),(15,'3','Culture','Y'),(16,'3','Nightlife','Y'),(17,'3','K-pop','Y'),(18,'3','Festival','Y'),(19,'3','Experience','Y'),(20,'3','History','Y'),(21,'3','DIY','Y'),(22,'3','기타전문분야','Y'),(23,'4','서울','Y'),(24,'4','경기도','Y'),(25,'4','경상도','Y'),(26,'4','강원도','Y'),(27,'4','전라도','Y'),(28,'4','충청도','Y'),(29,'4','제주도','Y'),(30,'4','기타지역','Y'),(31,'41','서울전체','Y'),(32,'41','강서','Y'),(33,'41','강북','Y'),(34,'41','강남','Y'),(35,'41','강동','Y'),(36,'42','경기도전체','Y'),(37,'42','가평','Y'),(38,'42','광명','Y'),(39,'42','수원','Y'),(40,'42','파주','Y'),(41,'42','포천','Y'),(42,'43','경상도전체','Y'),(43,'43','부산/서면','Y'),(44,'43','대구','Y'),(45,'43','울산','Y'),(46,'43','경주','Y'),(47,'43','포항','Y'),(48,'43','거제','Y'),(49,'43','통영','Y'),(50,'44','강원도전체','Y'),(51,'44','강릉','Y'),(52,'44','삼척','Y'),(53,'44','속초/양양','Y'),(54,'44','인제','Y'),(55,'44','평창','Y'),(56,'44','원주','Y'),(57,'44','태백','Y'),(58,'45','전라도전체','Y'),(59,'45','나주','Y'),(60,'45','담양','Y'),(61,'45','목포','Y'),(62,'45','보성','Y'),(63,'45','여수','Y'),(64,'45','완도','Y'),(65,'46','충청도전체','Y'),(66,'46','단양','Y'),(67,'46','충주','Y'),(68,'46','당진','Y'),(69,'46','보령','Y'),(70,'46','천안','Y'),(71,'46','태안','Y'),(72,'47','제주도전체','Y'),(73,'47','제주시','Y'),(74,'47','서귀포시','Y'),(75,'47','중문','Y'),(76,'47','우도','Y'),(77,'5','Short','Y'),(78,'5','Half','Y'),(79,'5','Full','Y'),(80,'6','사진촬영','Y'),(81,'6','영상촬영','Y'),(82,'6','기타서비스','Y');
/*!40000 ALTER TABLE `codes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'contenttypes','contenttype'),(6,'makers','code'),(5,'makers','imagefile'),(7,'makers','maker'),(9,'makers','makercode'),(8,'makers','producttype'),(2,'sessions','session'),(4,'users','user'),(3,'users','usertemp');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-09-03 22:51:12.334110'),(2,'contenttypes','0002_remove_content_type_name','2021-09-03 22:51:12.496276'),(3,'sessions','0001_initial','2021-09-03 22:51:12.528992'),(4,'users','0001_initial','2021-09-03 22:54:51.230610'),(5,'makers','0001_initial','2021-09-03 22:54:51.482682'),(6,'makers','0002_makercode_etc','2021-09-03 23:19:27.258493');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image_files`
--

DROP TABLE IF EXISTS `image_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `image_files` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `profile_image` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  `id_card_image` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  `passbook_image` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  `license_image` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  `maker_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `image_files_maker_id_9ddfe592_fk_makers_id` (`maker_id`),
  CONSTRAINT `image_files_maker_id_9ddfe592_fk_makers_id` FOREIGN KEY (`maker_id`) REFERENCES `makers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image_files`
--

LOCK TABLES `image_files` WRITE;
/*!40000 ALTER TABLE `image_files` DISABLE KEYS */;
/*!40000 ALTER TABLE `image_files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maker_codes`
--

DROP TABLE IF EXISTS `maker_codes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `maker_codes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code_id` bigint NOT NULL,
  `maker_id` bigint NOT NULL,
  `etc` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `maker_codes_code_id_a3b2137c_fk_codes_id` (`code_id`),
  KEY `maker_codes_maker_id_836ee9c8_fk_makers_id` (`maker_id`),
  CONSTRAINT `maker_codes_code_id_a3b2137c_fk_codes_id` FOREIGN KEY (`code_id`) REFERENCES `codes` (`id`),
  CONSTRAINT `maker_codes_maker_id_836ee9c8_fk_makers_id` FOREIGN KEY (`maker_id`) REFERENCES `makers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maker_codes`
--

LOCK TABLES `maker_codes` WRITE;
/*!40000 ALTER TABLE `maker_codes` DISABLE KEYS */;
/*!40000 ALTER TABLE `maker_codes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `makers`
--

DROP TABLE IF EXISTS `makers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `makers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nickname` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `bank_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `bank_number` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `account_holder` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `update_at` datetime(6) NOT NULL,
  `instagram` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `facebook` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `youtube` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `another_sns1` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `another_sns2` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `another_sns3` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `product_type_id` bigint DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `makers_product_type_id_456af9d2_fk_product_type_id` (`product_type_id`),
  KEY `makers_user_id_a1fd755b_fk_users_id` (`user_id`),
  CONSTRAINT `makers_product_type_id_456af9d2_fk_product_type_id` FOREIGN KEY (`product_type_id`) REFERENCES `product_type` (`id`),
  CONSTRAINT `makers_user_id_a1fd755b_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `makers`
--

LOCK TABLES `makers` WRITE;
/*!40000 ALTER TABLE `makers` DISABLE KEYS */;
/*!40000 ALTER TABLE `makers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_type`
--

DROP TABLE IF EXISTS `product_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_type` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `product_type` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_type`
--

LOCK TABLES `product_type` WRITE;
/*!40000 ALTER TABLE `product_type` DISABLE KEYS */;
INSERT INTO `product_type` VALUES (1,'크리에이팅 상품'),(2,'맞춤형 상품'),(3,'기획 상품 가이딩');
/*!40000 ALTER TABLE `product_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_temp`
--

DROP TABLE IF EXISTS `user_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_temp` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `code` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  `expired_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_temp`
--

LOCK TABLES `user_temp` WRITE;
/*!40000 ALTER TABLE `user_temp` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_temp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `phone_number` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-06 13:57:11

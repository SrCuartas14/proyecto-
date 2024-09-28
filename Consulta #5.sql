-- Volcando estructura de base de datos para chicasadomicilio
CREATE DATABASE IF NOT EXISTS `chicasadomicilio` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `chicasadomicilio`;

-- Volcando estructura para tabla chicasadomicilio.chicas
CREATE TABLE IF NOT EXISTS `chicas` (
  `id_chica` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `edad` int(11) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `especialidad` varchar(100) DEFAULT NULL,
  `disponibilidad` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id_chica`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla chicasadomicilio.chicas: ~30 rows (aproximadamente)
/*!40000 ALTER TABLE `chicas` DISABLE KEYS */;
INSERT IGNORE INTO `chicas` (`id_chica`, `nombre`, `edad`, `telefono`, `direccion`, `especialidad`, `disponibilidad`) VALUES
	(1, 'Ana Pérez', 28, '555-1234', 'Calle Falsa 123', NULL, 1),
	(2, 'Laura Gómez', 32, '555-5678', 'Avenida Siempre Viva 742', NULL, 1),
	(3, 'Sofía Martínez', 25, '555-8765', 'Boulevard de la Luna 101', NULL, 1),
	(4, 'María Rodríguez', 30, '555-4321', 'Calle del Sol 456', NULL, 0),
	(5, 'Julia Díaz', 29, '555-6789', 'Calle Primavera 222', NULL, 1),
	(6, 'Carla Ruiz', 27, '555-5432', 'Avenida del Mar 333', NULL, 1),
	(7, 'Ana Pérez', 28, '555-1234', 'Calle Falsa 123', NULL, 1),
	(8, 'Laura Gómez', 32, '555-5678', 'Avenida Siempre Viva 742', NULL, 1),
	(9, 'Sofía Martínez', 25, '555-8765', 'Boulevard de la Luna 101', NULL, 1),
	(10, 'María Rodríguez', 30, '555-4321', 'Calle del Sol 456', NULL, 0),
	(11, 'Julia Díaz', 29, '555-6789', 'Calle Primavera 222', NULL, 1),
	(12, 'Carla Ruiz', 27, '555-5432', 'Avenida del Mar 333', NULL, 1),
	(13, 'Ana Pérez', 28, '555-1234', 'Calle Falsa 123', NULL, 1),
	(14, 'Laura Gómez', 32, '555-5678', 'Avenida Siempre Viva 742', NULL, 1),
	(15, 'Sofía Martínez', 25, '555-8765', 'Boulevard de la Luna 101', NULL, 1),
	(16, 'María Rodríguez', 30, '555-4321', 'Calle del Sol 456', NULL, 0),
	(17, 'Julia Díaz', 29, '555-6789', 'Calle Primavera 222', NULL, 1),
	(18, 'Carla Ruiz', 27, '555-5432', 'Avenida del Mar 333', NULL, 1),
	(19, 'Ana Pérez', 28, '555-1234', 'Calle Falsa 123', NULL, 1),
	(20, 'Laura Gómez', 32, '555-5678', 'Avenida Siempre Viva 742', NULL, 1),
	(21, 'Sofía Martínez', 25, '555-8765', 'Boulevard de la Luna 101', NULL, 1),
	(22, 'María Rodríguez', 30, '555-4321', 'Calle del Sol 456', NULL, 0),
	(23, 'Julia Díaz', 29, '555-6789', 'Calle Primavera 222', NULL, 1),
	(24, 'Carla Ruiz', 27, '555-5432', 'Avenida del Mar 333', NULL, 1),
	(25, 'Ana Pérez', 28, '555-1234', 'Calle Falsa 123', NULL, 1),
	(26, 'Laura Gómez', 32, '555-5678', 'Avenida Siempre Viva 742', NULL, 1),
	(27, 'Sofía Martínez', 25, '555-8765', 'Boulevard de la Luna 101', NULL, 1),
	(28, 'María Rodríguez', 30, '555-4321', 'Calle del Sol 456', NULL, 0),
	(29, 'Julia Díaz', 29, '555-6789', 'Calle Primavera 222', NULL, 1);
/*!40000 ALTER TABLE `chicas` ENABLE KEYS */;

-- Volcando estructura para tabla chicasadomicilio.clientes
CREATE TABLE IF NOT EXISTS `clientes` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla chicasadomicilio.clientes: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT IGNORE INTO `clientes` (`id_cliente`, `nombre`, `telefono`, `direccion`, `email`) VALUES
	(1, 'Pedro Sánchez', '555-1111', 'Calle Mayor 10', 'pedro.sanchez@example.com'),
	(2, 'Gabriel Fernández', '555-2222', 'Calle Secundaria 20', 'luisa.fernandez@example.com'),
	(3, 'Carlos López', '555-3333', 'Calle Tercera 30', 'carlos.lopez@example.com'),
	(4, 'James Mosquera', '555-4444', 'Avenida Principal 40', 'maria.lopez@example.com'),
	(5, 'Kevin Gómez', '555-5555', 'Calle del Río 50', 'ana.gomez@example.com'),
	(6, 'José Martínez', '555-6666', 'Calle del Bosque 60', 'jose.martinez@example.com');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;

-- Volcando estructura para tabla chicasadomicilio.envios
CREATE TABLE IF NOT EXISTS `envios` (
  `id_envio` int(11) NOT NULL AUTO_INCREMENT,
  `id_cliente` int(11) DEFAULT NULL,
  `id_chica` int(11) DEFAULT NULL,
  `fecha_envio` datetime NOT NULL,
  `direccion_envio` varchar(255) DEFAULT NULL,
  `estado` enum('Pendiente','En proceso','Completado','Cancelado') DEFAULT 'Pendiente',
  PRIMARY KEY (`id_envio`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_chica` (`id_chica`),
  CONSTRAINT `envios_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`),
  CONSTRAINT `envios_ibfk_2` FOREIGN KEY (`id_chica`) REFERENCES `chicas` (`id_chica`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla chicasadomicilio.envios: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `envios` DISABLE KEYS */;
INSERT IGNORE INTO `envios` (`id_envio`, `id_cliente`, `id_chica`, `fecha_envio`, `direccion_envio`, `estado`) VALUES
	(1, 1, 1, '2024-08-10 14:00:00', 'Calle Mayor 10', 'Completado'),
	(2, 2, 2, '2024-08-11 16:00:00', 'Calle Secundaria 20', 'Completado'),
	(3, 3, 3, '2024-08-12 18:00:00', 'Calle Tercera 30', 'Completado'),
	(4, 4, 4, '2024-08-13 20:00:00', 'Avenida Principal 40', 'Completado'),
	(5, 5, 5, '2024-08-14 15:00:00', 'Calle del Río 50', 'Completado'),
	(6, 6, 6, '2024-08-15 17:00:00', 'Calle del Bosque 60', 'Completado');
/*!40000 ALTER TABLE `envios` ENABLE KEYS */;

-- Volcando estructura para tabla chicasadomicilio.fotos
CREATE TABLE IF NOT EXISTS `fotos` (
  `id_foto` int(11) NOT NULL AUTO_INCREMENT,
  `id_chica` int(11) DEFAULT NULL,
  `foto` longblob DEFAULT NULL,
  PRIMARY KEY (`id_foto`),
  KEY `id_chica` (`id_chica`),
  CONSTRAINT `fotos_ibfk_1` FOREIGN KEY (`id_chica`) REFERENCES `chicas` (`id_chica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla chicasadomicilio.fotos: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `fotos` DISABLE KEYS */;
/*!40000 ALTER TABLE `fotos` ENABLE KEYS */;

-- Volcando estructura para tabla chicasadomicilio.servicios
CREATE TABLE IF NOT EXISTS `servicios` (
  `id_servicio` int(11) NOT NULL AUTO_INCREMENT,
  `id_envio` int(11) DEFAULT NULL,
  `duracion` text DEFAULT NULL,
  `costo` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_servicio`),
  KEY `id_envio` (`id_envio`),
  CONSTRAINT `servicios_ibfk_1` FOREIGN KEY (`id_envio`) REFERENCES `envios` (`id_envio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla chicasadomicilio.servicios: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicios` ENABLE KEYS */;chicasadomiciliobase_datos_mujeres
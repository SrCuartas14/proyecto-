-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS base_datos_mujeres;
USE base_datos_mujeres;

-- Tabla de mujeres
CREATE TABLE mujeres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    coste DECIMAL(10, 2) NOT NULL,
    notas TEXT
);

-- Tabla de ventas
CREATE TABLE ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_mujer INT,
    id_cliente INT,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_mujer) REFERENCES mujeres(id),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

-- Tabla de tipo de servicio
CREATE TABLE tipo_servicio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL,
    coste DECIMAL(10, 2) NOT NULL
);

-- Tabla de clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    email VARCHAR(100)
);

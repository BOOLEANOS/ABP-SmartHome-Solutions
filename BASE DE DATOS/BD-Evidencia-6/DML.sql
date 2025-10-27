-- =========================================
-- BASE DE DATOS SMART HOME SOLUTIONS
-- =========================================

CREATE DATABASE smarthome;
USE smarthome;

-- =========================================
-- TABLA DE ROLES
-- =========================================
CREATE TABLE Rol (
  id_rol INT PRIMARY KEY AUTO_INCREMENT,
  nombre_rol VARCHAR(50) NOT NULL
);

INSERT INTO Rol (nombre_rol) VALUES 
('admin'), 
('usuario');

-- =========================================
-- TABLA DE USUARIOS
-- =========================================
CREATE TABLE Usuario (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  nombre_usuario VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  fecha_nacimiento DATE,
  password VARCHAR(100) NOT NULL,
  id_rol INT,
  FOREIGN KEY (id_rol) REFERENCES Rol(id_rol)
);

INSERT INTO Usuario (nombre_usuario, email, password, id_rol) VALUES
('Tobias','tobias21@gmail.com','olaquetal321',1),
('Goku','juan@mail.com','juan123',2),
('Luna','luna@gmail.com','freudthebest33',2),
('Jesus','jesus@gmail.com','labiblia',2),
('Coscu','coscu@gmail.com','coscuarmy55',2),
('Denis','denis@gmail.com','denislol2',2),
('Luis','luisito@gmail.com','luisillo987',2),
('Moria','moria@gmail.com','tinelli000',2),
('Lorena','lore_pao_pereyra@hotmail.com.ar','1234',1),
('Euge','euge@gmail.com','eugepass',2);

-- =========================================
-- TABLA DE TIPOS DE DISPOSITIVOS
-- =========================================
CREATE TABLE Tipo_dispositivo (
  id_tipo INT PRIMARY KEY AUTO_INCREMENT,
  tipo_dispositivo VARCHAR(50) NOT NULL
);

INSERT INTO Tipo_dispositivo (tipo_dispositivo) VALUES 
('Luz'),
('Sensor'),
('Cámara'),
('Electrodoméstico');

-- =========================================
-- TABLA DE DISPOSITIVOS
-- =========================================
CREATE TABLE Dispositivo (
  id_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
  nombre_dispositivo VARCHAR(50) NOT NULL,
  ubicacion VARCHAR(50),
  estado_dispositivo ENUM('encendido', 'apagado') DEFAULT 'apagado',
  id_usuario INT,
  id_tipo INT,
  FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
  FOREIGN KEY (id_tipo) REFERENCES Tipo_dispositivo(id_tipo)
);

INSERT INTO Dispositivo (nombre_dispositivo, ubicacion, estado_dispositivo, id_usuario, id_tipo) VALUES
('Luz Living','Living','apagado',2,1),
('Sensor Movimiento','Patio','encendido',2,2),
('Cámara Entrada','Entrada','encendido',1,3),
('Cafetera','Cocina','apagado',2,4),
('Luz Dormitorio','Dormitorio','apagado',2,1),
('Horno','Cocina','apagado',2,4),
('Ventilador','Dormitorio','encendido',2,4),
('Pava eléctrica','Cocina','encendido',2,4),
('Televisor','Living','encendido',1,4),
('Calefactor','Habitación','apagado',2,4);

-- =========================================
-- TABLA DE ACCIONES
-- =========================================
CREATE TABLE Accion_Automatizacion (
  id_accion INT PRIMARY KEY AUTO_INCREMENT,
  tipo_accion VARCHAR(50) NOT NULL
);

INSERT INTO Accion_Automatizacion (tipo_accion) VALUES 
('Encender'),
('Apagar'),
('Ajustar'),
('Suspender'),
('Notificar');

-- =========================================
-- TABLA DE CONDICIONES
-- =========================================
CREATE TABLE Condicion_Automatizacion (
  id_condicion INT PRIMARY KEY AUTO_INCREMENT,
  tipo_condicion VARCHAR(50) NOT NULL
);

INSERT INTO Condicion_Automatizacion (tipo_condicion) VALUES 
('Al anochecer'),
('Temperatura < 10°C'),
('Movimiento detectado'),
('Hora 22:00'),
('Inicio jornada laboral'),
('Fin jornada laboral'),
('Presencia detectada'),
('Humedad alta'),
('Temperatura > 28°C'),
('Sin conexión WiFi');

-- =========================================
-- TABLA DE AUTOMATIZACIONES
-- =========================================
CREATE TABLE Automatizacion (
  id_automatizacion INT PRIMARY KEY AUTO_INCREMENT,
  nombre_automatizacion VARCHAR(50) NOT NULL,
  estado_automatizacion ENUM('activa', 'inactiva') DEFAULT 'inactiva',
  id_condicion INT,
  id_dispositivo INT,
  id_accion INT,
  FOREIGN KEY (id_condicion) REFERENCES Condicion_Automatizacion(id_condicion),
  FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo),
  FOREIGN KEY (id_accion) REFERENCES Accion_Automatizacion(id_accion)
);

INSERT INTO Automatizacion (nombre_automatizacion, estado_automatizacion, id_condicion, id_dispositivo, id_accion) VALUES
('Modo Noche','activa',1,1,1),
('Modo Ahorro','inactiva',2,4,2),
('Notificación Movimiento','activa',3,3,5),
('Climatización','activa',9,10,3),
('Bienvenida','inactiva',7,9,1),
('Despertar','activa',4,5,1),
('Humedad Alta','activa',8,2,5),
('Fin Jornada','inactiva',6,4,2),
('Seguridad Nocturna','activa',1,3,5),
('Modo Verano','activa',9,7,3);

-- =========================================
-- TABLA INTERMEDIA DISPOSITIVO - AUTOMATIZACIÓN
-- =========================================
CREATE TABLE Dispositivo_Automatizacion (
  id_dispositivo INT,
  id_automatizacion INT,
  PRIMARY KEY (id_dispositivo, id_automatizacion),
  FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo),
  FOREIGN KEY (id_automatizacion) REFERENCES Automatizacion(id_automatizacion)
);

INSERT INTO Dispositivo_Automatizacion (id_dispositivo, id_automatizacion) VALUES
(1,1),
(5,1),
(7,1),
(2,2),
(10,2),
(3,3),
(4,4),
(8,5),
(6,6),
(9,9);

-- =========================================
-- CONSULTAS MULTITABLA (con explicación)
-- =========================================

-- 1 Mostrar quién es el dueño de cada dispositivo
SELECT d.nombre_dispositivo, u.nombre_usuario, t.tipo_dispositivo
FROM Dispositivo d
JOIN Usuario u ON d.id_usuario = u.id_usuario
JOIN Tipo_dispositivo t ON d.id_tipo = t.id_tipo;

-- 2 Ver automatizaciones activas y qué acción ejecutan
SELECT a.nombre_automatizacion, d.nombre_dispositivo, ac.tipo_accion
FROM Automatizacion a
JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
JOIN Accion_Automatizacion ac ON a.id_accion = ac.id_accion
WHERE a.estado_automatizacion = 'activa';

-- 3 Ver usuarios con cantidad de dispositivos asociados
SELECT u.nombre_usuario, COUNT(d.id_dispositivo) AS total_dispositivos
FROM Usuario u
LEFT JOIN Dispositivo d ON u.id_usuario = d.id_usuario
GROUP BY u.nombre_usuario;

-- 4 Ver dispositivos con su automatización y condición
SELECT d.nombre_dispositivo, a.nombre_automatizacion, c.tipo_condicion
FROM Dispositivo d
JOIN Dispositivo_Automatizacion da ON d.id_dispositivo = da.id_dispositivo
JOIN Automatizacion a ON da.id_automatizacion = a.id_automatizacion
JOIN Condicion_Automatizacion c ON a.id_condicion = c.id_condicion;

-- =========================================
-- SUBCONSULTAS (con explicación)
-- =========================================

-- 1 Dispositivos que no tienen automatización asignada
SELECT nombre_dispositivo
FROM Dispositivo
WHERE id_dispositivo NOT IN (
    SELECT DISTINCT id_dispositivo FROM Dispositivo_Automatizacion
);

-- 2 Automatizaciones que se activan "al anochecer"
SELECT nombre_automatizacion
FROM Automatizacion
WHERE id_condicion = (
    SELECT id_condicion FROM Condicion_Automatizacion WHERE tipo_condicion = 'Al anochecer'
);

-- 3Dispositivos con automatizaciones activas
SELECT nombre_dispositivo
FROM Dispositivo
WHERE id_dispositivo IN (
    SELECT id_dispositivo FROM Automatizacion WHERE estado_automatizacion = 'activa'
);

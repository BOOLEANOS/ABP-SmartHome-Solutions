CREATE TABLE Rol (
  id_rol INT PRIMARY KEY AUTO_INCREMENT,
  nombre_rol VARCHAR(50) NOT NULL
);

CREATE TABLE Tipo_dispositivo (
  id_tipo INT PRIMARY KEY AUTO_INCREMENT,
  tipo_dispositivo VARCHAR(50) NOT NULL
);

CREATE TABLE Usuario (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  nombre_usuario VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  fecha_nacimiento DATE,
  password VARCHAR(100) NOT NULL,
  id_rol INT, 
  FOREIGN KEY (id_rol) REFERENCES Rol(id_rol)
);

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

CREATE TABLE Accion_Automatizacion (
  id_accion INT PRIMARY KEY AUTO_INCREMENT,
  tipo_accion VARCHAR(50) NOT NULL
);

CREATE TABLE Condicion_Automatizacion (
  id_condicion INT PRIMARY KEY AUTO_INCREMENT,
  tipo_condicion VARCHAR(50) NOT NULL
);

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

CREATE TABLE Dispositivo_Automatizacion (
  id_dispositivo INT,
  id_automatizacion INT,
  PRIMARY KEY (id_dispositivo, id_automatizacion),
  FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo),
  FOREIGN KEY (id_automatizacion) REFERENCES Automatizacion(id_automatizacion)
);

INSERT INTO Rol (nombre_rol) VALUES 
('admin'), 
('estandar');

INSERT INTO Usuario (nombre_usuario, email, fecha_nacimiento, password, id_rol) VALUES
('Tobias','tobias21@gmail.com','2002-05-07','olaquetal321',1),
('Goku','juan@mail.com','1995-05-10','juan123',2),
('Lunita','Mitsuki3@gmail.com','2001-03-19','Freudthebest33',2),
('Jesus','jesucritoelreal@gmail.com','0000-12-25','labiblia',2),
('Coscu','coscu@gmail.com','1993-11-20','Coscuarmy55',2),
('Denis','denis7@gmail.com','2001-01-26','Denislol2',2),
('Luisito','luisitocomunica@gmail.com','1989-04-20','luisilloelpillo987',2),
('Milei','vivalalibertadcrjo@gmail.com','1970-10-22','cristina<3',2),
('Moria','moriacasan33@gmail.com','1946-08-16','tinelli000',2),
('Profesor', 'ProfesoresISPC@gmail.com','2000-01-01','ISPCCORDOBA',2);

INSERT INTO Tipo_dispositivo (tipo_dispositivo) VALUES 
('luz'),
('sensores'),
('camaras'),
('electrodomesticos'),
('parlantes'),
('celulares'),
('lavarropas'),
('aspiradoras'),
('consolas'),
('cafeteras'),
('hornos'),
('masajeadores');

INSERT INTO Dispositivo (nombre_dispositivo, ubicacion, estado_dispositivo, id_usuario, id_tipo) VALUES
('Luz ultravioleta','Habitacion','apagado',2,1),
('detector de sonido','patio','encendido',2,2),
('Camara vigilancia','Entrada','encendido',1,3),
('Cafetera','Cocina','apagado',2,4),
('Luz Dormitorio','Dormitorio','apagado',2,1),
('Horno','Cocina','apagado',2,4),
('Luz de crepusuculo','Habitacion pajaros', 'encendido', 2,1),
('Pava electrica','Cocina','encendido', 2,4),
('Fabrica/Horno de pan','Cocina','encendido',2,4),
('PlayStation5', 'habitacion', 'encendido',1,4),
('Calefactor', 'habitacion','encendido',2,2);

INSERT INTO Accion_Automatizacion (tipo_accion) VALUES 
('encender'),
('apagar'),
('ajustar'),
('suspender'),
('actualizar'),
('pausar'),
('reanudar');
 
INSERT INTO Condicion_Automatizacion (tipo_condicion) VALUES 
('al anochecer'),
('temperatura menor a 10celcius'),
('movimiento detectado'),
('hora exacta 22:00pm'),
('activar opcion'),
('finalizado horario trabajo'),
('al finalizar la mañana'),
('al finalizar la tarde'),
('al finalizar la noche'),
('si detecta temperatura alta'),
('si detecta temperatura baja');

INSERT INTO Automatizacion (nombre_automatizacion, estado_automatizacion, id_condicion, id_dispositivo, id_accion) VALUES
('Modo Noche','activa',1,1,5),
('Modo Ahorro','inactiva',1,4,4),
('Notificacion Movimiento','activa',3,3,3),
('detección de temperatura alta', 'activa',10,11,1),
('deteccion de temperatura baja', 'inactiva', 11,11,2),
('seguridad de la casa','activa',3,2,6),
('Modo cocina','activa',8,4,1),
('Apagado por noche','inactiva',9,6,2),
('Encendido por la mañana','activa',7,5,1),
('Encendido por la tarde','activa',8,5,1);

INSERT INTO Dispositivo_Automatizacion (id_dispositivo, id_automatizacion) VALUES
(1,1),
(5,1),
(7,1),
(2,2),
(11,2),
(3,3),
(11,4),
(11,5),
(5,6),
(6,7);
(2,8),
(4,9),
(8,10),
(9,9);

SELECT * FROM Rol;
SELECT * FROM Usuario;
SELECT * FROM Tipo_dispositivo;
SELECT * FROM Dispositivo;
SELECT * FROM Accion_Automatizacion;
SELECT * FROM Condicion_Automatizacion;
SELECT * FROM Automatizacion;
SELECT * FROM Dispositivo_Automatizacion;

-- Aca es donde aplicamos lo nuevo de la evidencia 6 que es las consultas multitablas y las subconsultas que pide el profe 

-- este permite conocer quien es el dueño del dispositivo que tiene asocidado
SELECT d.nombre_dispositivo, u.nombre_usuario, t.tipo_dispositivo
FROM Dispositivo d
JOIN Usuario u ON d.id_usuario = u.id_usuario
JOIN Tipo_dispositivo t ON d.id_tipo = t.id_tipo;

-- aca ve las automatizaciones que estan y que funcion van a ejecutar
SELECT a.nombre_automatizacion, d.nombre_dispositivo, ac.tipo_accion
FROM Automatizacion a
JOIN Dispositivo d ON a.id_dispositivo = d.id_dispositivo
JOIN Accion_Automatizacion ac ON a.id_accion = ac.id_accion
WHERE a.estado_automatizacion = 'activa';

-- en este vemos los usuarios con la cantidad de los dispositivos que tienen asocidados
SELECT u.nombre_usuario, COUNT(d.id_dispositivo) AS total_dispositivos
FROM Usuario u
LEFT JOIN Dispositivo d ON u.id_usuario = d.id_usuario
GROUP BY u.nombre_usuario;

-- y aca por ultimo permite ver el nombre del dispositivo, la automatizacion y la condicion que tienen asociados
SELECT d.nombre_dispositivo, au.nombre_automatizacion, c.tipo_condicion
FROM Dispositivo d
JOIN Dispositivo_Automatizacion da ON d.id_dispositivo = da.id_dispositivo
JOIN Automatizacion au ON da.id_automatizacion = au.id_automatizacion
JOIN Condicion_Automatizacion c ON au.id_condicion = c.id_condicion;

-- aca van las subconsultas 

-- en esta se muestran los dispositivos que no tienen una automatizacion asignada
SELECT nombre_dispositivo
FROM Dispositivo
WHERE id_dispositivo NOT IN (
    SELECT DISTINCT id_dispositivo
    FROM Dispositivo_Automatizacion
);

-- aca por ejemplo si alguna automatizacion se activa con la condificon que pusimos antes 'al anochecer'
SELECT nombre_automatizacion
FROM Automatizacion
WHERE id_condicion = (
    SELECT id_condicion
    FROM Condicion_Automatizacion
    WHERE tipo_condicion = 'al anochecer'
);

-- y en este los dispositivos que tienen las automatizaciones activas
SELECT nombre_dispositivo
FROM Dispositivo
WHERE id_dispositivo IN (
    SELECT id_dispositivo
    FROM Automatizacion
    WHERE estado_automatizacion = 'activa'
);

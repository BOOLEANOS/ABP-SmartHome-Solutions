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

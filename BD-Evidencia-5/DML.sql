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
('camara'),
('electrodomestico');

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
('Calefactor', 'habitacion','encendido',2,2)
;

INSERT INTO Accion_Automatizacion (tipo_accion) VALUES 
('encender'),
('apagar'),
('ajustar'),
('suspender'),
('acutalizar');

INSERT INTO Condicion_Automatizacion (tipo_condicion) VALUES 
('al anochecer'),
('temperatura menor a 10celcius'),
('movimiento detectado'),
('hora exacta 22:00pm'),
('activar opcion'),
('finalizado horario trabajo');


INSERT INTO Automatizacion (nombre_automatizacion, estado_automatizacion, id_condicion, id_dispositivo, id_accion) VALUES
('Modo Noche','activa',1,1,5),
('Modo Ahorro','inactiva',1,4,4),
('Notificacion Movimiento','activa',3,3,3);

INSERT INTO Dispositivo_Automatizacion (id_dispositivo, id_automatizacion) VALUES
(1,1),
(5,1),
(7,1),
(2,2),
(11,2),
(3,3);

SELECT * FROM Rol;
SELECT * FROM Usuario;
SELECT * FROM Tipo_dispositivo;
SELECT * FROM Dispositivo;
SELECT * FROM Accion_Automatizacion;
SELECT * FROM Condicion_Automatizacion;
SELECT * FROM Automatizacion;
SELECT * FROM Dispositivo_Automatizacion;

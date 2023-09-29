CREATE DATABASE Discord2;
USE Discord2;

-- Crear la tabla "Usuarios" para almacenar información de usuarios
CREATE TABLE Usuarios (
id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
apellido VARCHAR(50) NOT NULL, 
email VARCHAR(255) NOT NULL,
username VARCHAR(255) NOT NULL,
contraseña VARCHAR(255) NOT NULL,
fecha_nacimiento datetime,
ruta_imagen_perfil VARCHAR(100)
);

-- Crear la tabla "Servidores" para almacenar información de servidores
CREATE TABLE Servidores (
  id_servidor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  descripcion VARCHAR(255),
  fecha_creacion datetime NOT NULL
 
);

-- Creamos la tabla intermedia "Usuario_Servidor"  
CREATE TABLE Usuario_Servidor (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  servidor_id INT NOT NULL,
  rol VARCHAR(50),
  FOREIGN KEY (usuario_id) REFERENCES Usuarios(id_usuario),
  FOREIGN KEY (servidor_id) REFERENCES Servidores(id_servidor)
);

-- Crear la tabla "Canales" para almacenar información de canales  # BIEN
CREATE TABLE Canales (
  id_canal INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  servidor_id INT NOT NULL,
  FOREIGN KEY (servidor_id) REFERENCES Servidores (id_servidor)
);

-- Crear la tabla "Mensajes" para almacenar información de mensajes
CREATE TABLE Mensajes (
  id_mensaje INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  canal_id INT NOT NULL,
  usuario_id INT NOT NULL,
  contenido TEXT NOT NULL,
  fecha DATETIME NOT NULL,
  FOREIGN KEY (canal_id) REFERENCES Canales (id_canal),
  FOREIGN KEY (usuario_id) REFERENCES Usuarios (id_usuario)
);



-- Insertar un servidor
INSERT INTO discord2.Servidores (nombre, descripcion, fecha_creacion)
VALUES ('Nombre del Servidor', 'Descripción del Servidor', NOW());

-- Obtener el ID del servidor recién creado
SET @id_servidor = LAST_INSERT_ID();

-- Insertar un canal en el servidor
INSERT INTO discord2.Canales (nombre, servidor_id)
VALUES ('Nombre del Canal', @id_servidor);


-- Insertar al usuario 12 en el servidor y canal recién creados
INSERT INTO discord2.Usuario_Servidor (usuario_id, servidor_id, rol)
VALUES (12, @id_servidor, 'Miembro');

-- Insertar al usuario 14 en el servidor y canal recién creados
INSERT INTO discord2.Usuario_Servidor (usuario_id, servidor_id, rol)
VALUES (14, @id_servidor, 'Miembro');


-- Insertar un mensaje del usuario 1 en el servidor 1
INSERT INTO Mensajes (canal_id, usuario_id, contenido, fecha)
VALUES (1, 1, 'Hola, soy el usuario 1 en este servidor', NOW());

-- Insertar un mensaje del usuario 2 en el servidor 1
INSERT INTO Mensajes (canal_id, usuario_id, contenido, fecha)
VALUES (1, 2, 'Hola, soy el usuario 2 en este servidor', NOW());
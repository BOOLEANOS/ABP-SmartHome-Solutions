
# SmartHome Solutions – Sistema de Gestión de Dispositivos Inteligentes

El propósito de este proyecto es desarrollar una aplicación de consola que permita gestionar dispositivos inteligentes dentro de un hogar.
El sistema posibilita registrar usuarios, controlar dispositivos (encendido, apagado y configuración), y ejecutar automatizaciones simples, aplicando principios de Programación Orientada a Objetos (POO) y el patrón de diseño DAO (Data Access Object) para mantener una arquitectura modular, escalable y mantenible.

El proyecto se desarrolla para la empresa SmartHome Solutions, la cual busca ofrecer una solución centralizada para administrar diversos dispositivos del hogar.
La aplicación se apoya en una base de datos relacional que almacena la información de usuarios y dispositivos, cumpliendo y priorizando los principios de seguridad, fiabilidad, eficiencia de rendimiento y sostenibilidad.

En cuanto al alcance del proyecto, se ha logrado revisar y mejorar clases de dominio como son usuarios, dispositivos y automatizaciones.
Se implementó el patrón DAO para separar la lógica de acceso a datos. Se ha logrado que se puedan registrar usuarios (tanto admin como estandar), que se puedan listar y gestionar dispositivos y activar/desactivar automatizaciones en los ultimos. Se mantienen vigentes, ademas, las pruebas unitarias, garantizando la integridad del código.
El programa de consola (main.py) implementa las siguientes funcionalidades, utilizando el patrón DAO para interactuar con la Base de Datos:
1. Usuario estandar: Registro e inicio de sesión seguro. Consultar datos personales. 
2. Usuario administrador (admin): Registro e inicio de sesión seguro. Cambio de rol y gestion de dispositivos.
3. Base de datos: conexion con MySQL. Inserciones y consultas mediante scripts.

Tecnologías Utilizadas:
Lenguaje: Python
Paradigma: Programación Orientada a Objetos (POO)
Patrón: Data Access Object (DAO)
Base de Datos: MySQL
Entorno: Consola
Gestión de código: GitHub

Autores:
Lorena Paola Pereyra,
Nancy Maribel Morales,
Tobias Joel Ruffino,
María Eugenia Barrios



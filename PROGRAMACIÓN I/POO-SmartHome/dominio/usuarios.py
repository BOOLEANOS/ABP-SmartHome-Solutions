# usuarios.py

class Usuario:
    def __init__(self, id, nombre, correo, contrasena, rol):
        self.__id = id
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasena = contrasena
        self.__rol = rol

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_contrasena(self):
        return self.__contrasena

    def get_rol(self):
        return self.__rol

    def set_id(self, id):
        self.__id = id

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_correo(self, correo):
        self.__correo = correo

    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena

    def set_rol(self, rol):
        self.__rol = rol

    def mostrar_datos(self): 
        print(f"Nombre: {self.__nombre}\n"
              f"Correo: {self.__correo}\n"
              f"Contraseña: {self.__contrasena}\n"
              f"Rol: {self.__rol}\n")
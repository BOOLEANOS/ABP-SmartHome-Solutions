# usuarios.py

class Usuario:
    def __init__(self, nombre, correo, contrasena, rol):
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasena = contrasena
        self.__rol = rol


    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_contrasena(self):
        return self.__contrasena

    def get_rol(self):
        return self.__rol

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
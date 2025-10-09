# usuarios.py

class Usuario:
    def __init__(self, id, nombre, correo, contrasena, rol):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol

    def mostrar_datos(self): 
        print(f"Nombre: {self.nombre}\n"
              f"Correo: {self.correo}\n"
              f"Contraseña: {self.contrasena}\n"
              f"Rol: {self.rol}\n")
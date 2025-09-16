# gestion_usuarios.py
import re
from usuarios import Usuario

class GestionDeUsuarios:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def __validar_correo(self):
        while True:
            correo_valido = input("Ingrese su correo: ")
            pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if re.match(pattern, correo_valido):
                break
            else:
                print("Formato del correo inválido. Por favor, intentelo nuevamente.")
        return correo_valido
    
    def __validar_largo_texto(self, texto, min, max):
        while True:
            user_input = input(texto)
            input_length = len(user_input)

            if min <= input_length <= max:
                return user_input
            else:
                print(f"Input invalido. El texto debe contener entre {min} y {max} caracteres.")
    
    def registrar_usuario(self):
        
        nombre = self.__validar_largo_texto("Ingrese su nombre: ", 2, 20)
        correo = self.__validar_correo()
        contrasena = self.__validar_largo_texto("Cree una contraseña: ", 8, 20)
        
        rol = "admin" if not self.usuarios else "usuario"
        nuevo_id = len(self.usuarios) + 1
        
        nuevo_usuario = Usuario(nuevo_id, nombre, correo, contrasena, rol)
        self.usuarios.append(nuevo_usuario)
        
        print(f"Usuario {nombre} registrado con éxito como {'Administrador' if rol == 'admin' else 'Usuario'}.")

    def iniciar_sesion(self):
        correo = input("Correo: ")
        contrasena = input("Contraseña: ")
        for usuario in self.usuarios:
            if usuario.correo == correo and usuario.contrasena == contrasena:
                print("Inicio de sesión exitoso.")
                return usuario
        print("Credenciales incorrectas.")
        return None

    def modificar_rol_usuario(self):
        correo = input("Correo del usuario a modificar: ")
        for usuario in self.usuarios:
            if usuario.correo == correo:
                nuevo_rol = input("Nuevo rol (admin / estandar): ").lower()
                if nuevo_rol in ["admin", "estandar"]:
                    usuario.rol = nuevo_rol
                    print(f"Rol actualizado a {nuevo_rol}.")
                else:
                    print("Rol inválido.")
                return
        print("Usuario no encontrado.")

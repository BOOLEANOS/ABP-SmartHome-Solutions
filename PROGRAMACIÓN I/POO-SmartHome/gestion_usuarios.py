# gestion_usuarios.py
import re
from dominio.usuarios import Usuario

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
        
        nuevo_usuario = Usuario(nombre, correo, contrasena, rol)
        self.usuarios.append(nuevo_usuario)
        
        print(f"Usuario {nombre} registrado con éxito como {'Administrador' if rol == 'admin' else 'Usuario'}.")

    def iniciar_sesion(self):
        correo = input("Correo: ")
        contrasena = input("Contraseña: ")
        for usuario in self.usuarios:
            if usuario.get_correo() == correo and usuario.get_contrasena() == contrasena:
                print("Inicio de sesión exitoso.")
                return usuario
        print("Credenciales incorrectas.")
        return None

    def modificar_rol_usuario(self):
        correo = input("Correo del usuario a modificar: ")
        for usuario in self.usuarios:
            if usuario.get_correo() == correo:
                nuevo_rol = input("Nuevo rol (admin / estandar): ").lower()
                if nuevo_rol in ["admin", "estandar"]:
                    usuario.set_rol(nuevo_rol)
                    print(f"Rol actualizado a {nuevo_rol}.")
                    return usuario
                else:
                    print("Rol inválido.")
                return None
        print("Usuario no encontrado.")
        
    def listar_usuarios(self):
        if not self.usuarios:
            print("No se encuentran los usuarios registrados")
            return

        for usuario in self.usuarios:
            usuario.mostrar_datos()

    def eliminar_usuario(self):
        correo = input("Ingrese el correo del usuario a eliminar: ")
        for usuario in self.usuarios:
            if usuario.get_correo() == correo:
                self.usuarios.remove(usuario)
                print("Se elimino el usuario de manera existosa")
                return
        print("No se encuentra el usuario")

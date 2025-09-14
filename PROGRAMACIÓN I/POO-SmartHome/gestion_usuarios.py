# gestion_usuarios.py
from usuarios import Usuario

class GestionDeUsuarios:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def registrar_usuario(self):
        nombre = input("Ingrese su nombre: ")
        correo = input("Ingrese su correo: ")
        contrasena = input("Cree una contraseña: ")
        
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

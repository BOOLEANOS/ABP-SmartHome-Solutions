# usuarios.py
def registrar_usuario(usuarios):
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contrasena = input("Contraseña: ")
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": nombre,
        "correo": correo,
        "contrasena": contrasena
    }
    usuarios.append(nuevo_usuario)
    print("Usuario registrado con éxito.")

def iniciar_sesion(usuarios):
    correo = input("Correo: ")
    contrasena = input("Contraseña: ")
    for usuario in usuarios:
        if usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            print("Inicio de sesión exitoso.")
            return usuario
    print("Credenciales incorrectas.")
    return None
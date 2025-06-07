# usuarios.py
def registrar_usuario(usuarios):
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    contrasena = input("Cree una contraseña: ")

    rol = "admin" if not usuarios else "usuario"
    usuarios.append({
        "id": len(usuarios) + 1,
        "nombre": nombre,
        "correo": correo,
        "contrasena": contrasena,
        "rol": rol
    })

    print(f"Usuario {nombre} registrado con éxito como {'Administrador' if rol == 'admin' else 'Usuario'}.")

def iniciar_sesion(usuarios):
    correo = input("Correo: ")
    contrasena = input("Contraseña: ")
    for usuario in usuarios:
        if usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            print("Inicio de sesión exitoso.")
            return usuario
    print("Credenciales incorrectas.")
    
def modificar_rol_usuario(usuarios):
    correo = input("Correo del usuario a modificar: ")
    for u in usuarios:
        if u["correo"] == correo:
            nuevo_rol = input("Nuevo rol (admin / estándar): ").lower()
            if nuevo_rol in ["admin", "estándar"]:
                u["rol"] = nuevo_rol
                print(f"Rol actualizado a {nuevo_rol}.")
            else:
                print("Rol inválido.")
            return
    print("Usuario no encontrado.")
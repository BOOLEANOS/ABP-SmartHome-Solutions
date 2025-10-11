# test_mymodule.py
import pytest
from usuarios import Usuario

def test_usuario_init():
    usuario = Usuario(id=1, nombre="Test User", correo="test@example.com", contrasena="password123", rol="usuario")
    
    assert usuario.get_id() == 1
    assert usuario.get_nombre() == "Test User"
    assert usuario.get_correo() == "test@example.com"
    assert usuario.get_contrasena() == "password123"
    assert usuario.get_rol() == "usuario"

def test_mostrar_usuario(capsys):
    usuario = Usuario(id=1, nombre="Test User", correo="test@example.com", contrasena="password123", rol="usuario")

    usuario.mostrar_datos()
    datos_capturados = capsys.readouterr()
    datos_esperados = (
        "Nombre: Test User\n"
        "Correo: test@example.com\n"
        "Contraseña: password123\n"
        "Rol: usuario\n\n"
    )
    assert datos_capturados.out == datos_esperados

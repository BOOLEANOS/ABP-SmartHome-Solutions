import pytest
from usuarios import Usuario
from gestion_usuarios import GestionDeUsuarios
from unittest.mock import patch

# Fixture para una instancia de GestionDeUsuarios con usuarios predefinidos
@pytest.fixture
def gestion_con_usuarios():
    usuarios_existentes = [
        Usuario(1, "Ana", "ana@example.com", "ana123", "admin"),
        Usuario(2, "Pedro", "pedro@example.com", "pedro123", "estandar")
    ]
    return GestionDeUsuarios(usuarios_existentes)


@patch('builtins.input', side_effect=['Carlos', 'carlos@example.com', 'carlos123'])
def test_registrar_usuario_como_estandar(mock_input, gestion_con_usuarios, capsys):
    gestion_con_usuarios.registrar_usuario()
    datos_capturados = capsys.readouterr()
    
    assert len(gestion_con_usuarios.usuarios) == 3
    nuevo_usuario = gestion_con_usuarios.usuarios[-1]
    assert nuevo_usuario.nombre == "Carlos"
    assert nuevo_usuario.rol == "usuario"
    assert "registrado con éxito como Usuario" in datos_capturados.out

@patch('builtins.input', side_effect=['Admin', 'admin@example.com', 'adminpass'])
def test_registrar_usuario_como_admin(mock_input, capsys):
    gestion_vacia = GestionDeUsuarios([])
    gestion_vacia.registrar_usuario()
    datos_capturados = capsys.readouterr()
    
    assert len(gestion_vacia.usuarios) == 1
    primer_usuario = gestion_vacia.usuarios[0]
    assert primer_usuario.nombre == "Admin"
    assert primer_usuario.rol == "admin"
    assert "registrado con éxito como Administrador" in datos_capturados.out

@patch('builtins.input', side_effect=['a', 'NombreParaPrueba', 'prueba@test.com', 'Password123'])
def test_registrar_usuario_con_nombre_invalido(mock_input, capsys):
    gestion_vacia = GestionDeUsuarios([])
    gestion_vacia.registrar_usuario()
    captured = capsys.readouterr()
    
    assert "Input invalido. El texto debe contener entre 2 y 20 caracteres." in captured.out
    assert gestion_vacia.usuarios[0].nombre == "NombreParaPrueba"

@patch('builtins.input', side_effect=['NombreParaPrueba', 'prueba@', 'prueba@test.com', 'Password123'])
def test_registrar_usuario_con_correo_invalido(mock_input, capsys):
    gestion_vacia = GestionDeUsuarios([])
    gestion_vacia.registrar_usuario()
    captured = capsys.readouterr()
    
    assert "Formato del correo inválido. Por favor, intentelo nuevamente." in captured.out
    assert gestion_vacia.usuarios[0].correo == "prueba@test.com"

@patch('builtins.input', side_effect=['NombreParaPrueba', 'prueba@test.com', '123', 'Password123'])
def test_registrar_usuario_con_contrasena_invalido(mock_input, capsys):
    gestion_vacia = GestionDeUsuarios([])
    gestion_vacia.registrar_usuario()
    captured = capsys.readouterr()
    
    assert "Input invalido. El texto debe contener entre 8 y 20 caracteres." in captured.out
    assert gestion_vacia.usuarios[0].contrasena == "Password123"

@patch('builtins.input', side_effect=['ana@example.com', 'ana123'])
def test_iniciar_sesion_exitoso(mock_input, gestion_con_usuarios, capsys):
    usuario_logueado = gestion_con_usuarios.iniciar_sesion()
    datos_capturados = capsys.readouterr()
    
    assert usuario_logueado is not None
    assert usuario_logueado.correo == "ana@example.com"
    assert usuario_logueado.contrasena == "ana123"
    assert "Inicio de sesión exitoso." in datos_capturados.out

@patch('builtins.input', side_effect=['ana@example.com', 'incorrecta'])
def test_iniciar_sesion_contrasena_incorrecta(mock_input, gestion_con_usuarios, capsys):
    usuario_logueado = gestion_con_usuarios.iniciar_sesion()
    datos_capturados = capsys.readouterr()
    
    assert usuario_logueado is None
    assert "Credenciales incorrectas." in datos_capturados.out

@patch('builtins.input', side_effect=['inexistente@example.com', 'password'])
def test_iniciar_sesion_usuario_no_encontrado(mock_input, gestion_con_usuarios, capsys):
    usuario_logueado = gestion_con_usuarios.iniciar_sesion()
    datos_capturados = capsys.readouterr()
    
    assert usuario_logueado is None
    assert "Credenciales incorrectas." in datos_capturados.out


@patch('builtins.input', side_effect=['ana@example.com', 'estandar'])
def test_modificar_rol_exitoso(mock_input, gestion_con_usuarios, capsys):
    gestion_con_usuarios.modificar_rol_usuario()
    datos_capturados = capsys.readouterr()
    
    usuario_modificado = gestion_con_usuarios.usuarios[0]
    assert usuario_modificado.rol == "estandar"
    assert "Rol actualizado a estandar." in datos_capturados.out

@patch('builtins.input', side_effect=['pedro@example.com', 'invalido'])
def test_modificar_rol_invalido(mock_input, gestion_con_usuarios, capsys):
    gestion_con_usuarios.modificar_rol_usuario()
    datos_capturados = capsys.readouterr()
    
    usuario_no_modificado = gestion_con_usuarios.usuarios[1]
    assert usuario_no_modificado.rol == "estandar"
    assert "Rol inválido." in datos_capturados.out

@patch('builtins.input', side_effect=['inexistente@example.com', 'admin'])
def test_modificar_rol_usuario_no_encontrado(mock_input, gestion_con_usuarios, capsys):
    gestion_con_usuarios.modificar_rol_usuario()
    datos_capturados = capsys.readouterr()
    
    assert "Usuario no encontrado." in datos_capturados.out

def test_listar_usuarios_muestra_todos(capsys, gestion_con_usuarios):
    gestion_con_usuarios.listar_usuarios()
    datos = capsys.readouterr()

    assert "Ana" in datos.out
    assert "Pedro" in datos.out

def test_listar_usuarios_vacio(capsys):
    gestion_vacia = GestionDeUsuarios([])
    gestion_vacia.listar_usuarios()
    datos = capsys.readouterr()

    assert "No se encuentran los usuarios registrados" in datos.out

def test_eliminar_usuario_existente(mock_input, gestion_con_usuarios, capsys):
    gestion_con_usuarios.eliminar_usuario()
    datos = capsys.readouterr()

    assert len(gestion_con_usuarios.usuarios) == 1
    assert "Se elimino el usuario de manera existosa" in datos.out

def test_eliminar_usuario_inexistente(mock_input, gestion_con_usuarios, capsys):
    gestion_con_usuarios.eliminar_usuario()
    datos = capsys.readouterr()

    assert "No se encuentra el usuario" in datos.out

import pytest
from dispositivos import Dispositivo

def test_constructor_dispositivo():
    dispositivo = Dispositivo(
        id_dispositivo=1,
        nombre_dispositivo="Sensor de temperatura",
        ubicacion="Sala",
        estado_dispositivo="activo",
        id_tipo=2,
        id_usuario=5
    )
    
    assert dispositivo.id_dispositivo == 1
    assert dispositivo.nombre_dispositivo == "Sensor de temperatura"
    assert dispositivo.ubicacion == "Sala"
    assert dispositivo.estado_dispositivo == "activo"
    assert dispositivo.id_tipo == 2
    assert dispositivo.id_usuario == 5
    
def test_setters_dispositivo():
    dispositivo = Dispositivo(
        id_dispositivo=1,
        nombre_dispositivo="Sensor de temperatura",
        ubicacion="Sala",
        estado_dispositivo="activo",
        id_tipo=2,
        id_usuario=5
    )
    
    dispositivo.nombre_dispositivo = "Sensor de humedad"
    dispositivo.ubicacion = "Cocina"
    dispositivo.estado_dispositivo = "inactivo"
    dispositivo.id_tipo = 3
    dispositivo.id_usuario = 6
    
    assert dispositivo.nombre_dispositivo == "Sensor de humedad"
    assert dispositivo.ubicacion == "Cocina"
    assert dispositivo.estado_dispositivo == "inactivo"
    assert dispositivo.id_tipo == 3
    assert dispositivo.id_usuario == 6
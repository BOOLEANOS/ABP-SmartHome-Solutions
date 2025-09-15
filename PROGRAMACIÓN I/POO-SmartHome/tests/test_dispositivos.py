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
    
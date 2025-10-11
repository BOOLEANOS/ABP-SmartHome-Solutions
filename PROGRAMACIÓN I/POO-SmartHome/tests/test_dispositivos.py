import pytest
from dispositivos import Dispositivo

def test_constructor_dispositivo():
    dispositivo = Dispositivo(
        id=1,
        nombre="Sensor de temperatura",
        ubicacion="Sala",
        estado="activo",
        tipo=2,
    )
    
    assert dispositivo.get_id() == 1
    assert dispositivo.get_nombre() == "Sensor de temperatura"
    assert dispositivo.get_ubicacion() == "Sala"
    assert dispositivo.get_estado() == "activo"
    assert dispositivo.get_tipo() == 2
    
def test_setters_dispositivo():
    dispositivo = Dispositivo(
        id=1,
        nombre="Sensor de temperatura",
        ubicacion="Sala",
        estado= True,
        tipo=2
    )
    
    dispositivo.set_nombre("Sensor de humedad")
    dispositivo.set_ubicacion("Cocina") 
    dispositivo.set_tipo(2)
    
    assert dispositivo.get_nombre() == "Sensor de humedad"
    assert dispositivo.get_ubicacion() == "Cocina"
    assert dispositivo.get_tipo() == 2

def test_encender_apagar():
    dispositivo = Dispositivo(1, "Lámpara", "Oficina", False, 2)
    
    dispositivo.encender()
    assert dispositivo.get_estado() is True

    dispositivo.apagar()
    assert dispositivo.get_estado() is False

def test_str_dispositivo_encendido():
    dispositivo = Dispositivo(1, "Ventilador", "Dormitorio", True, 2)
    assert str(dispositivo) == "Dispositivo(ID: 1, Nombre: Ventilador, Ubicación: Dormitorio, Estado: Encendido, Tipo: 2)"

def test_str_dispositivo_apagado():
    dispositivo = Dispositivo(2, "Ventilador", "Dormitorio", False, 2)
    assert str(dispositivo) == "Dispositivo(ID: 2, Nombre: Ventilador, Ubicación: Dormitorio, Estado: Apagado, Tipo: 2)"

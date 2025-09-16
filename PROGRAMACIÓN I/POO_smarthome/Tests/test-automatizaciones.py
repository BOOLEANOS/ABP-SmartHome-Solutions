# test_automatizacion.py
import pytest
from poo_smarthome.automatizaciones import Automatizacion

def test_ejecutar_condicion_true(capsys):
    accion_llamada = []

    def accion():
        accion_llamada.append(True)

    auto = Automatizacion(
        id=1,
        nombre="Encender luces",
        condicion=lambda ctx: True,
        acciones=[accion]
    )

    auto.ejecutar(contexto={})
    captured = capsys.readouterr()

    assert "Ejecutando automatización: Encender luces" in captured.out
    assert True in accion_llamada


def test_ejecutar_condicion_false(capsys):
    accion_llamada = []

    def accion():
        accion_llamada.append(True)

    auto = Automatizacion(
        id=2,
        nombre="Apagar luces",
        condicion=lambda ctx: False,
        acciones=[accion]
    )

    auto.ejecutar(contexto={})
    captured = capsys.readouterr()

    assert "No se cumple la condición de: Apagar luces" in captured.out
    assert accion_llamada == []



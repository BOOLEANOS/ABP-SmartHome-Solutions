# test_automatizacion.py
import unittest
from POO_smarthome.automatizaciones import Automatizacion

class TestAutomatizacion(unittest.TestCase):

    def test_condicion_true_ejecucion_accion(self):
        # Variable para verificar si la acción se ejecutó
        self.accion_ejecutada = False

        def accion():
            self.accion_ejecutada = True

        automatizacion = Automatizacion(
            id=1,
            nombre="Test Accion True",
            condicion=True,
            acciones=[accion]
        )

        automatizacion.ejecutar()
        self.assertTrue(self.accion_ejecutada)

    def test_condicion_false_no_ejecucion(self):
        self.accion_ejecutada = False

        def accion():
            self.accion_ejecutada = True

        automatizacion = Automatizacion(
            id=2,
            nombre="Test Accion False",
            condicion=False,
            acciones=[accion]
        )

        automatizacion.ejecutar()
        self.assertFalse(self.accion_ejecutada)


if __name__ == "__main__":
    unittest.main()
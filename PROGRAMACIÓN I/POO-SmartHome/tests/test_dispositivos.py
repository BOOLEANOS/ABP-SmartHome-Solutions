import unittest
from dispositivos import Dispositivo
class TestDispositivo(unittest.TestCase):

    def setUp(self):
        
        self.dispositivo = Dispositivo(
            id_dispositivo=1,
            nombre_dispositivo="Sensor de temperatura",
            ubicacion="Sala",
            estado_dispositivo="activo",
            id_tipo=2,
            id_usuario=5
        )
        
    def test_atributos_dispositivo(self):
        self.assertEqual(self.dispositivo.id_dispositivo, 1)
        self.assertEqual(self.dispositivo.nombre_dispositivo, "Sensor de temperatura")
        self.assertEqual(self.dispositivo.ubicacion, "Sala")
        self.assertEqual(self.dispositivo.estado_dispositivo, "activo")
        self.assertEqual(self.dispositivo.id_tipo, 2)
        self.assertEqual(self.dispositivo.id_usuario, 5)

if __name__ == '__main__':
    print("Ejecutando pruebas de la clase Dispositivo...\n")
    unittest.main()

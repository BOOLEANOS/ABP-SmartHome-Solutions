
class Dispositivo: 
  def __init__(self, id, nombre, tipo, estado=True, usuario_id=None):
    self.id = id
    self.nombre = nombre
    self.tipo = tipo
    self.estado = estado
    self.usuario_id = usuario_id

  def mostrar_info(self):
    estado_str = "Encendido" if self.estado else "Apagado"
    print(f"ID: {self.id} | Nombre: {self.nombre} | Tipo: {self.tipo} | Estado: {estado_str}")

class GestionDispositivos:
  def __init__(self):
    self.dispositivos = []
    

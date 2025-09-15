class Dispositivo:
  def __init__(self, id, nombre, tipo, estado=True, usuario_id-None):
    self.id = id
    self.nombre = nombre
    self.tipo = tipo
    self.estado = estado
    self.usuario_id = usuario_id

  def mostrar_info(self):
    estado_str = "Encendido" if self.estado else "Apagado"
    print(f"ID: {self.id} | Nombre: {self.nombre} | Tipo: {self.tipo} | Estado: {self.estado_str}")

class GestionDispositivos:
  def __init__(self):
    self.dispositivos = []

  def crear_dispositivo(self, usuario_id):
    nombre = input("Nombre del dispositivo creado: ")
    tipo = input("Tipo de dispositivo (luz, camara, termostato, electrodomestico, etc.): ")

    if not nombre or not tipo:
      print("Nombre y tipo son cruciales")
      return

    for d in self.dispositivos:
      if d.nombre.lower() == nombre.lower () and d.usuario_id == usuario_id:
      print("El nombre ya esta ocupado, porfavor tenes que ingresar otro.")
      return


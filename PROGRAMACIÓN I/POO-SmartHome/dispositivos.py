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

      nuevo_dispositivo = Dispositivo(
        id=len(self.dispositivos) + 1,
        nombre=nombre,
        tipo=tipo,
        estado=True,
        usuario_id=usuario_id
      )
      self.dispositivos.append(nuevo_dispositivo)
      print(f"El Dispositivo '{nombre}' fue agregado.")

  def mostrar_dispositivos_usuario(self, usuario_id):
      print("\nDispositivo registrtado:")
      encontrados = [d for d in self.dispositivos if d.usuario_id == usuario_id]

      if not encontrados:
        print("No existe dispositivo registrado amigo.")
        return
      
      for idx, d in enumerate(encontrados, 1):
        print(f"{idx}. {d.nombre} ({d.tipo}) - Estado: {'encendido' if d.estado else 'apagado'}")

  def eliminar_dispositivo_por_nombre(self, usuario_id):
    nombre = input("Ingrese el nombre que queres borrar: ")

    for d in self.dispositivos:
      if d.nombre.lower() == nombre.lower() and d.usuario_id == usuario_id:
        self.dispositivos.remove(d)
        print(f"El dispositivo '{nombre}' fue borrado.")
        return
    print("El dispositivo no se encuentra")

  def cambiar_estado_dispositivo(self, usuario_id, estado):
    nombre = input("Introduce el nombre de su dispositivo")

    for d in self.dispositivos:
      if d.nombre.lower() == nombre.lower() and d.usuario_id == usuario_id:
        d.estado = estado
        print("el dispositivo se activo de manera correcta." if estado else "el dispositivo se desactivo de manera correcta")
        return
  def buscar_dispositivo(self, criterio, usuario_id):
    for d in self.dispositivos:
      if d.usuario_id == usuario_id and (str(d.id) == str(criterio) or d.nombre.lower() == criterio.lower()):
        print("el dispositivo fue encontrado")
        d.mostrar_info()
        return d
    print("el dispositivo no fue encontrado")
    return None
    
        
        
                                                      




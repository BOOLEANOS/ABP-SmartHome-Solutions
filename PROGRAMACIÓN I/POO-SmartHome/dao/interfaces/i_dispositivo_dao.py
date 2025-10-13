class IDispositivoDAO:
  
    def crear_dispositivo(self, dispositivo: Dispositivo):
        """Crea un nuevo dispositivo en la base de datos."""
        pass

    def obtener_todos(self):
        """Obtiene todos los dispositivos almacenados."""
        pass

    def obtener_por_id(self, id_dispositivo: int):
        """Obtiene un dispositivo por su ID."""
        pass

    def actualizar_dispositivo(self, dispositivo: Dispositivo):
        """Actualiza los datos de un dispositivo existente."""
        pass
      
    def eliminar_dispositivo(self, id_dispositivo: int):
        """Elimina un dispositivo según su ID."""
        pass

from ..database import DatabaseConnection
from .exceptions import NotFound, InvalidDataError
class Mensaje:
    """Mensaje model class"""

    def __init__(self, id_mensaje = None, 
                 canal_id = None, 
                 usuario_id = None, 
                 contenido = None, 
                 fecha = None 
                ):
        
        
        """Constructor method"""
        self.id_mensaje = id_mensaje
        self.canal_id = canal_id
        self.usuario_id = usuario_id
        self.contenido = contenido
        self.fecha = fecha


    def serialize(self):
        """Serialize object representation
        Returns:
            dict: Object representation
        Note:

        """
   
        return {
            "id_mensaje": self.id_mensaje,
            "canal_id": self.canal_id,
            "usuario_id": self.usuario_id,
            "contenido": self.contenido,
            "fecha": str(self.fecha)
        }
    
    @classmethod
    def get(cls, mensaje):
        """Get a mensaje by id
        Args:
            - mensaje (Mensaje): Mensaje object with the id attribute
        Returns:
            - Mensaje: Mensaje object
        """

        query = """SELECT id_mensaje, canal_id, usuario_id, contenido, fecha
        FROM discord2.mensajes WHERE id_mensaje = %s"""

        params = mensaje.id_mensaje,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        
        raise NotFound(mensaje.id_mensaje) #MENSAJE
    
    
    @classmethod
    def get_all(cls):
        """Get all mensajes
        Returns:
            - list: List of Mensajes objects
        """
        query = """SELECT id_mensajes, canal_id, usuario_id, contenido, fecha
        FROM discord2.mensajes"""
        results = DatabaseConnection.fetch_all(query)

        mensajes = []
        if results is not None:
            for result in results:
                mensajes.append(cls(*result))
        return mensajes


    @classmethod
    def create(cls, mensaje):
        """Create a new mensaje
        Args:
            - mensajes (Mensajes): Mensaje object

        Raises:
            - InvalidDataError: If input data is not valid
      
        """
        
        # Construir la consulta SQL
        query = """INSERT INTO discord2.mensajes (canal_id, usuario_id, contenido, fecha) 
        VALUES (%s, %s, %s, %s)"""
        
  

        params = mensaje.canal_id, mensaje.usuario_id, mensaje.contenido, mensaje.fecha
   
        
        try:
            # Ejecutar la consulta SQL
            DatabaseConnection.execute_query(query, params=params)
        except Exception as e:
            # Puedes manejar cualquier excepción de la base de datos aquí
            raise InvalidDataError("Failed to create mensaje")
        

   

    @classmethod
    def update(cls, mensaje):
        """Update a mensaje
        Args:
            - mensaje (Mensaje): Mensaje object
        """
        allowed_columns = {'canal_id', 'usuario_id', 'contenido','fecha' }
                           


        query_parts = []
        params = []
        for key, value in mensaje.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(mensaje.id_mensaje)

        query = "UPDATE discord2.menaje SET " + ", ".join(query_parts) + " WHERE id_mensaje = %s"
        DatabaseConnection.execute_query(query, params=params)

    
    @classmethod
    def delete(cls, mensaje):
        """Delete a mensaje
        Args:
            - mensaje (Mensaje): Mensaje object with the id attribute
        """
        query = "DELETE FROM discord2.mensajes WHERE id_mensaje = %s"
        params = mensaje.id_mensaje,
        DatabaseConnection.execute_query(query, params=params)




    @classmethod
    def get_by_id_canal(cls, id_canal):
        """Filter get id_canal
        Returns:
            - list: List of Servidor objects
        """
        query = """
               SELECT * FROM discord2.Mensajes WHERE canal_id = %s"""
        
        params = (id_canal,)

        results = DatabaseConnection.fetch_all(query, params=params)

        mensajes = []
        if results is not None:
            for result in results:
                mensajes.append(cls(*result))
        return mensajes
    

    #url avatar, username, fecha, mensaje
            
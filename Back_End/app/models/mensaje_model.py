from ..database import DatabaseConnection
from .exceptions import FilmNotFound, InvalidDataError
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
        
        raise FilmNotFound(mensaje.id_mensaje) #MENSAJE
    
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

        # Validaciones de datos de entrada, EJERCICIO N° 2
        # if len(film.title) < 3:
        #     raise InvalidDataError("Title must have at least three characters")
        
        # if not isinstance(film.language_id, int) or not isinstance(film.rental_duration, int):
        #     raise InvalidDataError("Invalid data types for some attributes")
        
        # if film.special_features is not None and (not isinstance(film.special_features, list) \
        #         or not all(isinstance(feature, str) for feature in film.special_features) \
        #         or not all(feature in ["Trailers", "Commentaries", "Deleted Scenes", "Behind the Scenes"]
        #                     for feature in film.special_features)):
        #     raise InvalidDataError("Invalid special features")
       
        
        # Construir la consulta SQL
        query = """INSERT INTO discord2.mensajes (canal_id, usuario_id, contenido, fecha) 
        VALUES (%s, %s, %s, %s)"""
        
        # if film.special_features is not None:
        #     special_features = ','.join(film.special_features)
        # else:
        #     special_features = None

        params = mensaje.canal_id, mensaje.usuario_id, mensaje.contenido, mensaje.fecha
   
        
        try:
            # Ejecutar la consulta SQL
            DatabaseConnection.execute_query(query, params=params)
        except Exception as e:
            # Puedes manejar cualquier excepción de la base de datos aquí
            raise InvalidDataError("Failed to create mensaje")
        

    # def exists(self):
    #     # Verificar si el ID de la película existe en la base de datos
    #     return Film.query.filter_by(film_id=self.film_id).first() is not None    

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
        params.append(mensaje.film_id)

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
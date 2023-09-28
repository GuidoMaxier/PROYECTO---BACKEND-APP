from ..database import DatabaseConnection
from .exceptions import FilmNotFound, InvalidDataError


class Canal:
    """Canal model class"""

    def __init__(self, id_canal = None, 
                 nombre = None, 
                 servidor_id = None
                 ):
        
        
        """Constructor method"""
        self.id_canal = id_canal
        self.nombre = nombre
        self.servidor_id = servidor_id
  

    def serialize(self):
        """Serialize object representation
        Returns:
            dict: Object representation
        Note:

        """
        # if self.special_features is not None:
        #     special_features = list(self.special_features)
        # else:
        #     special_features = None
        return {
            "id_canal": self.id_canal,
            "nombre": self.nombre,
            "servidor_id": self.servidor_id
        }
    
    @classmethod
    def get(cls, canal_data):
        """Get a canal by id
        Args:
            - canal (Canal): Film object with the id attribute
        Returns:
            - Canal: Canal object
        """

        query = """SELECT id_canal, nombre, servidor_id 
        FROM discord2.canales WHERE id_canal = %s"""

        params = canal_data.id_canal,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        
        raise FilmNotFound(canal_data.id_canal) #CANAL
    
    
    @classmethod
    def get_all(cls):
        """Get all films
        Returns:
            - list: List of Canal objects
        """
        query = """SELECT id_canal, nombre, servidor_id
        FROM discord2.canales"""
        results = DatabaseConnection.fetch_all(query)

        films = []
        if results is not None:
            for result in results:
                films.append(cls(*result))
        return films


    @classmethod
    def create(cls, canal_data):
        """Create a new canal
        Args:
            - canal (Canal): Canal object

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
        query = """INSERT INTO discord2.canales (nombre, servidor_id) 
        VALUES (%s, %s)"""
        
        # if film.special_features is not None:
        #     special_features = ','.join(film.special_features)
        # else:
        #     special_features = None

        params = canal_data.nombre, canal_data.servidor_id

        
        try:
            # Ejecutar la consulta SQL
            DatabaseConnection.execute_query(query, params=params)
        except Exception as e:
            # Puedes manejar cualquier excepción de la base de datos aquí
            raise InvalidDataError("Failed to create canal")
        

    # def exists(self):
    #     # Verificar si el ID de la película existe en la base de datos
    #     return Film.query.filter_by(film_id=self.film_id).first() is not None    

    @classmethod
    def update(cls, canal_data):
        """Update a canal
        Args:
            - canal (Canal): Canal object
        """
        allowed_columns = {'nombre', 'servidor_id'}

        query_parts = []
        params = []

        for key, value in canal_data.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)

        params.append(canal_data.id_canal)

        if query_parts:
            query = f"UPDATE discord2.canales SET {', '.join(query_parts)} WHERE id_canal = %s"
            DatabaseConnection.execute_query(query, params=params)
        else:
            # No se proporcionaron datos válidos para actualizar
            raise InvalidDataError("No se proporcionaron datos válidos para actualizar el canal")
    
    @classmethod
    def delete(cls, canal_data):
        """Delete a canal
        Args:
            - canal (Canal): Canal object with the id attribute
        """
        query = "DELETE FROM discord2.canales WHERE id_canal = %s"
        params = canal_data.id_canal,
        DatabaseConnection.execute_query(query, params=params)


    @classmethod
    def check_nombre(cls, nombre):
        """verificamos que el nombre del servidor no este en uso"""
        
        query = "SELECT id_canal FROM discord2.canales WHERE nombre = %s"
        params = (nombre,)
        result = DatabaseConnection.fetch_one(query, params=params)
    
        return result
    

    @classmethod
    def get_by_id_server(cls, id_servidor):
        """Filter get id_usuario
        Returns:
            - list: List of Servidor objects
        """
        query = """
               SELECT *
                FROM discord2.Canales
                WHERE servidor_id = %s"""
        
        params = (id_servidor,)

        results = DatabaseConnection.fetch_all(query, params=params)

        canales = []
        if results is not None:
            for result in results:
                canales.append(cls(*result))
        return canales
        

    @classmethod
    def get_by_name_server(cls, nombre):
        """Filter get id_usuario
        Returns:
            - list: List of Servidor objects
        """
        query = """
               SELECT Canales.*
                FROM discord2.Canales
                INNER JOIN Servidores ON Canales.servidor_id = Servidores.id_servidor
                WHERE Servidores.nombre = %s"""
        
        params = (nombre,)

        results = DatabaseConnection.fetch_all(query, params=params)

        canales = []
        if results is not None:
            for result in results:
                canales.append(cls(*result))
        return canales    
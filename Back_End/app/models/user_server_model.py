from ..database import DatabaseConnection
from .exceptions import FilmNotFound, InvalidDataError

class UserServer:
    """User_Server model class"""

    def __init__(self, id = None, 
                 usuario_id = None, 
                 servidor_id = None, 
                 rol = None, 
                ):
        
        
        """Constructor method"""
        self.id = id
        self.usuario_id = usuario_id
        self.servidor_id = servidor_id
        self.rol = rol


    def serialize(self):
        """Serialize object representation
        Returns:
            dict: Object representation
        Note:
            - The last_update attribute is converted to string
            - The special_features attribute is converted to list if it is not
            null in the database. Otherwise, it is converted to None
            - The attributes rental_rate and replacement_cost are converted to 
            int, because the Decimal type may lose precision if we convert 
            it to float
        """
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "servidor_id": self.servidor_id,
            "rol":self.rol
        }
    

    @classmethod
    def get(cls, userserver):
        """Get a userserver by id
        Args:
            - userserver (UserServer): Film object with the id attribute
        Returns:
            - UserServer: UserServer object
        """

        query = """SELECT id, usuario_id, servidor_id, rol
        FROM discord2.usuario_servidor WHERE id = %s"""
        params = UserServer.id,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        
        raise FilmNotFound(UserServer.id) #TABLA INTERMEDIA
    
    
    @classmethod
    def get_all(cls):
        """Get all userservers
        Returns:
            - list: List of UserServer objects
        """
        query = """SELECT id, usuario_id, servidor_id, rol
        FROM discord2.usuario_servidor"""
        results = DatabaseConnection.fetch_all(query)

        userserver = []
        if results is not None:
            for result in results:
                userserver.append(cls(*result))
        return userserver


    @classmethod
    def create(cls, userserver):
        """Create a new userserver
        Args:
            - userserver(UserServer): UserServer object

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
        query = """INSERT INTO discord2.usuario_servidor (usuario_id, servidor_id, rol)
        VALUES (%s, %s, %s)"""
        


        params = userserver.usuario_id, userserver.servidor_id, userserver.rol
        
        try:
            # Ejecutar la consulta SQL
            DatabaseConnection.execute_query(query, params=params)
        except Exception as e:
            # Puedes manejar cualquier excepción de la base de datos aquí
            raise InvalidDataError("Failed to create tabla Usuario servidor")
        

    # def exists(self):
    #     # Verificar si el ID de la película existe en la base de datos
    #     return Film.query.filter_by(film_id=self.film_id).first() is not None    

    @classmethod
    def update(cls, userserver):
        """Update a userserver
        Args:
            - userserver (UserServer): UserServer object
        """
        allowed_columns = {'usuario_id', 'servidor_id', 'rol'}

        query_parts = []
        params = []
        for key, value in userserver.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(userserver.id)

        query = "UPDATE discord2.usuario_servidor SET " + ", ".join(query_parts) + " WHERE id = %s"
        DatabaseConnection.execute_query(query, params=params)

    
    @classmethod
    def delete(cls, userservidor):
        """Delete a userservidor
        Args:
            - userservidor (UserServidor): UserServidor object with the id attribute
        """
        query = "DELETE FROM discord2.usuario_servidor WHERE id = %s"
        params = userservidor.id,
        DatabaseConnection.execute_query(query, params=params)
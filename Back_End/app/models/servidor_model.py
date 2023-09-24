from ..database import DatabaseConnection
from .exceptions import FilmNotFound, InvalidDataError


class Servidor:
    """Servidor model class"""

    def __init__(self, id_servidor = None, 
                 nombre = None, 
                 descripcion = None, 
                 fecha_creacion = None, 
                ):
        
        
        """Constructor method"""
        self.id_servidor = id_servidor
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion


    def serialize(self):
        """Serialize object representation
        Returns:
            dict: Object representation
        Note:
 
        """

        return {
            "id_servidor": self.id_servidor,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "fecha_creacion": str(self.fecha_creacion)
        }



    @classmethod
    def get(cls, servidor_data):
        """Get a servidor by id
        Args:
            - servidor (Servidor): Film object with the id attribute
        Returns:
            - Servidor: Servidor object
        """

        query = """SELECT id_servidor, nombre, descripcion, fecha_creacion
        FROM discord2.servidor WHERE id_servidores = %s"""

        params = servidor_data.id_servidor,
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(*result)
        
        raise FilmNotFound(servidor_data.id_servidor) #servidor
    
    
    @classmethod
    def get_all(cls):
        """Get all servidores
        Returns:
            - list: List of Servidor objects
        """
        query = """SELECT id_servidor, nombre, descripcion, fecha_creacion
        FROM discord2.servidores"""

        results = DatabaseConnection.fetch_all(query)

        servidores = []
        if results is not None:
            for result in results:
                servidores.append(cls(*result))
        return servidores


    @classmethod
    def create(cls, servidor_data):
        """Create a new film
        Args:
            - servidor (Servidor): Film object

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
        query = """INSERT INTO discord2.servidores (nombre, descripcion, fecha_creacion) 
        VALUES (%s, %s, %s, %s)"""
        
        # if film.special_features is not None:
        #     special_features = ','.join(film.special_features)
        # else:
        #     special_features = None

        params = (servidor_data.id_servidor, servidor_data.descripcion, servidor_data.fecha_creacion)
        
        try:
            # Ejecutar la consulta SQL
            DatabaseConnection.execute_query(query, params=params)
        except Exception as e:
            # Puedes manejar cualquier excepción de la base de datos aquí
            raise InvalidDataError("Failed to create servidor")
        

    def exists(self):
        # Verificar si el ID de la película existe en la base de datos
        return Servidor.query.filter_by(servidor_id=self.id_servidor).first() is not None    

    @classmethod
    def update(cls, servidor_data):
        """Update a servdor
        Args:
            - servidor (Servidor): Servidor object
        """
        allowed_columns = {'nombre', 'descripcion', 'fecha_creacion'}

        query_parts = []
        params = []
        
        for key, value in servidor_data.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)

        params.append(servidor_data.id_usuario)

        if query_parts:
            query = f"UPDATE Discord2.servidores SET {', '.join(query_parts)} WHERE id_servidor = %s"
            DatabaseConnection.execute_query(query, params=params)
        else:
            # No se proporcionaron datos válidos para actualizar
            raise InvalidDataError("No se proporcionaron datos válidos para actualizar el servidor")

    
    @classmethod
    def delete(cls, servidor_data):
        """Delete a servidor
        Args:
            - servidor(Servidor): Film object with the id attribute
        """
        query = "DELETE FROM discord2.servidores WHERE id_servidor = %s"
        params = servidor_data.id_servidor,
        DatabaseConnection.execute_query(query, params=params)
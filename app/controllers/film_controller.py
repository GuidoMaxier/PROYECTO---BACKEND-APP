from ..models.film_model import Film

from flask import request

from decimal import Decimal


from ..routes.error_handlers import handle_film_not_found

from ..models.exceptions import FilmNotFound, InvalidDataError

class FilmController:
    """Film controller class"""

    @classmethod
    def get(cls, film_id):
        """Get a film by id"""
        film = Film(film_id=film_id)
        result = Film.get(film)

        if result is not None:
            return result.serialize(), 200

        
    @classmethod
    def get_all(cls):
        """Get all films"""
        film_objects = Film.get_all()
        films = []
        for film in film_objects:
            films.append(film.serialize())
        return films, 200
    
    @classmethod
    def create(cls):
        """Create a new film"""
        data = request.json
        # TODO: Validate data
        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100

        film = Film(**data)
        Film.create(film)
        return {'message': 'Film created successfully'}, 201



    # Realizamos la validación de los datos.
    @classmethod
    def validate_input_data(cls, data):
        if len(data.get('title', '')) < 3:
            raise InvalidDataError("Title must have at least three characters")
        
        if not isinstance(data.get('language_id'), int) or not isinstance(data.get('rental_duration'), int) \
                or not isinstance(data.get('rental_rate'), int) or not isinstance(data.get('replacement_cost'), int):
            raise InvalidDataError("Invalid data types for some attributes")
        
        if data.get('special_features') is not None and (not isinstance(data.get('special_features'), list) \
                or not all(isinstance(feature, str) for feature in data.get('special_features')) \
                or not all(feature in ["Trailers", "Commentaries", "Deleted Scenes", "Behind the Scenes"]
                            for feature in data.get('special_features'))):
            raise InvalidDataError("Invalid special features")


    # EJERCICIO N°3 y N°4
    @classmethod
    def update(cls, film_id):
        """Update a film"""
    
        data = request.json
        # TODO: Validate data
       
        # Realizamos las validaciones de datos de entrada
        cls.validate_input_data(data)
        
        
        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
        
        data['film_id'] = film_id

        film = Film(**data)

        # TODO: Validate film exists
        if not Film.exists(film_id):
            raise FilmNotFound(film_id)
        
        Film.update(film)
        return {'message': 'Film updated successfully'}, 200
    
    
    # EJERCICIO N°5
    @classmethod
    def delete(cls, film_id):
        """Delete a film"""
        film = Film(film_id=film_id)

        # TODO: Validate film exists
        if not Film.exists(film_id):
            raise FilmNotFound(film_id)
        
        Film.delete(film)
        return {'message': 'Film deleted successfully'}, 200
from flask import Blueprint
from ..models.exceptions import FilmNotFound, InvalidDataError

errors = Blueprint("errors", __name__)

# Define el manejador  

#EJERCICIO 1 - EJERCICIO 3  EJERCICIO 5
@errors.app_errorhandler(FilmNotFound)
def handle_film_not_found(error):
        return error.get_response()


#EJERCICIO 2 - EJERCICIO 4
@errors.app_errorhandler(InvalidDataError)
def handle_InvalidDataError(error):
        return error.get_response()

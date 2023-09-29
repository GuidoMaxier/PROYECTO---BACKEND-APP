from flask import Blueprint
from ..models.exceptions import NotFound, InvalidDataError

errors = Blueprint("errors", __name__)





@errors.app_errorhandler(NotFound)
def handle_not_found(error):
        return error.get_response()



@errors.app_errorhandler(InvalidDataError)
def handle_InvalidDataError(error):
        return error.get_response()

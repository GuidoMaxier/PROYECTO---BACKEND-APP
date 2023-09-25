from flask import Blueprint

from flask_cors import cross_origin 

from ..controllers.servidor_controller import ServidorController

servidor_bp = Blueprint('servidor_bp', __name__)


servidor_bp.route('/', methods=['GET'])(ServidorController.get_all)

servidor_bp.route('/<int:id_servidor>', methods=['GET'])(ServidorController.get)

servidor_bp.route('/', methods=['POST'])(ServidorController.create)

servidor_bp.route('/<int:id_servidor>', methods=['PUT'])(ServidorController.update)

servidor_bp.route('/<int:id_servidor>', methods=['DELETE'])(ServidorController.delete)


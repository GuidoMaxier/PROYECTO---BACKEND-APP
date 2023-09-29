from flask import Blueprint

from flask_cors import cross_origin 

from ..controllers.canal_controller import CanalController

canal_bp = Blueprint('canal_bp', __name__)


canal_bp.route('/', methods=['GET'])(CanalController.get_all)

canal_bp.route('/<int:id_canal>', methods=['GET'])(CanalController.get)

canal_bp.route('/', methods=['POST'])(CanalController.create)

canal_bp.route('/<int:id_canal>', methods=['PUT'])(CanalController.update)

canal_bp.route('/<int:id_canal>', methods=['DELETE'])(CanalController.delete)

canal_bp.route('/server/<int:id_servidor>', methods=['GET'])(CanalController.get_by_id_server)



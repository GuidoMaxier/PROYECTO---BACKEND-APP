from flask import Blueprint

from ..controllers.user_server_controller import UserServerController

userserver_bp = Blueprint('userserver_bp', __name__)

userserver_bp.route('/', methods=['GET'])(UserServerController.get_all)
userserver_bp.route('/<int:userserver_id>', methods=['GET'])(UserServerController.get)
userserver_bp.route('/', methods=['POST'])(UserServerController.create)
userserver_bp.route('/<int:userserver_id>', methods=['PUT'])(UserServerController.update)
userserver_bp.route('/<int:userserver_id>', methods=['DELETE'])(UserServerController.delete)
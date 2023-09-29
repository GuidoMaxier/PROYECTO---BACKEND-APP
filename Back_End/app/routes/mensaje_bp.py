from flask import Blueprint

from ..controllers.mensaje_controller import MensajeController

mensaje_bp = Blueprint('mensaje_bp', __name__)

mensaje_bp.route('/', methods=['GET'])(MensajeController.get_all)

mensaje_bp.route('/<int:id_mensaje>', methods=['GET'])(MensajeController.get)

mensaje_bp.route('/', methods=['POST'])(MensajeController.create)
mensaje_bp.route('/<int:id_mensaje>', methods=['PUT'])(MensajeController.update)
mensaje_bp.route('/<int:id_mensaje>', methods=['DELETE'])(MensajeController.delete)
mensaje_bp.route('/canal/<int:id_canal>', methods=['GET'])(MensajeController.get_by_id_canal)


# mensaje_bp.route('/api/enviar_mensaje', methods=['POST'])
# mensaje_bp.route('/api/mensajes', methods=['GET'])
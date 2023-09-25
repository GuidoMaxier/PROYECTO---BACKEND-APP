from flask import Flask, request, session, jsonify
from flask_cors import CORS
from config import Config
from flask_socketio import SocketIO #Chat



from .routes.film_bp import film_bp

from .routes.user_bp import user_bp #profile_bp, auth_bp
from .routes.servidor_bp import servidor_bp
from .routes.usuario_servidor_bp import userserver_bp 


from .database import DatabaseConnection
from .routes.error_handlers import errors 



def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)


   # CORS(app, resources={r"/socket.io/*": {"origins": "*"}})
  
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
   

    app.config.from_object(
        Config
    )


    DatabaseConnection.set_config(app.config)

    # app.register_blueprint(film_bp, url_prefix = '/films')

    app.register_blueprint(user_bp)

    app.register_blueprint(errors) #Agregado

    app.register_blueprint(servidor_bp, url_prefix = '/servidor')
    app.register_blueprint(userserver_bp , url_prefix = '/userserver')

    # Registra los Blueprints con las rutas correspondientes
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(profile_bp)


    # Lista para almacenar los mensajes (simula una base de datos)
    # db_mensajes = []

    db_mensajes = [
        {'usuario': 'Usuario1', 'mensaje': '¡Hola!'},
        {'usuario': 'Usuario2', 'mensaje': 'Hola, ¿cómo estás?'},
        {'usuario': 'Usuario1', 'mensaje': 'Estoy bien, gracias.'},
        {'usuario': 'Usuario2', 'mensaje': 'Eso es genial.'},
    ]
    

    @app.route('/api/enviar_mensaje', methods=['POST'])
    def enviar_mensaje():
        data = request.get_json()
        mensaje = data['mensaje']
        usuario = data['usuario']

        print("mensaje chat", mensaje)

        # Agregar el mensaje a la lista (simulado)
        db_mensajes.append({'usuario': usuario, 'mensaje': mensaje})

        return jsonify({"mensaje": "Mensaje enviado con éxito"})

    @app.route('/api/mensajes', methods=['GET'])
    def obtener_mensajes():
        return jsonify(db_mensajes)


    return app
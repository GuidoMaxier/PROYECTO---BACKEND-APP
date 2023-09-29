from flask import Flask, request, session, jsonify
from flask_cors import CORS
from config import Config


from .routes.user_bp import user_bp #profile_bp, auth_bp
from .routes.servidor_bp import servidor_bp
from .routes.canal_bp import canal_bp
from .routes.usuario_servidor_bp import userserver_bp 
from .routes.mensaje_bp import mensaje_bp


from .database import DatabaseConnection
from .routes.error_handlers import errors 



def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)


   # CORS(app, resources={r"/socket.io/*": {"origins": "*"}})
  
    CORS(app, supports_credentials=True)
   

    app.config.from_object(
        Config
    )


    DatabaseConnection.set_config(app.config)


    app.register_blueprint(user_bp)

    app.register_blueprint(errors) #Agregado

    app.register_blueprint(servidor_bp, url_prefix = '/servidor')

    app.register_blueprint(canal_bp, url_prefix = '/canal')

    app.register_blueprint(userserver_bp , url_prefix = '/userserver')

    app.register_blueprint(mensaje_bp , url_prefix = '/mensaje')

    # Registra los Blueprints con las rutas correspondientes
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(profile_bp)



    return app
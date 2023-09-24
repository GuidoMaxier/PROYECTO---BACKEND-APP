from app import init_app
from flask import Flask, render_template, request, jsonify
# from flask_socketio import SocketIO,  emit


if __name__ == "__main__":
    app = init_app()
    # socketio = SocketIO(app, cors_allowed_origins="*")
    app.run()




    # # Datos simulados para demostración (simula una base de datos)
    # db_mensajes = [
    #     {'usuario': 'Usuario1', 'mensaje': '¡Hola!'},
    #     {'usuario': 'Usuario2', 'mensaje': 'Hola, ¿cómo estás?'},
    #     {'usuario': 'Usuario1', 'mensaje': 'Estoy bien, gracias.'},
    #     {'usuario': 'Usuario2', 'mensaje': 'Eso es genial.'},
    # ]
    

 
    # # Datos simulados para demostración
    # mensajes = []

    # @app.route('/api/enviar_mensaje', methods=['POST'])
    # def enviar_mensaje():
    #     data = request.json #request.get_json()
    #     mensaje = data['mensaje']
    #     usuario = data['usuario']

    #     print("mensaje chat", mensaje)
    #     # Agregar el mensaje a la lista (simulado)
    #     db_mensajes.append({'usuario': usuario, 'mensaje': mensaje})

    #     # Emitir el mensaje a todos los clientes conectados a través del WebSocket
    #     emit('mensaje_nuevo', {'usuario': usuario, 'mensaje': mensaje}, broadcast=True)

    #     return jsonify({"mensaje": "Mensaje enviado con éxito"})
    

    # @app.route('/api/mensajes', methods=['GET'])
    # def obtener_mensajes():
    #     return jsonify(db_mensajes)
    

    # # Evento 'connect': se ejecuta cuando un cliente se conecta
    # @socketio.on('connect')
    # def handle_connect():
    #     print('Cliente conectado')

    # # Evento 'disconnect': se ejecuta cuando un cliente se desconecta
    # @socketio.on('disconnect')
    # def handle_disconnect():
    #     print('Cliente desconectado')

    # socketio.run(app, debug=True)



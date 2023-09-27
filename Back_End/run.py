from app import init_app
from flask import Flask, render_template, request, jsonify
# from flask_socketio import SocketIO,  emit


if __name__ == "__main__":
    app = init_app()
    # socketio = SocketIO(app, cors_allowed_origins="*")
    app.run()


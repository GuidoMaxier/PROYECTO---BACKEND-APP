
from ..models.user_model import User

from flask import Flask, request, session, jsonify 

from decimal import Decimal


from ..routes.error_handlers import handle_not_found


from flask_cors import cross_origin 

#from flask_session import Session


class UserController:
    """Usuarios controller class"""

    @classmethod
    def get(cls, id_usuario):
        """Get a usuario by id"""
        user = User(id_usuario=id_usuario)
        result = User.get(user)

        if result is not None:
            return result.serialize(), 200

        
    @classmethod
    def get_all(cls):
        """Get all users"""
        user_objects = User.get_all()
        users = []
        for user in user_objects:
            users.append(user.serialize())
        return users, 200
    

    @classmethod
    def create(cls):
        """Create a new usuario"""
        data = request.json
        

        # TODO: Validate data


        # Verificar si ya existe un usuario con el mismo nombre de usuario
        if User.check_username(data['username']):
            return jsonify({'message': 'El nombre de usuario ya está en uso'}), 400
            

        # Verificar si ya existe un usuario con el mismo correo electrónico
        if User.check_email(data['email']):
            return jsonify({'message': 'El correo electrónico ya está registrado'}), 400
            

        user = User(**data)
        User.create(user)
        return {'message': 'Creacion de Usuario Exitosa'}, 201


    @classmethod
    def update(cls, id_usuario):
        """Update a USER"""
        
        data = request.json

        # TODO: Validate data
        data['id_usuario'] = id_usuario

        UsernameExite = User.check_username(data['username'])
        EmailExiste = User.check_email(data['email'])

        if UsernameExite is not None:
            if UsernameExite[0] != id_usuario:
                return jsonify({'message': 'El nombre de usuario ya está en uso'}), 400

        if EmailExiste is not None:
              if EmailExiste[0] != id_usuario:
                  return jsonify({'message': 'El correo electrónico ya está registrado'}), 400
                  


        user = User(**data)

        # TODO: Validate exists
        User.update(user)
        return {'message': 'USER updated successfully'}, 200
    


    @classmethod
    def delete(cls, id_usuario):
        """Delete a USER"""

        print("ID-usuario: ", id_usuario)
        user = User(id_usuario=id_usuario)

        # TODO: Validate user exists


        User.delete(user)
        return {'message': 'Usuario deleted successfully'}, 204
    

    

    @classmethod
    def login(cls):

        data = request.json
        user = User(
            username=data.get('username'),
            contraseña=data.get('contraseña')
        )


        if User.is_registered(user):
            # session['username'] = data.get('username')
            # return {"message": "Sesion iniciada"}, 200
            result = User.obtener_datos_del_usuario(user)

            if result is not None:
                return result.serialize(), 200

            else:
                return {"message": "Usuario o contraseña incorrectos....."}, 401 

        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
        

    @classmethod
    def show_profile(cls):

        user_nombre = session.get('username')

        if user_nombre is None:
                return {"message": "Usuario no encontrado user_nombre"}, 404
         
        user = User.obtener_datos_del_usuario(User(username = user_nombre))

        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
        
  
    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200
    


    

    #@app.route('/cambiarclave', methods=['POST'])
    @classmethod
    def cambiar_clave(cls):
        try:
            data = request.json
    

            # TODO: Validate exists
            user = User(**data)

            User.update_clave(user)
            
            return jsonify({"message": "Contraseña cambiada exitosamente"}), 200

        except Exception as e:
            return jsonify({"error": "Error al cambiar la contraseña"}), 500
        
 




    

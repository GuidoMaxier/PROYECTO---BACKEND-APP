from ..models.servidor_model import Servidor
from ..models.user_server_model import UserServer

from flask import request, jsonify



class ServidorController:
    """Servidor controller class"""

    @classmethod
    def get(cls, id_servidor):
        """Get a servidor by id"""
        servidor = Servidor(id_servidor=id_servidor)
        result = Servidor.get(servidor)

        if result is not None:
            return result.serialize(), 200


    @classmethod
    def get_all(cls):
        """Get all servidores"""
        servidor_objects = Servidor.get_all()
        servidores = []
        for servidor in servidor_objects:
            servidores.append(servidor.serialize())
        return servidores, 200
    

    # @classmethod
    # def create(cls):
    #     """Create a new servidor"""
    #     data = request.json
    #     # TODO: Validate data

    #     # Verificar si ya existe un servidor con el mismo nombre
    #     if Servidor.check_username(data['nombre']):
    #         return jsonify({'message': 'El nombre del servidor ya está en uso'}), 400
        
    #     # Escribimos en la tabla intermedia

        
    #     servidor = Servidor(**data)
    #     Servidor.create(servidor)
    #     return {'message': 'Servidor created successfully'}, 201
    
    @classmethod
    def create(cls):
        """Create a new servidor"""
        data = request.json

        # Validar los datos aquí (por ejemplo, asegurarse de que los campos requeridos estén presentes)
        print(data['nombre'])

        # Verificar si ya existe un servidor con el mismo nombre
        if Servidor.check_nombre(data['nombre']):
            return jsonify({'message': 'El nombre del servidor ya está en uso'}), 400
        

        nombre = data['nombre']
        descripcion = data['descripcion']
        fecha_creacion = data['fecha_creacion']

        servidor = Servidor(nombre=nombre, descripcion=descripcion, fecha_creacion=fecha_creacion)
        Servidor.create(servidor)
       

        # Obtener el ID del servidor recién creado
        servidor_id = Servidor.check_nombre(data['nombre'])

        print(servidor_id[0])

        # Registrar la relación en la tabla intermedia "Usuario_Servidor"
        usuario_id = data['id_usuario']
        rol = data['rol']
        usuario_servidor = UserServer(usuario_id=usuario_id, servidor_id=servidor_id[0], rol=rol)
        UserServer.create(usuario_servidor)

        return {'message': 'Servidor creado con éxito'}, 201


    @classmethod
    def update(cls, id_servidor):
        """Update a servidor"""
        data = request.json
        # TODO: Validate data
        # if data.get('rental_rate') is not None:
        #     if isinstance(data.get('rental_rate'), int):
        #         data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        # if data.get('replacement_cost') is not None:
        #     if isinstance(data.get('replacement_cost'), int):
        #         data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
        
        data['id_servdor'] = id_servidor

        servidor = Servidor(**data)

        # TODO: Validate film exists
        Servidor.update(servidor)
        return {'message': 'Servidor updated successfully'}, 200
    
    @classmethod
    def delete(cls, id_servidor):
        """Delete a servidor"""
        servidor = Servidor(id_servidor=id_servidor)

        # TODO: Validate film exists
        Servidor.delete(servidor)
        return {'message': 'Servidor deleted successfully'}, 204
    

            
    @classmethod
    def get_filter(cls, id_usuario):
        """Get filter servidores"""
        servidor_objects = Servidor.get_filter(id_usuario=id_usuario)
        servidores = []
        for servidor in servidor_objects:
            servidores.append(servidor.serialize())
        return servidores, 200
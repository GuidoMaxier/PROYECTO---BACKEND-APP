from ..models.mensaje_model import Mensaje

from flask import request, jsonify


from ..routes.error_handlers import handle_not_found



class MensajeController:
    """Mensaje controller class"""

    @classmethod
    def get(cls, id_mensaje):
        """Get a mensaje by id"""
        mensaje = Mensaje(id_mensaje=id_mensaje)
        result = Mensaje.get(mensaje)

        if result is not None:
            return result.serialize(), 200

        
    @classmethod
    def get_all(cls):
        """Get all mensajes"""
        mensaje_objects = Mensaje.get_all()
        mensajes = []
        for mensaje in mensaje_objects:
            mensajes.append(mensaje.serialize())
        return mensajes, 200
    
    
    @classmethod
    def create(cls):
        """Create a new mensaje"""
        data = request.json
        # TODO: Validate data
        # if data.get('rental_rate') is not None:
        #     if isinstance(data.get('rental_rate'), int):
        #         data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        

        mensaje = Mensaje(**data)
        Mensaje.create(mensaje)
        return {'message': 'Mensaje created successfully'}, 201


    @classmethod
    def update(cls, id_mensaje):
        """Update a mensaje"""
        data = request.json
        # TODO: Validate data
        
        # if data.get('replacement_cost') is not None:
        #     if isinstance(data.get('replacement_cost'), int):
        #         data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
        
        data['id_mensaje'] = id_mensaje

        mensaje = Mensaje(**data)

        # TODO: Validate  exists
        Mensaje.update(mensaje)
        return {'message': 'Mensaje updated successfully'}, 200
    
    @classmethod
    def delete(cls, id_mensaje):
        """Delete a mensaje"""
        mensaje = Mensaje(id_mensaje=id_mensaje)

        # TODO: Validate  exists
        Mensaje.delete(mensaje)
        return {'message': 'Mensaje deleted successfully'}, 204
    

    @classmethod
    def get_by_id_canal(cls, id_canal):
        """Get filter mensajes"""
        mensaje_objects = Mensaje.get_by_id_canal(id_canal=id_canal)
        mensajes = []
        for mensaje in mensaje_objects:
            mensajes.append(mensaje.serialize())
        return mensajes, 200
    

   
    

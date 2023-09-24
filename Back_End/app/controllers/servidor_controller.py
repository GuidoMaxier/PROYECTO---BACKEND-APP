from ..models.servidor_model import Servidor

from flask import request



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
    

    @classmethod
    def create(cls):
        """Create a new servidor"""
        data = request.json
        # TODO: Validate data
        # if data.get('rental_rate') is not None:
        #     if isinstance(data.get('rental_rate'), int):
        #         data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        # if data.get('replacement_cost') is not None:
        #     if isinstance(data.get('replacement_cost'), int):
        #         data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100

        servidor = Servidor(**data)
        Servidor.create(servidor)
        return {'message': 'Servidor created successfully'}, 201


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
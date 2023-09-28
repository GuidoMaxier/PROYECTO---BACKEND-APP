from ..models.canal_model import Canal

from flask import request




class CanalController:
    """Canal controller class"""

    @classmethod
    def get(cls, id_canal):
        """Get a canal by id"""
        canal = Canal(id_canal=id_canal)
        result = Canal.get(canal)

        if result is not None:
            return result.serialize(), 200



        
    @classmethod
    def get_all(cls):
        """Get all canales"""
        canal_objects = Canal.get_all()
        canales = []
        for canal in canal_objects:
            canales.append(canal.serialize())
        return canales, 200
    
    @classmethod
    def create(cls):
        """Create a new canale"""
        data = request.json
        # TODO: Validate data
        # if data.get('rental_rate') is not None:
        #     if isinstance(data.get('rental_rate'), int):
        #         data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        # if data.get('replacement_cost') is not None:
        #     if isinstance(data.get('replacement_cost'), int):
        #         data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100

        canal = Canal(**data)
        Canal.create(canal)
        return {'message': 'Canal created successfully'}, 201


    @classmethod
    def update(cls, id_canal):
        """Update a canal"""
        data = request.json
        # TODO: Validate data
        # if data.get('rental_rate') is not None:
        #     if isinstance(data.get('rental_rate'), int):
        #         data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        # if data.get('replacement_cost') is not None:
        #     if isinstance(data.get('replacement_cost'), int):
        #         data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
        
        data['id_canal'] = id_canal

        canal = Canal(**data)

        # TODO: Validate film exists
        Canal.update(canal)
        return {'message': 'Canal updated successfully'}, 200
    
    @classmethod
    def delete(cls, id_canal):
        """Delete a canal"""
        canal = Canal(id_canal=id_canal)

        # TODO: Validate canal exists
        Canal.delete(canal)
        return {'message': 'Canal deleted successfully'}, 204
    
    @classmethod
    def get_by_id_server(cls, id_servidor):
        """Get filter canales"""
        canal_objects = Canal.get_by_id_server(id_servidor=id_servidor)
        canales = []
        for canal in canal_objects:
            canales.append(canal.serialize())
        return canales, 200
    
    @classmethod
    def get_by_name_server(cls, nombre):
        """Get filter canales"""
        canal_objects = Canal.get_by_name_server(nombre=nombre)
        canales = []
        for canal in canal_objects:
            canales.append(canal.serialize())
        return canales, 200
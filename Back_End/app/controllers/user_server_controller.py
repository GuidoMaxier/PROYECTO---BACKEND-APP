from ..models.user_server_model import UserServer

from flask import request

from decimal import Decimal


from ..routes.error_handlers import handle_film_not_found



class UserServerController:
    """UserServer controller class"""

    @classmethod
    def get(cls, id):
        """Get a userserver by id"""
        userserver = UserServer(id=id)
        result = UserServer.get(userserver)

        if result is not None:
            return result.serialize(), 200



        
    @classmethod
    def get_all(cls):
        """Get all userserver"""
        userserver_objects = UserServer.get_all()
        userservers = []
        for userserver in userserver_objects:
            userservers.append(userserver.serialize())
        return userservers, 200
    
    @classmethod
    def create(cls):
        """Create a new userserver"""
        data = request.json
        # TODO: Validate data
        # if data.get('rental_rate') is not None:
        #     if isinstance(data.get('rental_rate'), int):
        #         data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        # if data.get('replacement_cost') is not None:
        #     if isinstance(data.get('replacement_cost'), int):
        #         data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100

        userserver = UserServer(**data)
        UserServer.create(userserver)
        return {'message': 'UserServer created successfully'}, 201


    @classmethod
    def update(cls, id):
        """Update a userservidor"""
        data = request.json
        # TODO: Validate data
        # if data.get('rental_rate') is not None:
        #     if isinstance(data.get('rental_rate'), int):
        #         data['rental_rate'] = Decimal(data.get('rental_rate'))/100
        
        # if data.get('replacement_cost') is not None:
        #     if isinstance(data.get('replacement_cost'), int):
        #         data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
        
        data['id'] = id

        userserver = UserServer(**data)

        # TODO: Validate film exists
        UserServer.update(userserver)
        return {'message': 'User_Server updated successfully'}, 200
    
    @classmethod
    def delete(cls, id):
        """Delete a userserver"""
        userserver = UserServer(id=id)

        # TODO: Validate film exists
        UserServer.delete(userserver)
        return {'message': 'User_Server deleted successfully'}, 204
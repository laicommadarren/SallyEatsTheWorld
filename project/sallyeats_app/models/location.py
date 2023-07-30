from sallyeats_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request

class Location:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.urlname = data['urlname']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_locations(cls):
        query = "SELECT * FROM locations;"
        results = connectToMySQL('sallyeatstheworld_schema').query_db(query)
        locations = []
        for location in results:
            locations.append( cls(location) )
        return locations
    
    @classmethod
    def get_one_location(cls, data):
        query = "SELECT * from locations where name=%(location_name)s"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_from_urlname(cls,data):
        query = "SELECT * from locations where urlname=%(location_url)s;"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        if not result:
            return False
        return cls(result[0])
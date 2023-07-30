from sallyeats_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request

class Restaurant:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.urlname = data['urlname']
        self.yelp_link = data['yelp_link']
        self.image_link = data['image_link']
        self.location_id = data['location_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_restaurants_from_location(cls, data):
        query = "SELECT * FROM restaurants where location_id=%(id)s;"
        results = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        restaurants = []
        for restaurant in results:
            restaurants.append( cls(restaurant) )
        return restaurants
    
    @classmethod
    def get_one_restaurant(cls, data):
        query = "SELECT * from restaurants where name=%(restaurant_name)s;"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_from_urlname(cls, data):
        query = "SELECT * from restaurants where urlname=%(restaurant_url)s;"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        if not result:
            return False
        return cls(result[0])
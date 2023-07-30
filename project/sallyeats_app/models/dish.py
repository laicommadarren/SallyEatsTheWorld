from sallyeats_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Dish:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.urlname = data['urlname']
        self.description = data['description']
        self.image_link = data['image_link']
        self.restaurant_id = data['restaurant_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.topfive = []

    @classmethod
    def get_dishes_from_restaurant(cls, data):
        query = "SELECT * FROM dishes where restaurant_id=%(id)s;"
        results = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        dishes = []
        for dish in results:
            dishes.append( cls(dish) )
        return dishes
    
    @classmethod
    def get_one_dish(cls, data):
        query = "SELECT * FROM dishes WHERE id = %(id)s"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_from_urlname(cls, data):
        query = "SELECT * from dishes where urlname=%(dish_url)s;"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        if not result:
            return False
        return cls(result[0])
    
    @classmethod
    def rate_dish(cls, data):
        query = "INSERT INTO users_tried_dishes (user_id, dish_id, dish_rating) VALUES (%(user_id)s, %(dish_id)s, %(dish_rating)s);"
        return connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
    
    @classmethod
    def update_rating(cls, data):
        query = "UPDATE users_tried_dishes SET dish_rating = %(dish_rating)s WHERE (user_id = %(user_id)s AND dish_id = %(dish_id)s);"
        return connectToMySQL('sallyeatstheworld_schema').query_db(query, data)

    @classmethod
    def check_dish_rated_by_user(cls, data):
        query = "SELECT * from users_tried_dishes WHERE (user_id = %(user_id)s AND dish_id = %(dish_id)s);"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        print(result)
        if not result:
            return False
        #return cls(result[0])
        return result[0]
    
    @classmethod
    def get_topfive(cls, data):
        query = "SELECT * from users_tried_dishes LEFT JOIN dishes ON dishes.id = users_tried_dishes.dish_id WHERE user_id = %(user_id)s ORDER BY dish_rating DESC LIMIT 5;"
        results = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        if not results:
            return False
        list = cls(results[0])
        for row in results:
            dish_data = {
                'id' : row['id'],
                'name' : row['name'],
                'urlname' : row['urlname'],
                'description' : row['description'],
                'image_link' : row['image_link'],
                'restaurant_id' : row['restaurant_id'],
                'created_at' : row['dishes.created_at'],
                'updated_at' : row['dishes.updated_at'] 
            }
            list.topfive.append(Dish(dish_data))
        return list

    @classmethod
    def get_average_rating(cls, data):
        query = "SELECT ROUND(SUM(dish_rating)/COUNT(dish_rating),1) AS average_rating from users_tried_dishes WHERE dish_id = %(id)s;"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        print(result)
        if not result:
            return False
        return result[0]
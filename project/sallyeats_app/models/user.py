from sallyeats_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.notifications = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (username, email, password) VALUES (%(username)s, %(email)s, %(password)s)"
        return connectToMySQL('sallyeatstheworld_schema').query_db(query,data)
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_username(cls,data):
        query = "SELECT * FROM users WHERE username = %(username)s;"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def check_friendship(cls,data):
        query = "SELECT * FROM friends WHERE (user_id = %(user_id)s AND friend_id = %(friend_id)s) OR (user_id = %(friend_id)s AND friend_id = %(user_id)s);"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query,data)
        if not result:
            return False
        return result[0]
    
    @classmethod
    def request_friend(cls,data):
        query = "INSERT INTO friends (user_id, friend_id) VALUES (%(user_id)s, %(friend_id)s);"
        result = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
    
    @classmethod
    def get_notifications(cls, data):
        query = "SELECT * FROM friends LEFT JOIN users ON user_id = users.id WHERE friend_id = %(id)s AND is_friend = 0;"
        results = connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
        if not results:
            return False
        notif = cls(results[0])
        for row in results:
            user_data = {
                'id' : row['id'],
                'username' : row['username'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            notif.notifications.append(User(user_data))
            return notif

    @classmethod
    def accept_request(cls,data):
        query = "UPDATE friends SET is_friend = 1 WHERE user_id = %(user_id)s AND friend_id = %(friend_id)s;"
        return connectToMySQL('sallyeatstheworld_schema').query_db(query, data)
    
    @classmethod
    def decline_request(cls,data):
        query = "DELETE FROM friends WHERE user_id = %(user_id)s AND friend_id = %(friend_id)s;"
        return connectToMySQL('sallyeatstheworld_schema').query_db(query, data)

    @staticmethod
    def validate_registration(user):
        is_valid = True # we assume this is true
        if len(user['username']) < 6:
            flash("Username must be at least 6 characters", 'category_reg')
        if len(user['username']) > 16:
            flash("Username cannot exceed 16 characters", 'category_reg')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Email format is not valid.", 'category_reg')
            print('Email format invalid')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", 'category_reg')
            is_valid = False
        if not user['confirm_password'] == user['password']:
            flash("Passwords do not match.", 'category_reg')
            print('Passwords do not match')
            is_valid = False
        return is_valid
    
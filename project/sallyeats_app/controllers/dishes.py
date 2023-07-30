from flask import render_template, session, request, redirect, flash
from sallyeats_app import app
from sallyeats_app.models.dish import Dish
from sallyeats_app.models.restaurant import Restaurant
from sallyeats_app.models.location import Location

@app.route('/<location_url>/<restaurant_url>/<dish_url>')
def dish(location_url, restaurant_url, dish_url):
    restaurant_data = {
        'restaurant_name' : session['restaurant_name']
    }
    dish_data = {
        'id' : session['dish_id']
    }
    rating_data = {
        'user_id' : session['user_id'],
        'dish_id' : session['dish_id']
    }
    restaurant_dishes_data = {
        'id' : session['restaurant_id']
    }
    location_data = {
        'location_name' : session['location_name']
    }
    restaurantname_data = {
        'restaurant_name' : session['restaurant_name']
    }
    location=Location.get_one_location(location_data)
    dish = Dish.get_one_dish(dish_data)
    restaurant = Restaurant.get_one_restaurant(restaurantname_data)
    locationurl_data = {
        'location_url' : location_url
    }
    dishurl_data = {
        'dish_url' : dish_url
    }
    restauranturl_data = {
        'restaurant_url' : restaurant_url
    }
    current_location = Location.get_from_urlname(locationurl_data)
    current_dish = Dish.get_from_urlname(dishurl_data)
    current_restaurant = Restaurant.get_from_urlname(restauranturl_data)
    # if any of the url components don't match, or any of the restaurant-location/dish-restaurant correspondence don't match, redirect to dashboard. future work to add flash messages explaining why (optional)
    if not current_location or not current_restaurant or not current_dish or not current_dish.restaurant_id == current_restaurant.id: 
        flash("You have navigated to an improper URL. Please navigate using the given page links.")
        return redirect('/dashboard')
    # overwrite session to match the entered url components
    if not location.urlname == location_url or not restaurant.urlname == restaurant_url or not current_restaurant.location_id == current_location.id or not dish.urlname == dish_url:
        if not location.urlname == location_url:
            session['location_id'] = current_location.id
            session['location_name'] = current_location.name
        if not restaurant.urlname == restaurant_url: 
            session['restaurant_id'] = current_restaurant.id
            session['restaurant_name'] = current_restaurant.name
        if not dish.urlname == dish_url:
            session['dish_id'] = current_dish.id
            session['dish_name'] = current_dish.name
        #reload the page after session is updated
        return redirect('/'+location_url+'/'+restaurant_url+'/'+dish_url)
    return render_template('dish.html', dish=Dish.get_one_dish(dish_data), restaurant=Restaurant.get_one_restaurant(restaurant_data), location_url=location_url, restaurant_url=restaurant_url, user_rated_dish=Dish.check_dish_rated_by_user(rating_data), average_rating=Dish.get_average_rating(dish_data)['average_rating'], dishes = Dish.get_dishes_from_restaurant(restaurant_dishes_data))

@app.route('/<location_url>/<restaurant_url>/<dish_url>', methods=['POST'])
def routetodish(location_url, restaurant_url, dish_url):
    session['dish_id'] = request.form['dish_id']
    session['dish_name'] = request.form['dish_name']
    return redirect("/"+location_url+"/"+restaurant_url+"/"+dish_url)

@app.route('/<location_url>/<restaurant_url>/<dish_url>/rate', methods=['POST'])
def ratedish(location_url, restaurant_url, dish_url):
    data = {
        'user_id' : session['user_id'],
        'dish_id' : session['dish_id'],
        'dish_rating' : request.form['dish_rating']
    }
    Dish.rate_dish(data)
    return redirect("/"+location_url+"/"+restaurant_url+"/"+dish_url)

@app.route('/<location_url>/<restaurant_url>/<dish_url>/updaterating', methods=['POST'])
def ratedishupdate(location_url, restaurant_url, dish_url):
    data = {
        'user_id' : session['user_id'],
        'dish_id' : session['dish_id'],
        'dish_rating' : request.form['dish_rating']
    }
    Dish.update_rating(data)
    return redirect("/"+location_url+"/"+restaurant_url+"/"+dish_url)
from flask import render_template, redirect, request, session
from sallyeats_app import app
from sallyeats_app.models.restaurant import Restaurant
from sallyeats_app.models.dish import Dish
from sallyeats_app.models.location import Location

@app.route('/<location_url>/<restaurant_url>')
def restaurant(location_url, restaurant_url):
    data = {
        'restaurant_name' : session['restaurant_name']
    }
    location_data = {
        'location_name' : session['location_name']
    }
    restaurant_data = {
        'id' : session['restaurant_id']
    }
    restaurantname_data = {
        'restaurant_name' : session['restaurant_name']
    }
    location=Location.get_one_location(location_data)
    restaurant = Restaurant.get_one_restaurant(restaurantname_data)
    locationurl_data = {
            'location_url' : location_url
        }
    restauranturl_data = {
            'restaurant_url' : restaurant_url
        }
    current_location = Location.get_from_urlname(locationurl_data)
    current_restaurant = Restaurant.get_from_urlname(restauranturl_data)
    if not current_location or not current_restaurant or not current_restaurant.location_id == current_location.id: 
        flash("You have navigated to an improper URL. Please navigate using the given page links.")
        return redirect('/dashboard')
    if not location.urlname == location_url or not restaurant.urlname == restaurant_url:
        if not location.urlname == location_url:
            session['location_id'] = current_location.id
            session['location_name'] = current_location.name
        if not restaurant.urlname == restaurant_url: 
            session['restaurant_id'] = current_restaurant.id
            session['restaurant_name'] = current_restaurant.name
        return redirect('/'+location_url+'/'+restaurant_url)
    return render_template('restaurant.html', dishes = Dish.get_dishes_from_restaurant(restaurant_data), restaurant=Restaurant.get_one_restaurant(data), location_url=location_url)

@app.route('/<location_url>/<restaurant_url>', methods=['POST'])
def routetorestaurant(location_url, restaurant_url):
    session['restaurant_id'] = request.form['restaurant_id']
    session['restaurant_name'] = request.form['restaurant_name']
    return redirect("/"+location_url+"/"+restaurant_url)
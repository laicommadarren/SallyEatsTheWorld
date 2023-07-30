from flask import render_template, redirect, request, session
from sallyeats_app import app
from sallyeats_app.models.location import Location
from sallyeats_app.models.restaurant import Restaurant

@app.route('/<location_url>')
def location(location_url):
    data = {
        'location_name' : session['location_name']
    }
    location_data = {
        'id' : session['location_id']
    }
    return render_template('location.html', location=Location.get_one_location(data), restaurants=Restaurant.get_all_restaurants_from_location(location_data), location_url=location_url)

@app.route('/<location_url>/', methods=['POST'])
def routetolocation(location_url):
    session['location_id'] = request.form['location_id']
    session['location_name'] = request.form['location_name']
    print(location_url)
    print(session['location_name'])
    return redirect("/"+location_url)
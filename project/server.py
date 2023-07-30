from sallyeats_app import app
from sallyeats_app.controllers import dishes, locations, restaurants, users
from sallyeats_app.models import dish, location, restaurant, user

if __name__=="__main__":
    app.run(debug=True)
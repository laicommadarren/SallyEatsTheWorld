from flask import render_template, redirect, request, session, flash
from sallyeats_app import app
from sallyeats_app.models.user import User
from sallyeats_app.models.location import Location
from sallyeats_app.models.dish import Dish 
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login_page():
    return render_template('login.html')

@app.route('/register', methods=["POST"])
def register():
    # validate the form here ...
    if not User.validate_registration(request.form):
        return redirect('/login')
    data = {
        "email": request.form['email'],
        "username": request.form['username']
    }
    email_in_db = User.get_by_email(data)
    # check if email exists in database already
    if email_in_db:
        flash("An account with this email already exists.", 'category_reg')
        return redirect ('/login')
    #check if username already exists in database
    username_in_db = User.get_by_username(data)
    if username_in_db:
        flash("An account with this username already exists. Please select another username.", 'category_reg')
        return redirect ('/login')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "username": request.form['username'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User to save to database
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    session['user_username'] = data["username"]
    return redirect('/dashboard')

@app.route('/signin', methods=['POST'])
def signin():
    # see if the username provided exists in the database
    data = { "username" : request.form["username"] }
    user_in_db = User.get_by_username(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid username/password combination", 'category_signin')
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid username/password combination", 'category_signin')
        return redirect('/login')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['user_username'] = user_in_db.username
    # never render on a post!!!
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if not session:
        flash("You can only access the dashboard after registration or login.", 'category_db')
        return redirect('/login')
    data = {
        'id' : session['user_id']
    }
    return render_template("dashboard.html", username=session['user_username'], locations=Location.get_all_locations(), notifs = User.get_notifications(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/user/<username>')
def user_profile(username):
    data = {
        'username' : username
    }
    user = User.get_by_username(data)
    friendship_data = {
        'user_id' : session['user_id'],
        'friend_id' : user.id
    }
    topfive_data = {
        'user_id' : user.id
    }
    if user:
        return render_template('userprofile.html', user=user, friendship = User.check_friendship(friendship_data), top_five_dishes=Dish.get_topfive(topfive_data))
    
@app.route('/user/<username>/requestfriend')
def friend_request(username):
    data = {
        'username' : username
    }
    user = User.get_by_username(data)
    friendship_data = {
        'user_id' : session['user_id'],
        'friend_id' :  user.id
    }
    User.request_friend(friendship_data)
    return redirect('/user/'+username)

@app.route('/acceptfriend', methods=["POST"])
def acceptrequest():
    data = {
        'user_id' : request.form['user_id'],
        'friend_id' : session['user_id']
    }
    User.accept_request(data)
    return redirect('/dashboard')

@app.route('/declinefriend', methods=["POST"])
def declinerequest():
    data = {
        'user_id' : request.form['user_id'],
        'friend_id' : session['user_id']
    }
    User.decline_request(data)
    return redirect('/dashboard')
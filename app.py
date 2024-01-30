import os
import pymongo
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home_page")
def home_page():
    recommendations = list(mongo.db.recommendations.find())

    # Add city_name to each recommendation
    for recommendation in recommendations:
        city_id = recommendation.get("city_id")
        default_location = mongo.db.locations.find_one({"_id": ObjectId(city_id)})
        city_name = default_location.get("name", "")
        recommendation["city_name"] = city_name

    # Group recommendations by category
    grouped_recommendations = {}
    for recommendation in recommendations:
        category = recommendation.get('category')
        if category not in grouped_recommendations:
            grouped_recommendations[category] = []
        grouped_recommendations[category].append(recommendation)


    return render_template("home_page.html", recommendations=recommendations, grouped_recommendations=grouped_recommendations)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))
        else:
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!", "success")
            return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route('/city/<city_name>')
def city_page(city_name):
    # Query MongoDB based on the city_name parameter
    city_data = mongo.db.locations.find_one({'name': city_name})

    if city_data:
        # Query the recommendations collection for recommendations associated with the city_id
        recommendations = list(mongo.db.recommendations.find({"city_id": city_data['_id']}))

        # Group recommendations by category
        grouped_recommendations = {}
        for recommendation in recommendations:
            category = recommendation.get('category')
            if category not in grouped_recommendations:
                grouped_recommendations[category] = []
            grouped_recommendations[category].append(recommendation)

        # Render the template with city data and grouped recommendations
        return render_template('view_recommendations.html', city_data=city_data, grouped_recommendations=grouped_recommendations)
    else:
       # Raise a 404 error if the provided city name is not found
            abort(404)


@app.route("/add_recommendations", methods=["GET", "POST"])
def add_recommendations():
    if request.method == "POST":
        # Retrieve the recommendation data from the form
        category = request.form.get("category")
        user = request.form.get("user")
        comment = request.form.get("comment")
        city_name = request.form.get("city")

        # Find the city based on the provided city name
        city_data = mongo.db.locations.find_one({'name': city_name})

        # Ensure that the city is found in the locations collection
        if city_data:
            # City id is now defined with what is retrieved from Mongodb
            city_id = city_data['_id']

            locations = mongo.db.locations.find({}, {"name": 1, "_id": 0})
            city_names = [location["name"] for location in locations]
            categories = mongo.db.recommendations.distinct("category")

            # Insert the recommendation into the recommendations collection
            recommendation = {
                "city_id": city_id,
                "category": category,
                "user": user,
                "comment": comment
            }

            mongo.db.recommendations.insert_one(recommendation)

            flash("Recommendation successfully added!", "success")

            return render_template("add_recommendations.html", cities=city_names, categories=categories, city_id=city_id)
        else:
            # Raise a 404 error if the provided city name is not found
            abort(404)

    else:
        # Handle the GET request, provide initial data for the form
        locations = mongo.db.locations.find({}, {"name": 1, "_id": 0})
        city_names = [location["name"] for location in locations]
        categories = mongo.db.recommendations.distinct("category")

        return render_template("add_recommendations.html", cities=city_names, categories=categories)


@app.route('/edit_recommendation/<id>', methods=["GET", "POST"])
def edit_recommendation(id):

    recommendation = mongo.db.recommendations.find_one({"_id": ObjectId(id)})
    # Fetch the city_id from the recommendation
    city_id = recommendation.get("city_id")

    # Query the locations collection to retrieve the corresponding city_name
    default_location = mongo.db.locations.find_one({"_id": ObjectId(city_id)})
    locations = mongo.db.locations.distinct("name")

    # Get the city_name from the location document
    city_name_default = default_location.get("name", "")
    
    # Get the city_name from the location document
    city_name_default = default_location.get("name", "")

    if request.method == "POST":
        print("POST request detected")
        # Retrieve the recommendation data from the form
        comment = request.form.get("comment")

        update_query = {
        "$set": {
            "comment": comment
        }
    }
        mongo.db.recommendations.update_one({"_id": ObjectId(id)}, update_query)
        flash("Task Successfully Updated")

    return render_template('edit_recommendation.html', recommendation=recommendation, city_name_default=city_name_default)


@app.route("/delete_recommendation/<id>")
def delete_recommendation(id):
    recommendation = mongo.db.recommendations.find_one({"_id": ObjectId(id)})

    return render_template("delete_confirmation.html", recommendation=recommendation)


@app.route("/delete_confirmation/<id>")
def delete_confirmation(id):
    recommendation = mongo.db.recommendations.find_one({"_id": ObjectId(id)})
    username = recommendation.get("user")
    
    mongo.db.recommendations.delete_one({"_id": ObjectId(id)})
    
    flash("Task Successfully Deleted")
    return redirect(url_for("profile", username=username))

@app.route("/delete_cancel/<id>")
def delete_cancel(id):
    recommendation = mongo.db.recommendations.find_one({"_id": ObjectId(id)})
    username = recommendation.get("user")
    
    return redirect(url_for("profile", username=username))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
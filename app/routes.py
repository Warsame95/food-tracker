from flask import render_template
from forms import FoodTrackerForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/add')
def add():
    foodtracker_form = FoodTrackerForm

    if foodtracker_form.validate_on_submit():
        food_name = foodtracker_form.food_name.data
        quantity = foodtracker_form.quantity.data
        carbs = foodtracker_form.carbs.data
        protein = foodtracker_form.protein.data
        fats = foodtracker_form.fats.data
        date = foodtracker_form.date.data


    return render_template("add.html", template_form = foodtracker_form)
from flask import render_template
from app import app
from .forms import FoodTrackerForm

app.config["SECRET_KEY"] = "mysecret"

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add():
    foodtracker_form = FoodTrackerForm(csrf_enabled=False)

    if foodtracker_form.validate_on_submit():
        food_name = foodtracker_form.food_name.data
        quantity = foodtracker_form.quantity.data
        calories = foodtracker_form.calories.data
        carbs = foodtracker_form.carbs.data
        protein = foodtracker_form.protein.data
        fats = foodtracker_form.fats.data
        date = foodtracker_form.date.data


    return render_template("add.html", template_form = foodtracker_form)
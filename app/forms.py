from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, DateField

class FoodTrackerForm(FlaskForm):
    food_name = StringField('Food Name')
    quantity = IntegerField('Quantity')
    carbs = DecimalField('Carbohydrates (g)')
    protein = DecimalField('Protein (g)')
    fats = DecimalField('Fats (g)')
    date = DateField('Date')
    submit = SubmitField('Add Food Entry')
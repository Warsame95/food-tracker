from __init__ import db


log_food = db.Table('log_food',
                    db.Column('log_id', db.Integer, db.ForeignKey('log.id')),
                    db.Column('food_id', db.Integer, db.ForeignKey('food.id'))
                )

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    foods = db.relationship('Food', secondary= log_food, lazy='dynamic')

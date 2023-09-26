from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String)
    restaurant_pizza = db.relationship(
        "RestaurantPizza",  backref="restaurants"
    )

 

    def __str__(self):
        return self.name

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column('pizza_id',db.Integer, db.ForeignKey("pizzas.id"))
    restaurant_id = db.Column('restaurant_id',db.Integer, db.ForeignKey("restaurants.id"))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    



    def response_serializer(self):
        return {
                "id":self.id,
                "pizza_id":self.pizza_id,
                "restaurant_id":self.restaurant_id,
                "created_at":str(self.created_at),
                "updated_at":str(self.updated_at),
            }                     
    
    def __str__(self):
        return self.pizza_id
 
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    restaurant_pizza = db.relationship(
        "RestaurantPizza", backref="pizzas"
    )
    def response_serializer(self):
        return {
                "id":self.id,
                "ingredients":self.ingredients,
            }  
    
    def __str__(self):
        return self.name
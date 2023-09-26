from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String)
    pizzas = db.relationship(
         "Pizza", secondary="restaurant_pizzas",  back_populates="restaurants"
    )

    @validates("name")
    def validate_name(self, key, name):
        if not len(name.strip().split(" ")) < 50:
            raise ValueError("Must have a name less than 50 words in length")
        restaurant = Restaurant.query.filter_by(name=name).first()
        if restaurant:
            raise ValueError("Name value must be unique")
        return name

 

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
    
    @validates("price")
    def validate_price(self, key, price):
        if isinstance(price, int) and (price >= 1 and price <= 30):
            return price
        else:
            raise ValueError("Must have a price between 1 and 30")


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
    restaurants = db.relationship(
         "Restaurant", secondary="restaurant_pizzas",  back_populates="pizzas"
    )
    def response_serializer(self):
        return {
                "id":self.id,
                "ingredients":self.ingredients,
            }  
    
    def __str__(self):
        return self.name
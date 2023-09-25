from api import db, api
from flask_restful import Resource, reqparse
from .models import Restaurant, Pizza, RestaurantPizza
from .serializer import response_serializer
from datetime import datetime 

parser = reqparse.RequestParser()
parser.add_argument('pizza_id')
parser.add_argument('restaurant_id')
parser.add_argument('price')
parser.add_argument('created_at')
parser.add_argument('updated_at')

class RestaurantList(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        response = response_serializer(restaurants) # to convert the data to JSON format
        return response, 200 
    
class PizzaList(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        response = response_serializer(pizzas) 
        return response, 200
    
class RestaurantPizzaPost(Resource):
    def get(self):
        restaurantpizzas = RestaurantPizza.query.all()
        response = response_serializer(restaurantpizzas)
        return response, 200

    def post(self): 
        data = parser.parse_args()
        created_date = datetime.strptime(data["created_at"], "%d/%m/%y")
        updated_date = datetime.strptime(data["updated_at"], "%d/%m/%y")
        data["created_at"] = created_date
        data["updated_at"] = updated_date
        new_data = RestaurantPizza(**data)
        db.session.add(new_data)
        db.session.commit()
        data["created_at"] = str(created_date)
        data["updated_at"] = str(updated_date)

        return data, 201


        # new_data = RestaurantPizzaPost(**data)

    
api.add_resource(RestaurantList, "/restaurants") 
api.add_resource(PizzaList, "/pizzas")
api.add_resource(RestaurantPizzaPost, "/restaurant_pizzas")

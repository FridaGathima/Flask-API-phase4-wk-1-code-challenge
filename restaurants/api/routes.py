from api import db, api
from flask_restful import Resource, reqparse
from .models import db, Restaurant, Pizza, RestaurantPizza
from .serializer import response_serializer
from .serializer import response_serializer1
from .serializer import response_serializer2


from datetime import datetime
from flask import make_response, jsonify

parser = reqparse.RequestParser()
parser.add_argument('pizza_id')
parser.add_argument('restaurant_id')
parser.add_argument('price')
parser.add_argument('created_at')
parser.add_argument('updated_at')
class Index(Resource):
    def get(self):
        response = {
            "index": "Welcome to my RestFull API"}

        return  make_response (jsonify(response))
api.add_resource(Index, '/')    

class RestaurantList(Resource):
  
    def get(self):
        restaurants = Restaurant.query.all()
        response = response_serializer2(restaurants)
        return make_response(jsonify(response), 200 )
    
class PizzaList(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        response = response_serializer1(pizzas) 
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

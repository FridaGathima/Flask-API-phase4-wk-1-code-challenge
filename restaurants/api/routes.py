from api import db, api
from flask_restful import Resource, reqparse
from flask import request
from .models import db, Restaurant, Pizza, RestaurantPizza
from .serializer import response_serializer
from .serializer import response_serializer1
from .serializer import response_serializer2


from datetime import datetime
from flask import app, make_response, jsonify

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
    
class RestaurantPizzaResource(Resource):
    def get(self):
        restaurantpizzas = RestaurantPizza.query.all()
        response = response_serializer(restaurantpizzas)
        return response, 200

    def post(self): 
        try:
            data = request.get_json()
            rp = RestaurantPizza(
                price=data["price"],
                pizza_id=data["pizza_id"],
                restaurant_id=data["restaurant_id"]
            )
            db.session.add(rp)
            db.session.commit()
            pizza = Pizza.query.filter_by(id=data["pizza_id"]).first()
            pizza_dict = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            }

            response = make_response(jsonify(pizza_dict), 201)

            return response
        except ValueError as e:
            response = make_response(jsonify({"errors": e.args}), 400)
            return response
        except Exception as e:
            response = make_response(jsonify({"errors": e.args}), 400)
            return response


        # new_data = RestaurantPizzaPost(**data)


class RestaurantId(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            pizzas = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in restaurant.pizzas]
            response = {
                "id":restaurant.id,
                "name":restaurant.name,
                "address":restaurant.address,
                "pizzas": pizzas
            }
            return make_response(jsonify(response), 200 )
        else: 
            return make_response(jsonify({"error": "Restaurant not found"}), 404 ) 
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id=id).delete()
            db.session.delete(restaurant)
            db.session.commit()
            return make_response("", 204 )
        else:
            return make_response(jsonify({"error": "Restaurant not found"}), 404 ) 

        
api.add_resource(RestaurantList, "/restaurants") 
api.add_resource(PizzaList, "/pizzas")
api.add_resource(RestaurantPizzaResource, "/restaurant_pizzas")
api.add_resource(RestaurantId, '/restaurants/<int:id>')

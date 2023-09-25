from api import db, api
from flask_restful import Resource
from .models import Restaurant #RestaurantPizza
from .serializer import response_serializer

class RestaurantList(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        response = response_serializer(restaurants)
        return response, 200

    def post(self):
        pass



api.add_resource(RestaurantList, "/restaurants") 

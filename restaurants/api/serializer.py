from .models import Restaurant, Pizza, RestaurantPizza

def response_serializer2(restaurants: Restaurant):
    response = []
    for restaurant in restaurants:
        restaurant_dict = {
            "id":restaurant.id,
            "name":restaurant.name,
            "address":restaurant.address,
        }
        response.append(restaurant_dict)
    return response
 
def response_serializer1(pizzas: Pizza):
    response_pizza = []
    for pizza in pizzas:
        pizza_dict = {
            "id":pizza.id,
            "name":pizza.name,
            "ingredients":pizza.ingredients,
            "created_at":str(pizza.created_at),
            "updated_at":str(pizza.updated_at),
        }
        response_pizza.append(pizza_dict)
    return response_pizza

def response_serializer(restaurantpizzas: RestaurantPizza):
    response_restaurantpizza = []
    for restaurantpizza in restaurantpizzas:
        resstaurantpizza_dict = {
            "id":restaurantpizza.id,
            "price":restaurantpizza.price,
            "pizza_id":restaurantpizza.pizza_id,
            "restaurant_id":restaurantpizza.restaurant_id,
            "created_at":str(restaurantpizza.created_at),
            "updated_at":str(restaurantpizza.updated_at),
        }
        response_restaurantpizza.append(resstaurantpizza_dict)
    return response_restaurantpizza


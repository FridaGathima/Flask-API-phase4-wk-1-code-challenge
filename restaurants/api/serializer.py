from .models import Restaurant

def response_serializer(restaurants: Restaurant):
    response = []
    for restaurant in restaurants:
        restaurant_dict = {
            "id":restaurant.id,
            "name":restaurant.name,
            "address":restaurant.address,
        }
        response.append(restaurant_dict)
    return response

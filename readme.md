<h1>Flask Code Challenge - Pizza Restaurants</h1>

For this assessment, you'll be working with a Pizza Restaurant domain.

Your job is to build out the Flask API to add the functionality described in the deliverables below.

Test you endpoints as stated below:

 - Running the Flask server and using Postman to make requests

<h2>Models</h2>

You need to create the following relationships:

    - A Restaurant has many Pizzas through RestaurantPizza

    - A Pizza has many Restaurants through RestaurantPizza

    - A RestaurantPizza belongs to a Restaurant and belongs to a Pizza

<h2>Validations</h2>

Add validations to the RestaurantPizza model:

    - must have a price between 1 and 30

Add validations to Restaurant Model:

    - must have a name less than 50 words in length

    - must have a unique name

<h2>Routes</h2>

Set up the following routes. Make sure to return JSON data in the format specified along with the appropriate HTTP verb.

<h3>GET /restaurants</h3>

Return JSON data in the format below:

[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]

<h3>GET /restaurants/:id</h3>

If the Restaurant exists, return JSON data in the format below:

{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}

If the Restaurant does not exist, return the following JSON data, along with the appropriate HTTP status code:

{
  "error": "Restaurant not found"
}

<h3>DELETE /restaurants/:id</h3>

If the Restaurant exists, it should be removed from the database, along with any RestaurantPizzas that are associated with it (a RestaurantPizza belongs to a Restaurant, so you need to delete the RestaurantPizzas before the Restaurant can be deleted).

After deleting the Restaurant, return an empty response body, along with the appropriate HTTP status code.

If the Restaurant does not exist, return the following JSON data, along with the appropriate HTTP status code:

{
  "error": "Restaurant not found"
}

<h3>GET /pizzas</h3>

Return JSON data in the format below:

[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]

<h3>POST /restaurant_pizzas</h3>

This route should create a new RestaurantPizza that is associated with an existing Pizza and Restaurant. It should accept an object with the following properties in the body of the request:

{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
If the RestaurantPizza is created successfully, send back a response with the data related to the Pizza:

{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
If the RestaurantPizza is not created successfully, return the following JSON data, along with the appropriate HTTP status code:

{
  "errors": ["validation errors"]
}

<h2>Languages</h2>

- Python
- Github
- Git
- SQLAlchemy
- Flask

<h2>Author</h2>

Frida Nduta Gathima 

<h2>Licence</h2>

Copyright (c) 2023 Frida Nduta Gathima.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files , to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# dictionary and the list of the dictionary in the dictionary

restaurant = {
    "name": "The House of Elliot",
    "address": "1234 Main St",
    "phone no": "555-1234",
    "operating hours": "10am - 10pm",
    "rating": 5,
    "food": [
        {
            "name": "Pizza",
            "price": 12.99,
            "description": "Delicious pizza with your choice of toppings",
            "image": "pizza.jpg"
        },
        {
            "name": "Burger",
            "price": 8.99,
            "description": "Juicy burger with your choice of toppings",
            "image": "burger.jpg"
        },
        {
            "name": "Salad",
            "price": 7.99,
            "description": "Fresh salad with your choice of toppings",
            "image": "salad.jpg"
        }
    ]
}

print(restaurant["name"])
print(restaurant["operating hours"])
print(restaurant["food"][0])
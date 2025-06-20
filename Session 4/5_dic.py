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


chat = {
    "bisman":[
        {
            "by":"bisman",
            "message":"hello",
            "sent": "10.00 AM",
            "recived": "10.01 AM",
            "read": "10.01 AM",
        },
        {
            "by":"himanshu",
            "message":"how are you???",
            "sent": "10.10 AM",
            "recived": "10.15 AM",
            "read": "10.31 AM",
        },
        {
            "by":"bisman",
            "message":"Nothing free",
            "sent": "11.00 AM",
            "recived": "11.00 AM",
            "read": "11.10 AM",
        }
    ],
    "Jaiveer":[
        {
            "by":"Jaiveer",
            "message":"hello",
            "sent": "10.00 AM",
            "recived": "10.01 AM",
            "read": "10.01 AM",
        },
        {
            "by":"himanshu",
            "message":"how are you???",
            "sent": "10.10 AM",
            "recived": "10.15 AM",
            "read": "10.31 AM",
        },
        {
            "by":"Jaiveer",
            "message":"Nothing free",
            "sent": "11.00 AM",
            "recived": "11.00 AM",
            "read": "11.10 AM",
        }
    ]
}
# menu and the prices are the list and they are mutable
# wrong way
menu = ["espresso", "latte", "cappuccino"]
prices = [200, 250, 300]

print(menu[0]," : ", prices[0])

restaurant_menu = {
    "espresso": 200,
    "latte": 250,
    "cappuccino": 300
}

print(restaurant_menu["espresso"])
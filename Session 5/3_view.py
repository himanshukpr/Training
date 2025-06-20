# view reperesents an interface for displaying data
form_location = input("Enter From location: ")
travellers = int(input("Enter number of travellers: "))
feedback = float(input("Enter feedback (1 - 5): "))

# here we are binding the model with the view
flight_booking = {
    "from": form_location,
    "travellers": travellers,
    "feedback": feedback
}

print(flight_booking)
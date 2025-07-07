from car import Car
from linkedlist import CarList


car1 = Car('BMW','black')
car2 = Car('23','black')
car3 = Car('3','black')


cars = CarList()
cars.add(car1)
cars.add(car2)
cars.add(car3)

cars.show()
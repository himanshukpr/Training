from car import Car
from linkedlist import CarList


car1 = Car('BMW','black')
car2 = Car('BMW2','black')
car3 = Car('supra','black')
car4 = Car('3','black')

cars = CarList()
cars.add(car1)
cars.add(car2)
cars.add(car3)
cars.add(car4)

cars.show()

print('-----------------------------')
cars.tail_delete()
cars.show()

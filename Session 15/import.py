from car import Car
from linkedlist import CarList


car1 = Car('BMW','black')
car2 = Car('BMW2','black')
car3 = Car('supra','black')
car4 = Car('3','black')
# car4 = Car('3','black')
car5 = Car('Saffari','white')


car6 = Car('in_between','white')

cars = CarList()
cars.add(car1)
cars.add(car2)
cars.add(car3)
cars.add(car4)

cars.add_in_front(car5)

print('---------------------------------------------------------------------------------------')
# cars.head_delete()


print('---------------------------------------------------------------------------------------')
cars.add_in_between('BMW2',car6)
cars.show()

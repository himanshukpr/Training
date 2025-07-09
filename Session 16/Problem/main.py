from Product import Product_info
from Cart_linkedlist import Cart

product1 = Product_info('1 laptop',100,2)
product2 = Product_info('2 mobile',400,12)
product3 = Product_info('3 tablet',300)
product4 = Product_info('6 tablet',50)


cart = Cart()
cart.add(product1)
cart.add(product2)
cart.add(product3)
cart.add(product4)


print('---------------------------------')
cart.sort()
cart.show()

# print(cart.head)
# print(cart.tail)
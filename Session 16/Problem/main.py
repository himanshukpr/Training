from Product import Product_info
from Cart_linkedlist import Cart

product1 = Product_info('1 laptop',500,2)
product2 = Product_info('2 mobile',1500,12)
product3 = Product_info('3 tablet',5000)


cart = Cart()
cart.add(product1)
cart.add(product2)
cart.add(product3)


cart.update_quantity("1 laptop",quantity=0)
cart.show()

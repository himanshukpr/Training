coupon_code = input('Enter the coupon code: ')
billing_amount = int(input('Enter the billing amount: '))


# # simple if/else
# if billing_amount > 449:
#     print('Coupon can be applied')
#     print('Thank you')
# else:
#     print('Add items worth 449 or more to avail the coupon')



# nested if (filteration)
if coupon_code == 'zomato':
    if billing_amount > 449:
        billing_amount -= 150
        print('please pay: ', billing_amount)
        print('Thank you')
    else:
        print('Add items worth 449 or more to avail the coupon',(449 - billing_amount + 1), 'more worth items are required')
        print('please pay: ', billing_amount)

else:
    print('coupon code is invalid')
    print('please pay: ', billing_amount)

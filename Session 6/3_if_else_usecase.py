coupon_code = input("Enter the coupon code: ")
billing_amount = float(input("Enter the billing amount: "))


if coupon_code == 'zomato':
    if billing_amount >= 300:
        discount =  billing_amount * .20
        billing_amount = billing_amount - discount
        print("Coupon applied successfully")
        print("Please pay: \u20B9", billing_amount)
        print("discount is \u20B9", discount)
    else:
        print('Must add items worth \u20B9 300 or more to avail the coupon')
        print(300 - billing_amount, 'more worth items are required')
        print("Please pay: \u20B9", billing_amount)

elif coupon_code == 'bingo':
    if billing_amount >= 500:
        discount =  billing_amount * .50
        if discount > 150:
            discount = 150
        billing_amount = billing_amount - discount
        print("Coupon applied successfully")
        print("Please pay: \u20B9", billing_amount)
        print("discount is \u20B9", discount)
    else:
        print('Must add items worth 300 or more to avail the coupon')
        print(300 - billing_amount, 'more worth items are required')
        print("Please pay: \u20B9", billing_amount)

else:
    print("Coupon code is invalid")
    print("Please pay", billing_amount)
price = input('Enter the price: ')
price = int(price)
discount = input('Enter discount %: ')
discount = int(discount)
price_with_discount = price - (price * discount / 100)
reduction_amount = price * discount / 100
print(f'The price with dicount is {price_with_discount}')
print(f'The reduction amount is {reduction_amount}' )


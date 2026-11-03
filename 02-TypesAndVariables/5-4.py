# A program that calculates VAT for a given price.

price = input('Enter the price: ')
price = int(price)
VAT = input(' Enter THE VAT percentage: ')
VAT = int(VAT)
VAT_amount = price * VAT / 100
print(f' The VAT amount is {VAT_amount}')

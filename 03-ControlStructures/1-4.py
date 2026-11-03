###
# Credit card payment 
#
account_balance = 1200
total_payment = int(input('Enter total payment: '))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')
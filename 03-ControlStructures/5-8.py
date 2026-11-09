###
# ATM (cash machine) simulator
#
import sys
check_pin = 0
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code
check_pin = str(input("Enter PIN: "))
valid_pin = 0
if len(check_pin) == 4 and check_pin.isdigit():
    if pin == check_pin:
        valid_pin = 1
        print("Welcome!")

if valid_pin == 0:
    print("Wrong PIN")
    sys.exit()

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change pin")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Change pin")
        new_pin = str(input("Enter new pin: "))
        if len(new_pin) == 4:
            if new_pin.isdigit():
               print("You have new PIN.")
            else:
               print("Your PIN can only contain digits")
        else:
            print("Your pin can only contain 4 digits")
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
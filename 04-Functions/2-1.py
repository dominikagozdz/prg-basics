###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

read_letter = input("Enter a letter:")
print('You entered the letter', read_letter)

nb = "20303"
convert_number = int(nb)
print(f"Your number is: {convert_number}")

binary_string = bin(304)
print("binary string representing decimal number 304 is:", binary_string)

hexadecimal_string = hex(304)
print('hexadecimal string representing decimal number 304 is:', hexadecimal_string)

unicode_code = ord('€')
print(f'integer representing the Unicode code of the € sign is {unicode_code}')

alsolute_number = abs(-17)
print('absolute value of -17 is:', alsolute_number)
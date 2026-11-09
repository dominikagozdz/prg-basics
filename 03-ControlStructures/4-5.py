###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''
plain_text_code = 0


for char in plain_text:
    plain_text_code = ord(char)
    # read the character's code (use ord())
    plain_text_code = plain_text_code + 1
    # add one to the character's code
    encrypted_text = encrypted_text + chr(plain_text_code) 
    # replace new character code with its
    # corresponding character (use chr())
    # add encrypted character to encrypted text
print(plain_text)
print(encrypted_text)
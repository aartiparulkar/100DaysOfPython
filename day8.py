alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


# def encrypt(original_text, shift_amount):
#     encrypted_text = ''
#     for ch in original_text:
#         if ch.isalpha():
#             encrypted_ch_idx = (ord(ch.lower()) - ord('a') + shift_amount) % 26
#             encrypted_text += alphabet[encrypted_ch_idx]
#         else:
#             encrypted_text += ch
#     return encrypted_text


# def decrypt(original_text, shift_amount):
#     decrypted_text = ''
#     for ch in original_text:
#         if ch.isalpha():
#             decrypted_ch_idx = (ord(ch) - ord('a') - shift_amount) % 26
#             decrypted_text += alphabet[decrypted_ch_idx]
#         else:
#             decrypted_text += ch
#     return decrypted_text


# Combining encrypt() and decrypt() into one function
def caesar(operation, message, shift_amt):
    if operation == 'decode':
        shift_amt *= -1
        
    cipher_text = ''
    for ch in message:
        if ch.isalpha():
            ciphered_id = (alphabet.index(ch.lower()) + shift_amt) % 26
            cipher_text += alphabet[ciphered_id]
        else:
            cipher_text += ch
    print(f"This is your {operation}d message: {cipher_text}")
    return cipher_text


continue_cipher = True
while continue_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(operation=direction, message=text, shift_amt=shift)

    choice = input("Do you want to go again? Type 'yes' or 'no'. ")
    
    if choice == "no":
        continue_cipher = False

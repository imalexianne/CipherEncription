letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '  

num_letters = len(letters) 

def encrypt_decrypt(text, key):
    result = ''
      
    for letter in text:
        letter = letter.upper()
#         if not letter == '':
        index = letters.find(letter)
            # an entered character is not found in letters
#         
        if index == -1:
            result += letter
        else:
         
                # e mode ( Encription)
            new_index = index + key
               
            if new_index >= num_letters:
                    # Example:Y==>24 + 3 ==>letters[27]==> 27 - 26 =1  ==>letters[1] ==>B
                new_index -= num_letters  
         
            result += letters[new_index]        
            #letters[-7]
    return result
        
print()
print('*** CAESAR CIPHER PROGRAM ***')
print()


print('DECRYPTION MODE ACTIVATED')
print()
key =int(input('Enter the key: '))
text = input('Enter the text to encrypt: ')
ciphertext = encrypt_decrypt(text, key)
print(f'CIPHERTEXT: {ciphertext}')


import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

original_msg = input("Enter a message to encrypt: ")
encrypted_msg = ''
decrypted_msg = ''
for letter in original_msg:
    encrypted_msg += keys[chars.index(letter)]
print(f"Encrypted message: ${encrypted_msg}")

encrypted_msg = input("Enter a message to decrypt: ")
for letter in encrypted_msg:
    decrypted_msg += chars[keys.index(letter)]
print(f"Decrypted message: ${decrypted_msg}")


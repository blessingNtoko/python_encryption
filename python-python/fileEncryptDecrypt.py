from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Generate key from password
password_provided = input("Please type in your password in order to generate a key: ") # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)


# Encrypt
input_file = 'test.txt'
output_file = 'test.encrypted'

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)
    
    

# Decrypt
input_file = 'test.encrypted'
output_file = 'tested.txt'

with open(input_file, 'rb') as f:
    data = f.read()

decrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(decrypted)
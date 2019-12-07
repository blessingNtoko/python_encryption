import cryptography
from cryptography.fernet import Fernet





message = "my deep dark secret".encode()
key = Fernet.generate_key()
f = Fernet(key)

encrypted = f.encrypt(message)
print(encrypted)

decrypted = f.decrypt(encrypted)
print(decrypted)

print(message == decrypted)


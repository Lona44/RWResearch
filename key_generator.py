from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

with open('rw_key.key', 'wb') as filekey:
    filekey.write(key)

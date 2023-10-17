import Cryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def decrypt_file(localpath, key):
    with open(localpath, 'rb') as file:
        nonce = file.read(16)
        tag = file.read(16)
        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    # localpath = localpath[:-4]  # Remove the '.enc' extension
    with open(localpath, 'wb') as decrypted_file:
        decrypted_file.write(plaintext)



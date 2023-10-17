import paramiko
from scp import SCPClient
import Cryptodome
import socket
import os
from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

load_dotenv()

host1 = os.getenv('host1')
password = os.getenv('password1')
port1 = os.getenv('port1')
hostname1 = os.getenv('hostname1')

def pad_data(data):
    block_size = AES.block_size
    return data + (block_size - len(data) % block_size) * chr(block_size - len(data) % block_size)

def encrypt_file(filepath, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(filepath, 'rb') as file:
        plaintext = file.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    with open(filepath + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(cipher.nonce)
        encrypted_file.write(tag)
        encrypted_file.write(ciphertext)

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


def Transportation(host, username, password):
    ssh_client = paramiko.SSHClient()
    # sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('connection started')
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, 22 ,username,password)
    ftp_client=ssh_client.open_sftp()

    filepath = '/home/lain/spaghetti.txt'
    localpath = '/home/lain/spaghetti.txt'
    key = get_random_bytes(32)
    encryptedFile = encrypt_file(localpath, key)
    localpath = (f"{localpath}.enc")
    print(f"sending {localpath} to {host1}")
    ftp_client.put(localpath, filepath)
    print("send successfully")
    scp = SCPClient(ssh_client.get_transport())
    scp.put(('remotedecrypt.py'),'/home/lain/remotedecyrpt.py')
    decrption_command = (f"python -c from /home/lain/remotedecrypt.py import decryptfile; decryptfile({filepath}).")
    ssh_client.exec_command('')
    ftp_client.close()



Transportation(host1, 'root', password)
    

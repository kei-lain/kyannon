import paramiko
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

def Transportation(host, username, password):
    ssh_client = paramiko.SSHClient()
    # sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('connection started')
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, 22 ,username,password)
    ftp_client=ssh_client.open_sftp()

    filepath = '/home/lain/dockerimages.txt.enc'
    localpath = '/home/lain/dockerimages.txt'
    key = get_random_bytes(32)
    encryptedFile = encrypt_file(localpath, key)
    localpath = (f"{localpath}.enc")
    print(f"sending {localpath} to {host1}")
    ftp_client.put(localpath, filepath)
    ftp_client.close()



Transportation(host1, 'root', password)
    

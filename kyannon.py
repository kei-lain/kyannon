import paramiko
from scp import SCPClient
import Cryptodome
import socket
import os
from dotenv import load_dotenv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import argparse
import pathlib 

# load_dotenv()

# host1 = os.getenv('host1')
# password = os.getenv('password1')
# port1 = os.getenv('port1')
# hostname1 = os.getenv('hostname1')

parser = argparse.ArgumentParser(description='This is Kyannon. Kyannnon is a cli tool that encrypts files before sending over sftp!!')
parser.add_argument('-host', help='This is the argument that will list the host that you want to send the file(s) to')
parser.add_argument('-password', help='This argument inputs the password for the host')
parser.add_argument('-username', help='This argument inputs the username for the host')
parser.add_argument('-port', help='This argument inputs the port number')
parser.add_argument('-file',type=pathlib.Path , help='This argument inputs the file that will be sent over')
parser.add_argument('-endfile',type=pathlib.Path , help='This argument inputs where the files will be sent')
args = parser.parse_args()

def pad_data(data):
    block_size = AES.block_size
    return data + (block_size - len(data) % block_size) * chr(block_size - len(data) % block_size)

def encrypt_file(filepath, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(filepath, 'rb') as file:
        plaintext = file.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    with open(str(filepath) + '.enc', 'wb') as encrypted_file:
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


def Transportation(host, username, password, newfile,orignfile):
    ssh_client = paramiko.SSHClient()
    # sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('connection started')
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, 22 ,username,password)
    ftp_client=ssh_client.open_sftp()

    # filepath = '/home/lain/spaghetti.txt'
    filepath = newfile
    localpath = orignfile
    # localpath = '/home/lain/spaghetti.txt'
    key = get_random_bytes(32)
    encryptedFile = encrypt_file(localpath, key)
    localpath = (f"{localpath}.enc")
    print(f"sending {localpath} to {host}")
    ftp_client.put(localpath, filepath)
    print("send successfully")
    scp = SCPClient(ssh_client.get_transport())
    scp.put(('remotedecrypt.py'),'/home/lain/remotedecyrpt.py')
    decrption_command = (f"python -c from /home/lain/remotedecrypt.py import decryptfile; decryptfile({filepath}).")
    ssh_client.exec_command(decrption_command)
    ftp_client.close()



# Transportation(host1, 'root', password)
if __name__ == "__main__":
    # nfs = pathlib.PosixPath(str(args.endfile))
    # ofs = pathlib.PosixPath(str(args.file))
    # for nf in nfs.iterdir():
    #     for of in ofs.iterdir():
    #         Transportation(args.host,args.username,args.password, nf, of)
    Transportation(args.host,args.username,args.password,str(args.endfile), str(args.file))
            
        



    


    

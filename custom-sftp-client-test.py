import paramiko
import Cryptodome
import socket
import os
from dotenv import load_dotenv

load_dotenv()

host1 = os.getenv('host1')
password = os.getenv('password1')
port1 = os.getenv('port1')
hostname1 = os.getenv('hostname1')


def Transportation(host, username, password):
    ssh_client = paramiko.SSHClient()
    # sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('connection started')
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, 22 ,username,password)
    ftp_client=ssh_client.open_sftp()
    filepath = '/home/lain/testftp-file.txt'
    localpath = '/home/lain/test.txt'
    ftp_client.put(localpath, filepath)
    ftp_client.close()


    # try:
       
    #     # check = sock.connect_ex((host,port))  #attempts to see if the port the user chose is open
    #     # print()
    #     # if check == 0 :

    #     #     # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     #     transport = paramiko.Transport((host,port)) 
            

    #     # else:
    #     #     print(f'port {port} is not open')
    #     transport = paramiko.Transport((host,22))

    #     transport.connect(host,username,password)
    #     # ssh_client.connect(host,port=port,username=username,password=password)
    #     print("starting transport")
    #     sftp = paramiko.SFTPClient.from_transport(transport)

    #     ftp = ssh_client.open_sftp()
    #     filepath = "/"
    #     localpath = "/home/lain/Pictures/testftp-file.txt"
    #     sftp.put(localpath,filepath)
    #     if sftp: sftp.close()
    #     if transport: transport.close()


    
    # except:
    #     print("Something went wrong")
            
# else:
#     transport = paramiko.Transport(host, )


Transportation(host1, 'root', password)
    

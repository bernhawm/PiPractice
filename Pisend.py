import paramiko
from paramiko import SSHClient
from scp import SCPClient
from dotenv import load_dotenv
import os

load_dotenv()  # This loads the .env file

def create_ssh_client(host, port, username, password):
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, password=password)
    return client

def send_file_to_raspberry_pi(file_path, remote_path, host, port, username, password):
    ssh = create_ssh_client(host, port, username, password)
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(file_path, remote_path)

# Replace these variables with your Raspberry Pi's details
raspberry_pi_ip = os.getenv('IP') # Raspberry Pi IP address
ssh_port = 22                     # SSH port, usually 22
ssh_username = os.getenv('user')              # SSH username, usually 'pi' for Raspberry Pi
ssh_password = os.getenv('password')    # SSH password

# File to send and destination path on Raspberry Pi
local_file_path = 'TestFile.txt'
remote_file_path = 'TestFile.txt'

send_file_to_raspberry_pi(local_file_path, remote_file_path, raspberry_pi_ip, ssh_port, ssh_username, ssh_password)

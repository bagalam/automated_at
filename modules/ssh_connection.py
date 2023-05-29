import paramiko

def connect():
    ssh_client = paramiko.SSHClient()
    #ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="192.168.1.1",port=22,username="root",password="Admin123")
    return ssh_client

def get_modem(ssh_client):
    stdin, stdout, sterr = ssh_client.exec_command("gsmctl -w")
    stdin.close()
    modem = stdout.read().decode()
    
    stdin, stdout, sterr = ssh_client.exec_command("gsmctl -m")
    stdin.close()
    modem_model = stdout.read().decode()
    return modem, modem_model
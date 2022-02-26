import getpass
import paramiko
SSH_PORT = 22

def ssh_run_cmd(host,username,password,command,port=SSH_PORT):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    #client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connect using username and password
    client.connect(host, port, username, password)
    # execute a command
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read()
    for line in output.splitlines():
        print(line.decode())
    client.close()
    print('Completed. Connection Closed')

if __name__ == '__main__':
    host = input('Enter the target host: ')
    username = input('Enter username: ')
    password = getpass.getpass(prompt='Enter password: ')
    command = input('Enter command: ')
    ssh_run_cmd(host, username, password, command)

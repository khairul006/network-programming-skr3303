import paramiko
import getpass
SSH_PORT = 22

def run_sftp(host, username, password, port=SSH_PORT):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)

    # open sftp session
    sftp = client.open_sftp()
    # upload from localhost to remote host
    local_path = '/home/kai/dsproject/upm.png'
    remote_path = 'c:\\users\\khair\\desktop\\test-sftp\\upm.png'
    sftp.put(local_path, remote_path)
    print('Sent')

    # download from remote host to local host
    local_path = '/home/kai/dsproject/smiley.png'
    remote_path = 'c:\\sers\\khair\\desktop\\test-sftp\\smiley.png'
    sftp.get(remote_path, local_path)
    print('Received')
    sftp.close()
    print('Completed. Connection Closed')

if __name__ == '__main__':
    host = input('Enter the target host:')
    username = input('Enter username: ')
    password = getpass.getpass(prompt='Enter password: ')
    run_sftp(host, username, password)

import paramiko
import time
import sys

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

ip = 'ip-publik-disini'
username = 'admin'
password = 'tulis-password-disini'
port=22
remote_conn_pre = paramiko.SSHClient()
print('successfuly configured the SSH client')

# print remote_conn_pre

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip, username=username, password=password, port=port)

remote_conn = remote_conn_pre.invoke_shell()
outpt = remote_conn.recv(65535)  # read as much as you can.


stdin,stdout,stderr = remote_conn_pre.exec_command('\n')

time.sleep(1)

stdin,stdout,stderr = remote_conn_pre.exec_command('/export')
sys.stdout = Logger("/Users/macbookpro/export-router.txt")
print stdout.read()

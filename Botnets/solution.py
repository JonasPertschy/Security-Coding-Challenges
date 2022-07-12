# Solution based on paramiko and pqdm
# Read targets

import sys
from pqdm.threads import pqdm
from paramiko import SSHClient


targets = []
for target in open('target_machines.txt','r').readlines():
    targets.append(target.strip().split('@')) # Clean linefeed

print(targets)
print('Read ',len(targets),' targets')

def execute(target):
    username,server = target
    command = sys.argv[1]
    client = SSHClient()
    client.load_system_host_keys()
    client.connect(server,username=username)
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.readlines()

result = pqdm(targets, execute, n_jobs=2)
print(result)

#debug testcase
#print(execute(["root","127.0.0.1"]))
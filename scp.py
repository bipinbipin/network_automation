from paramiko import SSHClient
from paramiko import AutoAddPolicy
from scp import SCPClient

from device_list import *


# connects to scp server
def createSSHClient(**kwargs):
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(kwargs["server"], kwargs["port"], kwargs["user"], kwargs["password"])
    return client

ssh = createSSHClient(**scp_server)
scp = SCPClient(ssh.get_transport())

# scp.put('FooBar.txt')
scp.get('FooBar.txt')
scp.close()
# file = scp.get('FooBar.txt')
# print(file)
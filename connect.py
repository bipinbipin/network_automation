
from netmiko import ConnectHandler
from device_list import *

# connects to device
# router1_connect = ConnectHandler(**router1)

# runs simple command
# output = router1_connect.send_command("show ip int brief")
# print(output)
#
# output = router1_connect.send_command("show run")
# print(output)


def run_command_on_device(device, command):
    print("\n\nConnecting to device: " + device['ip'])
    connect = ConnectHandler(**device)
    print(connect.send_command(command))


# run command on list of devices
def run_command_on_list_of_devices(all_devices, command):
    for device in all_devices:
        run_command_on_device(device, command)


run_command_on_device(router1, "show ip int brief")
# run_command_on_list_of_devices(all_routers, "u all")




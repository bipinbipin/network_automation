router1 = {
    'device_type': 'cisco_ios',
    'ip': '10.2.131.21',
    'username': 'admin',
    'password': 'cisco'
}
router2 = {
    'device_type': 'cisco_ios',
    'ip': '10.2.131.22',
    'username': 'admin',
    'password': 'cisco'
}
router3 = {
    'device_type': 'cisco_ios',
    'ip': '10.2.131.23',
    'username': 'admin',
    'password': 'cisco'
}

all_routers = [router1, router2, router3]

scp_server = {
    'server': '10.2.131.30',
    'port': 22,
    'user': 'cisco',
    'password': '1234'
}

scp_server_on_router = {
    'server': '10.2.131.21',
    'port': 22,
    'user': 'admin',
    'password': 'cisco'
}
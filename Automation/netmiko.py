from netmiko import ConnectHandler

connection_parameters = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.1.88',
    # credentials to log in to the device
    'username': 'cisco',
    'password': 'cisco',
    # secret is the password required to enter privileged mode
    'secret': 'cisco',
}

# log in to the device
net_connect = ConnectHandler(**connection_parameters)

# enter privileged mode
net_connect.enable()

# display the configuration of the device
config = net_connect.send_command('show running-config')

# change the name of the device
add_description_to_interface = ['interface Fa0/0', 'description OSPF interface']
net_connect.send_config_set(add_description_to_interface)
net_connect.disconnect()
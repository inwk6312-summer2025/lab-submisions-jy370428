from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.106",
        "username": "student",
        "password": "Meilab123",
        "port": "22"},
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.107",
        "username": "student",
        "password": "Meilab123",
        "port": "22"},
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.108",
        "username": "student",
        "password": "Meilab123",
        "port": "22"},
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.109",
        "username": "student",
        "password": "Meilab123",
        "port": "22"}
]

for device in devices:
    net_connect = Netmiko(**device)
    print(f"Default prompt: {net_connect.find_prompt()}")
    net_connect.send_command_timing("disable")
    print(f"Disable command: {net_connect.find_prompt()}")
    net_connect.enable()
    print(f"Enable command: {net_connect.find_prompt()}")

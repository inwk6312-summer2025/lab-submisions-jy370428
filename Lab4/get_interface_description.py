from netmiko import ConnectHandler
r1 = {"device_type": "cisco_ios",
        "ip": "192.168.1.106",
        "username": "student",
        "password": "Meilab123",
        "port": "22"}
r2 = {"device_type": "cisco_ios",
        "ip": "192.168.1.107",
        "username": "student",
        "password": "Meilab123",
        "port": "22"}
for device in (r1, r2):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show ip interface brief")
    net_connect.disconnect()
    print("-"*100)
    print(output)
    print("-"*100)

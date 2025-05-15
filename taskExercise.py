from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-taskExercise.j2")

inter_dict = {
    "R2": "Loopback0- IP:150.1.2.2/32 and GigabitEthernet1/12- IP:155.1.12.2/24",
    "R3": "Loopback0- IP:150.1.3.3/32 and GigabitEthernet1/13- IP:155.1.13.3/24",
    "R4": "Loopback0- IP:150.1.4.4/32 and GigabitEthernet1/14- IP:155.1.14.4/24",
    "R1": "Loopback0- IP:150.1.1.1/32 and GigabitEthernet0/12- IP:155.1.12.1/24, GigabitEthernet0/13- IP:155.1.13.1/24, GigabitEthernet1/14- IP:IP:155.1.14.1/24"
}

print(template.render(interface_dict=inter_dict))

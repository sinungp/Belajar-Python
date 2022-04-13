import yaml
import os

netplan2={'network': {'ethernets': {'ens18': {'addresses': ['172.20.15.51/24'], 'gateway4': '172.20.15.1', 'nameservers': 
{'addresses': ['8.8.8.8', '8.8.4.4'], 'search': []}}}, 'version': 2}}

with open('/etc/netplan/00-installer-config.yaml', 'w') as f:
    
    data = yaml.dump(netplan2, f)

os.system("sudo netplan apply")


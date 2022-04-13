#Change IP & Gateway In Ubuntu Server 20.04
import pyaml as yaml
import ipaddress
import os

def ipEntered():
    while True:
        try:
            return ipaddress.ip_address(ip)
        except ValueError:
            print("ip tidak valid")

def gwEntered():
    while True:
        try:
            return ipaddress.ip_address(gateway)
        except ValueError:
            print("ip tidak valid")

ip = input('input ip/subnet ')
gateway = input('input gateway ')


ethernets = {'ethernets': {'ens18': {'addresses': [ip], 'gateway4': gateway, 'nameservers': {'addresses': ['8.8.8.8', '8.8.4.4'], 'search': []}}}, 'version': 2}

with open('/etc/netplan/00-installer-config.yaml', 'w') as outfile:
    yaml.dump(ethernets, outfile, indent=4)

os.system("sudo netplan apply")
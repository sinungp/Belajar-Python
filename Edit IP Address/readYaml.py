# process_yaml.py file

import yaml

with open(r'netplan.yaml') as file_ip:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    ip_conf = yaml.load(file_ip, Loader=yaml.FullLoader)

    print(ip_conf)

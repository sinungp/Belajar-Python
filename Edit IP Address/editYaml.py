import sys
import ruamel.yaml

yaml = ruamel.yaml.YAML()
# yaml.preserve_quotes = True
with open('netplan.yaml') as fp:
    data = yaml.load(fp)
for elem in data:
    if elem['addresses'] == 'address':
         elem['gateway'] = '172.20.15.2'
         break  # no need to iterate further
yaml.dump(data, sys.stdout)

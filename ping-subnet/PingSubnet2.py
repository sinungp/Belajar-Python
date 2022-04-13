import ipaddress
from subprocess import Popen, PIPE, DEVNULL
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobapython"
)

def ipEntered():
    while True:
        try:
            return ipaddress.ip_address(ip)
        except ValueError:
            print("ip tidak valid")

# IP range
ip = input("Masukan Ip address : ")
network = ipaddress.ip_network(ip)

# Time between pings (ms)
delay = '50'

# Because it looks cool
def spinning_cursor():
    while True:
        for cursor in '|/—\\':
            yield cursor
spinner = spinning_cursor()

# Loop through subnet hosts
for i in network.hosts():
    i=str(i)
    octets = i.split(".")
    octet4 = octets[3]
    # fping command
    try:
        toping = Popen(['fping', '-c1', '-t', delay, '-q', i], stdout=DEVNULL, stderr=PIPE)
    except:
        print("fping is required")
        break
    output = toping.communicate()[0]
    hostalive = toping.returncode
    if hostalive == 0:
        print(i,'is ' + '\033[92m' + 'reachable' + '\033[0m')

    else:
        print(next(spinner), str(octet4), end="\r", flush=True)
        print(i,'is ' + '\033[91m' + 'unreachable' + '\033[0m')

        #Untuk memasukan ip yang tidak konek ke database
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO ipaddr (ip) VALUES (%s);", (i,))
        mydb.commit()

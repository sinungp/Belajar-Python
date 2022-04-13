import pyaml as yaml

name = input('What is your name? ')
age = int(input('What is your age? '))
nationality = input('What is your nationality? ')
footed = input('What foot? ')
position = input('What is your position? ')

person = {'Person':{
              'Name': name, 
              'Age': age, 
              'Nationality': nationality, 
              'Footed': footed, 
              'Position': position}
         }

with open('test.yml', 'a') as outfile:
    yaml.dump(person, outfile, indent=4)
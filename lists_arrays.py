'''
array is a numeric data type, non-mixed
lists are non-defined data-types, and mixed
'''
from datetime import datetime, timedelta


names = ['José Thomaz', 'João Vicente', 'Lenita Soares', 'Flavio Soares'] #list creation
print(len(names))#lenght, will return the number of items on your list
names.insert(0, 'Bill Gates') #defines the index, and then the value to fill
names.append('Florzonha Fofona') #add the value after the last space on the list
names.append('Lil Robot')
presenters = names[1:4]
print(presenters)
print(names)
names.sort() #will change the order of the indexes

print(names)


#JSON into Python
dict = {}
dict['name'] = 'José Thomaz'
dict['nacionality'] = 'Brazilian'
birthday = input('Tell us when is your bithday (dd/mm/yyyy) ...')
#dict['birthday'] = str(datetime.strptime(birthday, '%d/%m/%Y'))
print(dict)
print(dict['name'])
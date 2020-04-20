''' List comprehensions and the zip function ''' 
from random import randint 
from pprint import PrettyPrinter 

keys = range(1,5) 
values = range(10, 41, 10) 
print('Keys:', [key for key in keys]) 
print('Values:', [value for value in values]) 
tuple_list = zip(keys, values) 
print('List of tuples:', [pair for pair in tuple_list] ) 
zip_keys, zip_values = zip(*zip(keys, values)) 
# unzip 
print('Keys from zip:', [key for key in zip_keys])

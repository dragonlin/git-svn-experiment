
''' Demonstrate dictionary comprehension ''' 

keys = [1, 'a', 2, 'b', 3, 'c']

print('List keys:\n', keys) 
values = [100, 'apple', 200, 'berry', 300, 'cherry'] 
print('List values:\n', values) 

# New dictionary using zip 
bundle = dict(zip(keys, values)) 
print('Dictionary bundle:\n', bundle) 

# New dictionary using comprehension 
box = {k:v for (k,v) in zip(keys, values)} 
print('Dictionary box:\n', box) 

# New dictionaries using conditional comprehension and key/value expressions 
alpha = {k.upper():v for (k,v) in zip(keys, values) if isinstance(k,str)}

print('Dictionary alpha:\n', alpha)

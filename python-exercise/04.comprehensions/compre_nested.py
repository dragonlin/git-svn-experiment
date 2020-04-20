''' Demonstrate nested list comprehensions '''
from pprint import PrettyPrinter
matrix_a = [[1, 2, 3],    
    [4, 5, 6],    
    [7, 8, 9]]
matrix_b = [[2, 4, 6],
    [12, 15, 18],    
    [28, 32, 36]]

print(matrix_a)

rows = cols = range(1,10) 
mult_table = [[row * col for col in cols] for row in rows] 
# print(mult_table)
pp = PrettyPrinter()
pp.pprint(mult_table)
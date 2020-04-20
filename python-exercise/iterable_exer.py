''' Provide a class to model cartesian product tuples '''


class IterCartesian(object):
    ''' A data type with an interable containing cartesian products '''
    
    def __init__(self, a, b, c):        
        ''' Initialize the data type and perform type checking '''
        self.params = (a, b, c)
        self._type_check()
        self.product = self._product()
        self.current_index = 0
        self.last_index = len(self.product) - 1

    def _type_check(self):
        error_msg = 'Parameters must be "int" or "float" objects'
        for param in self.params:
            if not (isinstance(param, int) or isinstance(param, float)):
                raise RuntimeError(error_msg)

    def _product(self):
        params = sorted(self.params)
        product = []
        for outer in params:
            for inner in params:
                product.append((outer, inner))
        return tuple(product)

    def __iter__(self):
        return self
    
    def __next__(self):        
        if self.current_index > self.last_index:            
            raise StopIteration        
        else:            
            next_value = self.product[self.current_index]            
            self.current_index += 1            
        return next_value

if __name__ == '__main__':    
    a_product = IterCartesian(2, 6.4, 4.1) # valid data    
    for a_tuple in a_product: # Demonstrate iteration        
        print(a_tuple)    
    b_product = IterCartesian(2, 'a', [1,2,3]) # invalid data to raise error
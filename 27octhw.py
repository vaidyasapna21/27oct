class book :                                                                                                                                
    def __init__(self, t, p, pg):        #User_Define Method
        self.title = t
        self.price = p
        self.page = pg

    def add(self, other):
        return self.price + other.price
    
    def sub(self, other):
            return self.price - other.price
    
    def multi(self, other):
            return self.price * other.price   
    
    def div(self, other):
            return self.price / other.price 
    
    def floordiv(self, other):
            return self.price // other.price     
     
    def modu(self, other):
            return self.price % other.price
    
    def greater(self, other):
                return self.price > other.price 
    
    def smaller(self, other):
                return self.price < other.price   
    
    def grater_equal(self, other):
                return self.price >= other.price  
    
    def smaller_equal(self, other):
                return self.price <= other.price 
    
    def equal_equal(self, other):
                return self.price == other.price                             
         
    

    def __add__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
            return self.sub(other)
    
    
    def __multi__(self, other):
                return self.multi(other)    
    
    
    def __div__(self, other):
                return self.div(other)                   
            
    def __floordiv__(self, other):
                 return self.floordiv(other)    
    
    def __modu__(self, other):
                return self.modu(other)   
    
    def __grater__(self, other):
            return self.greater(other)  
    
    def __smaller__(self, other):
            return self.smaller(other)   
    
    def __grater_equal__(self, other):
            return self.grater_equal(other)  
    
    def __smaller_equal__(self, other):
            return self.smaller_equal(other)  
        
    def __equal_equal__(self, other):
            return self.equal_equal(other)                                
    
    
class book :                                                                                                                                
    def __init__(self, t, p, pg):      #SPECIAL METHOD  
        self.title = t
        self.price = p
        self.page = pg

    def add(self, other):
        return (self.price + other.price)

    def __add__(self, other):
        return self.add(other)
    
    
    def __sub__(self,other):
        return (self.price - other.price)
    
    def __mul__(self,other):
            return (self.price * other.price)
        
    def __truediv__(self,other):
                return (self.price * other.price)    

    def __floordiv__(self,other):
                return (self.price * other.price)
    
    def __mod__(self,other):
                return (self.price * other.price) 
    
    def __gt__(self,other):
                    return (self.price > other.price) 
    
    def __it__(self,other):
                    return (self.price < other.price)  
    
    def __ge__(self,other):
                    return (self.price >= other.price)  
    
    def __le__(self,other):
                    return (self.price <= other.price)   
    def __eq__(self,other):
                    return (self.price == other.price)                                                            

a1 = book("core python", 500, 200)
b2 = book("advance python", 800, 100)

print(a1 + b2)
print(a1.add(b2))
print(a1- b2)
print(a1*b2)
print(a1/b2)
print(a1//b2)
print(a1%b2)
print(a1> b2)
print(a1<b2)
print(a1>=b2)
print(a1<=b2)
print(a1==b2)



    
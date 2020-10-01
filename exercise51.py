import math
class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def root(self):
        value = math.sqrt((self.b**2) - 4*self.a*self.c)
        answer = -(self.b)+value
        finalanswer = answer/(2*self.a)
        print(finalanswer)
quadratic1 = Quadratic(1,-4, 4) #pass in your a b and c values mine are 1 -4 and 4 respectively
quadratic1.root()
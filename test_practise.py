# Encapsulation

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self,a):
        print(f"{self.brand} {self.model} started")
        print(a)
        
    def start2(self):
        #print(a)
        print(self.brand)
    
    
# Encapsulation
my_car = Car("Toyota", "Corolla")
my_car.start("assd")  # Output: Toyota Corolla started

class Table:
    def __init__(self,n):
        self.n=n
    def mult(self):
        for i in range(1,11):
            print(i*self.n)
T=Table(5)
T.mult()


class Factorial:
    def __init__(self,n):
        self.n=n
        self.p=0
        
    def fact(self):
        p=1
        for i in range(self.n,0,-1):
            p=p*i
        self.p=p
        #print(self.p)

    
    def fact2(self):
        print(self.p**2)

f=Factorial(5)
f.fact()
f.fact2()
class Fraction: #Initializing the class name
    def __init__(self,x,y): #Initializing the constructor
        self.x = x
        self.y = y
    
    def __str__(self): #This method represents the object when anything is printed or converted into string.
        return f"{self.x}/{self.y}"

    def __add__(self,other): #This method represents the object when anything is added.
        num = self.x * other.y + self.y* other.x
        den = self.y * other.y
        return f"{num}/{den}"

    def __sub__(self,other): #This method represents the object when anything is subtracted
        num = self.x * other.y - self.y* other.x
        den = self.y * other.y
        return f"{num}/{den}"

    def __mul__(self,other): #This method represents the object when anything is multiplied
        num = self.x * other.y
        den = self.y * other.y
        return f"{num}/{den}"
    
    def __truediv__(self,other): #This method represents the object when anything is divided.
        num = self.x * other.y
        den = self.y * other.x
        return f"{num}/{den}"

f1 = Fraction(1,2) #First object is created of Fraction class.
f2 = Fraction(2,4) #Second object is created of Fraction class.
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)

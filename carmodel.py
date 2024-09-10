#Step 1: Understanding Magic Methods
#Magic methods are a special piece of Python programming. They are specific to Object Oriented 
# Programming in Python, meaning that they can only be implemented in, and will only work in, classes.
#They allow actions to be performed on class instance objects that are otherwise impossible, such as printing
#  and comparing.Magic methods will always take the __<>__() form. For example, in the following code snippet
# the __str__() magic method is defined for the Car class.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model =model

    def __str__(self):
        return f"make: {self.make}, model: {self.model}"
myCar = Car("Hyundai","Sonata")
print (myCar) #make: Hyundai, model: Sonata


#Magic Methods Example
#Source: Python Docs

#There are many magic methods that can be implemented for any class we write. Some of them, such as those
#  shown here, are implemented by default. However, they can also be overwritten, such as in our example of
#  the __str__() function in the Car class, shown above. Remember, overwriting a function means that the function
#  may already exist, but we write over what is there by re-defining the function.
#Whenever we create a new class, Python creates a __str__() function for us by default. The default 
# implementation is often not very useful, since it only prints out the address in memory of our object. 
# By overwriting the __str__() function, we make our class more usable.
#Magic methods help our classes to be more useful. They enable us to use some common functions, 
# such as print() and len() . They also allow us to perform comparisons, such as <, >, <=, >=, and == .
#To use these operators, the following shorthand guide may be useful:


#Magic Method	Operator    
# __add__(self,other) # +
#__sub__(self,other) # -
#__mul__(self,other) # *
#__truediv__(self,other) # /

#__lt__(self,other) # <
#__gt__(self,other) # >
#__le__(self,other) # <=
#__ge__(self,other) # >=
#__eq__(self,other) # ==
#__ne__(self,other) # !=

class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"make: {self.make}, model: {self.model}"
    
    def __repr__(self):
        return f"Car('{self.make}', '{self.model}')"

    def __eq__(self,other): # ==
        if self.make == other.make and self.model == other.model:
            return True
        else:
            return False

    def __ne__(self,other): # !=
        if self == other:
            return False
        else:
            return True

car1 = Car("Hyundai","Sonata")
car2 = Car("Hyundai","Sonata")
car3 = Car("Honda","Accord")
print(car1 == car2) #True (self is car1, other is car2)
print(car1 == car3) #False (self is car1, other is car3)
print(car2 != car3) #True (self is car2, other is car3)


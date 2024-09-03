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
    myCar = Car("Toyota", "Corolla")
    print (myCar)



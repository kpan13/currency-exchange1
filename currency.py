#Step 2: Creating a Currency Exchange Emulator
#To better understand magic methods and how they are used, we will be creating a Currency Exchange Emulator.
#We will be using the following Replit for this part of class: https://replit.com/@SD-Team/Python-1044#main.py
#If you try to run the Replit before making any changes, you will get an error. This is intentional - the test 
# code at the bottom of the Replit is using operators that will only be defined for the class after you have 
# implemented them. To get started, simply fork the Replit to your own account!

class Currency: 
    currencies = {'CHF': 0.930023,  # Swiss Franc
                  'CAD': 1.264553,  # Canadian Dollar
                  'GBP': 0.737414,  # British Pound
                  'EUR': 0.820282,  # Euro
                  'USD': 1.0}  # US Dollar 
    
    def __init__(self, Value, unit="USD"):
        self.value = Value
        self.unit = unit

    def __str__(self):
        return f"{round(self.value, 2)} {self.unit}"
   
    def __repr__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def changeTo(self, new_unit):
        """
        Transforms Currency object from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Currency.currencies[self.unit]) * Currency.currencies[new_unit]
        self.unit = new_unit

    # Add magic methods here
    def __add__(self, other):
        """
        Defines the '+' operator. 
        If other is a Currency object, the currency values are added and the result 
        will be in the unit of self. If other is an int or a float, other will be 
        treated as a USD value.
        """
        if isinstance(other, (int, float)):
            x = other * Currency.currencies[self.unit]
        else:
            x = (other.value / Currency.currencies[other.unit]) * Currency.currencies[self.unit]
        return Currency(self.value + x, self.unit)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            x = other * Currency.currencies[self.unit]
        else:
            x = (other.value / Currency.currencies[other.unit]) * Currency.currencies[self.unit]
        self.value += x
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            x = other * Currency.currencies[self.unit]
        else:
            x = (other.value / Currency.currencies[other.unit]) * Currency.currencies[self.unit]
        return Currency(self.value - x, self.unit)

    def __isub__(self, other):
        if isinstance(other, (int, float)):
            x = other * Currency.currencies[self.unit]
        else:
            x = (other.value / Currency.currencies[other.unit]) * Currency.currencies[self.unit]
        self.value -= x
        return self

    def __rsub__(self, other):
        return Currency(other - self.value, "USD")

# Example usage
v1 = Currency(100, "USD")
v2 = Currency(100, "EUR")
print(v1 + v2)   # 182.93 USD
print(v2 + v1)   # 182.93 EUR
print(v1 + 3)    # An int or a float is treated as USD
print(3 + v1)    # An int or a float is treated as USD
print(30 - v2)   # 30 minus EUR value

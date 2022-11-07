# Normal Import
import calculator
print(type(calculator))
print(calculator.add(2,4))
print(calculator.multiply(2,4))
print(calculator.subtract(2,4))
print(calculator.divide(2,4))
print(calculator.CONSTANCT)
print()

# Filtered Import
from calculator import add,subtract
print(add(4,6))
print(subtract(5,2))
print()

# Universal Import
from calculator import *
print(divide(4,2))
# print(globals())
print()

# Making importing a lot of methods look better
from calculator import (add,
                        subtract,
                        multiply,
                        divide)
print(divide(5,2))
print()

# Aliasis
import calculator as cal
def calculator(a,b):
    return a
print(calculator(2,3))
print(cal.add(2,3))

from calculator import (
    add as addition,
    subtract as subtraction)
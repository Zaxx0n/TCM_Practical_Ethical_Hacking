#!/bin/python3
#
from TCM_Practical_Ethical_Hacking.introductiontopython.Employees import Employees

e1 = Employees("Bob", "Sales", "Director of Sales", 100000, 20)
e2 = Employees("Linda", "Executive", "CIO", 150000, 10)

print(e1.name)
print(e2.role)
print(e1.eligible_for_retirement())

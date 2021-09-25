import random

Salary = {'Director': 120800.0,
          'Secretary': 101150.25,
          'Locksmith': 188200.00}
print(Salary)

del Salary['Secretary']
print(Salary)


key = 'Secretary'
if key in Salary:
    del Salary['Secretary']
    print(Salary)


key2 = 5
if key2 in Salary:
    del Salary [key2]
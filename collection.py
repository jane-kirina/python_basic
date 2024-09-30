# https://www.geeksforgeeks.org/python-collections-module/

'''List of standard data struction in python:
    List (mutable)
    Tuple (immutable)
    Set (unique values)
    Dictionary (key-value)
'''
import operator

'''Convert two lists to dictionary'''
list1 = ["blue", "black", "tangerine", "brown"]
list2 = [23, 44, 51, 14]

print("Keys: " + str(list1))
print("Values: " + str(list2))

dict1 = {}

for key in list1:
    for value in list2:
        dict1[key] = value
        list2.remove(value)
        break

'''Join two Sets'''
set1 = {"Txt", "Data", "String"}
set2 = {12, 45, 21, 672}
set3 = {1, "set", 21, "Data"}
print(f'set1: {set1}')
print(f'set2: {set2}')
print(f'set3: {set3}')

print(set1.union(set2).union(set3))  # using union()
print(set1 | set2 | set3)  # using | operation

set4 = set1.copy()
set4.update(set2)
set4.update(set3)
print(set4)  # using update()

from functools import reduce

print(reduce(operator.or_, [set1, set2, set3]))  # using reduce()



class Test:
    planet = 'Earth'
    _real_planet = 'Neptune'

    def __init__(self, name, text):
        self._name = name
        self._text = text

    def print_stuff(self):
        print(f'name - {self._name}:\n{self._text}')

    def __str__(self):
        return f'{self.planet}, {self._real_planet}, {self._name}, {self._text}'


test_sample = Test('testName', 'simple and plain text')
test_sample.print_stuff()
print(test_sample.planet)

print(test_sample._real_planet)


class TypeTest(Test):
    def print_stuff(self):
        print(f'name - {self._name}:\n{self._text}\nplanet -> {self.planet}')


type_test_sample = TypeTest('naaame', 'textttttt')
type_test_sample.print_stuff()

print(type_test_sample)

# --- Built-in Functions ---

# abs() - absolute value of a number
abs(1)
abs(-1)

# round() - rounding to the correct sign
round(3.12874726, 0)
round(3.12874726, 2)
round(3.12874726, 5)

# all() - True if all elements of the list/set True
all([True, True, True, True, ])
all([1, 0, 1, ])
all([1, '0', 1, ])

# any() - True if at least one list element True
any([True, False, True, True, ])
any([1, 0, None, ])

# hash() - hash value for the object
data = [1, 100, 50, 12, 42]
hash('StringString')
hash(data)

# isinstance() - whether an object is an object of a given class
isinstance(data, list)

# Ternary Operator
# condition_if_true if condition else condition_if_else
bool1 = 'true' if True else 'false'
bool2 = 'true' if False else 'false'

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
date_of_week = now.weekday()
print(date_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)

print(date_of_birth)

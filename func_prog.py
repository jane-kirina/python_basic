# map, filter, zip and reduce

# MAP
# no map
def multiply_by2(list_of_num):
    new_list = []
    for item in list_of_num:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))


# with map
# map iterates over the object and gives values from object to input function
def multiply_by2_map(item):
    return item * 2


list_of_num = [1, 2, 3, 4, 5]

print(list(map(multiply_by2_map, list_of_num)))
print(list_of_num)


# FILTER
#  selects elements from an iterable based on the output of a function

def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, list_of_num)))

# ZIP
# aggregates iterables in a tuple, and returns it.
list_1 = [1, 2, 3]
list_2 = [10, 20, 30]
list_3 = [100, 200, 300]

print(list(zip(list_1, list_2, list_3)))

print(list_1)
print(list_2)

# REDUCE
# used to apply a particular function passed in its argument to all the list elements
from functools import reduce


def accumulator(acc, item):
    # print(acc, item)
    return acc + item


print(reduce(accumulator, list_1, 0))

print(list_1)

# LAMBDA
# lambda param: action, param

print(list(map(lambda item: item * 2, list_of_num)))
print(list(filter(lambda item: item % 2 == 0, list_of_num)))
print(reduce(lambda acc, item: acc + item, list_of_num))


# EXERCISES

# Square
list_a = [5, 4, 3]
print(list(map(lambda item: item ** 2, list_a)))

# List Sorting
list_b = [(0, 2), (4, 3), (10, -1), (9, 9)]

list_b.sort()
print(list_b)  # sorting based on 1 item

list_c = [(0, 2), (4, 3), (9, 9), (10, -1)]

list_c.sort(key=lambda x: x[1])  # sorting based on 2 item
print(list_c)



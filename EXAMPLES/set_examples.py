# x = {}   dict
# y = {'a': 5, 'm': 10} dict
# z = set()  set
# w = {'a', 'b', 'c'}  set
# t = ()   tuple
# m = 5,  tuple with one element
# n = 5, 6, 7   tuple
# j = []   list
# k = [1, 2, 3]  list
# r = [x.upper() for x in my_stuff]  list comprehension
# s = (x.upper() for x in my_stuff)  generator expression

set1 = {'red', 'blue', 'green', 'purple', 'green'}  # create literal set
set2 = {'green', 'blue', 'yellow', 'orange'}

set1.add('taupe')  # add element to set (ignored if already in set)

print(f"{set1 = }")
print(f"{set2 = }")
print(f"{set1 & set2 = }")  # intersection -- common items
print(f"{set1 ^ set2 = }")  # XOR -- non-common items (in one set but not both)
print(f"{set1 | set2 = }")  # union -- unique combination of both sets
print(f"{set1 - set2 = }")  # difference -- Remove items in right set from left set
print(f"{set2 - set1 = }")
print()

with open('../DATA/breakfast.txt') as breakfast_in:
    food = breakfast_in.read().splitlines()

unique_food = set(food)  # Create set from iterable (e.g., list)
print(sorted(unique_food, key=str.lower))

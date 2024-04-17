
# sum the squares of a list of numbers
# using list comprehension, entire list is stored in memory
s1 = sum([x * x for x in range(1000000)])

# only one square is in memory at a time with generator expression
squares_gen = (x * x for x in range(1000000))
s2 = sum(squares_gen) 
print(s1, s2)
print()

# generator function -- returns a generator (iterator)
def get_squares(iterable):
    for i in iterable:
        yield i * i

s3 = sum(get_squares(range(1000000)))
print(s3)

g = get_squares([1,2,3,4])
print(f"{g = }")
for value in g:
    print(value)


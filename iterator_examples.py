
colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

sorted_colors = sorted(colors)
print(f"{sorted_colors = }")

rcolors = reversed(colors)
print(f"{rcolors = }")
for color in rcolors:
    print(color)

for i, color in enumerate(colors):
    print(i, color)
print()

e = enumerate(colors)
for i, color in e:
    print(i, color)
print()
print("Second round:")
for i, color in e:
    print(i, color)
print()

for i, color in enumerate(colors, 1):
    print(i, color)
print()

values = [5, 2, 9]
cities = ['Denver', 'Santa Fe', 'Salem']

combined = zip(values, cities)
print(f"{combined = }")
for value, city in combined:
    print(value, city)
print()

print(list(zip(values, cities, colors)))
print()

for _ in range(10):
    print("Are we having fun yet?")
print()

# range(stop-before)   range(start-at, stop-before)  range(start-at, stop-before, count-by)

for i in range(1, 31, 2):
    print(f"{i}", end=" ")
print()
print()


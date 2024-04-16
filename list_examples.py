list1 = list()  # empty list
list2 = [1, 2, 3]  # literal list assigned to variable
list3 = []   # empty

cities = list()
cities.append("Cincinnati")
cities.append("Durham")
cities.append("Albany")
print(f"{cities = }")
cities.insert(0, "Boston")
cities.insert(3, "Atlanta")
print(f"{cities = }")
cities[4] = "Elmira"
print(f"{cities = }")
# cities[19] = "Pittsburgh"  INVALID
more_cities = ['Cleveland', 'Columbus', 'Dayton']
cities.extend(more_cities)
print(f"{cities = }")

#  LIST.append(obj)   LIST.insert(pos, obj)   LIST.extend(iterable)

del cities[2]   # del obj    del obj[index]
print(f"{cities = }")

cities.remove('Elmira')
print(f"{cities = }")

city = cities.pop()   # remove and return last item
print(f"{city = }")
print(f"{cities = }")

city = cities.pop(2)
print(f"{city = }")
print(f"{cities = }")

x = [1, 2, 3] + ['a', 'b', 'c']
print(f"{x = }")

cities.append("Miami")
cities.append("Burlington")
cities.append("Nashville")
cities.append("Detroit")
cities.insert(2, "Topeka")
cities.insert(5, "Sioux Falls")
print(f"{cities = }")

print(f"{cities[:5] = }")
print(f"{cities[0:5] = }")
#   SLICE[start:sentinel]
pos = cities.index('Columbus')
print(f"{cities[pos:pos+3] = }")

artist = "Taylor Swift"
print(f"{artist[7:12] = }")
print(f"{artist[7:] = }")
print(f"{artist[:6] = }")

#  CONTAINER[start-at:stop-before:count-by]
print()
for city in cities:
    print(city)
print()

# for VAR in ITERABLE:
#     code...

for letter in artist:
    print(letter.upper())

print(f"{'Topeka' in cities = }")
print(f"{'Durham' in cities = }")


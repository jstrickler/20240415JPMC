low_value = 12.39029303
artist = "Taylor Swift"
city = "Los Angeles"

print(low_value, artist, city)
#  str(low_value) + " " + str(artist) + " " + str(city) + "\n"

print(low_value, artist, city, sep="")
print(low_value, artist, city, sep="/")
print(low_value, artist, city, sep=", ")

print(low_value, end=" ")
# conditional code...
print(artist, city)

print(artist, ":", city)

# f-string  (formatted string)
print(f"{artist}: {city}")
print(f"2 + 2 is {2 + 2}")
print(f"{artist} lives in {city}")

# legacy
print("{}: {}".format(artist, city))

print(f"Value is {low_value}")
print(f"Value is {low_value:.1f}")

x = 33
print(f"x is {x:04d}")

print(f"{x = }")
print(f"{2 + 2 = }")

# old legacy
print("%s: %s" % (artist, city))






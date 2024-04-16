fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"{f0 = }\n")

f1 = [f.upper() for f in fruits]
print(f"{f1 = }\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"{f2 = }\n")

f3 = [f for f in fruits if f.startswith('a')]
print(f"{f3 = }\n")

words = ['    spam', 'ham     ', '    toast', 'Waffles']

new_words = [w.strip().upper() for w in words]
print(f"{new_words = }\n")

suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

deck = [(r,s) for s in suits for r in ranks]
print(f"{deck = }\n")


fruit_gen = (f.upper() for f in fruits)
print(f"{fruit_gen = }")
for fruit in fruit_gen:  # fruit_gen is a generator (a type of iterator)
    print(fruit)





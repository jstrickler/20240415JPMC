import os
from pprint import pprint

FOLDER = "../DATA"

file_names = 'alice.txt', 'parrot.txt', 'words.txt'
# [value for var in iterable] list comprehension
# {key:value for var in iterable}  dict comprehension
# {value for var in iterable}   set comprehension
file_info = {name: os.path.getsize(os.path.join(FOLDER, name)) for name in file_names}

pprint(file_info)

print('-' * 60)

capitals = {'NY': 'ALBANY', 'NC': 'RALEIGH', 'CA': 'SACRAMENTO', 'VT': 'MONTPELIER'}

caps = {state: capital.title() for state, capital in capitals.items()}
print(caps)

states = {capital:state for state, capital in capitals.items()}
print(states)

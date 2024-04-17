from pprint import pprint

knight_info = {}  # create empty dict

with open("../DATA/knights.txt") as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[name] = (title, color, quest, comment)  # create new dict element with name as key and a tuple of the other fields as the value

pprint(knight_info)
print()

#  for key, value in DICT.items(): ...
for name, info in knight_info.items():
    title_width = 5
    name_width = 10
    print(f"{info[0]:{title_width}} \033[1m{name:{name_width}}\033[0m \033[3m{info[1]}\033[0m")
print()
print(knight_info['Robin'][2])

d1 = dict()  # empty dict
print(f"{d1 = }")
print(f"{type(d1) = }")
d2 = {'NC': 'Raleigh', 'OH': 'Columbus', 'CA': 'Sacramento'}
print(f"{d2 = }")
d3 = {}  # empty dict

d2['MA'] = 'Boston'
d2['VA'] = 'Richmond'
print(f"{d2 = }")
d2['VA'] = 'Roanoke'
print(f"{d2 = }")

del d2['VA']
print(f"{d2 = }")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['SJC'] = }")
# print(f"{airports['COL'] = }")
print(f"{'CVG' in airports = }")
print(f"{airports.get('CVG') = }")
print(f"{airports.get('SJC') = }")
print(f"{airports.get('CVG', 'bummer -- not found') = }")

print(f"{airports.setdefault('CVG', 'Cincinatti') = }")
print(f"{airports = }")

for code, city in airports.items():
    if city.startswith('C'):
        print(code, city)

print(f"{airports.keys() = }")
print(f"{airports.values() = }")







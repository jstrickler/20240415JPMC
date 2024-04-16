s1 = "spam\n"   # all 4 are the same
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print("Guido's the ex-BDFL of Python")
print()
print('Guido is the ex-"BDFL" of Python')
print()
print("""Guido's the ex-"BDFL" of Python""")

query = """
select *
from customers
where company_name = "Spam Industries"
order by date
"""

print(r"s\bpa\fm\n")

print("It's 80\u00B0 outside")

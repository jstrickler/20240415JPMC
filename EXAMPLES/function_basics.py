

def say_hello():  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )


def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()


def sqrt(num):  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)
x = 5
p = sqrt(x)

print(f"m is {m:.3f} n is {n:.3f} p is {p:.3f}")

# def FUNCTION(param, param, ....):
#     # code ...
#     return SOME_VALUE

# type hints!
def blob(x, y):
    print(x, y)

blob(1, 2)
blob('spam', 'ham')
blob((4,5), [8, 1, 17])

# def blob(a, b, c):
#     print(a, b, c)

# blob('a', 'm', 'z')

#  5 types of function parameters
#  required positional name not allowed
#  required positional (name OK)   ************
#  optional positional 
#  required named
#  optional named

#  Element('last_name', manager=True, salaried=False)
#  find_text("banana", "foo.txt", "bar.txt", "blah.txt", ignore_case=False)

def find_text(search_term, *file_paths, ignore_case=True):
    pass






value = 12

if value > 75:  # {
    print("wombat")
    print("wallaby")
# }
elif value > 50:  #  else if
    print("kangaroo")
    print("kookaburra")
elif value > 25:
    print("cane toad")
else:
    print("platypus")

print("All done!")

x = 0
if x:
    print("it is TRUE")
else:
    print("it is FALSE")

# for numbers:
#   0 is False 
#  non-0 is True

# for containers (list, tuple, str, bytes, set, dict, etc...)
# len(c) == 0  is False
# len(c) > 0  is True
    
# None is also False

# True False
print(f"{int(True) = }")
print(f"{int(False) = }")

#   A ? B : C
#  B if A else C

DEBUG = True
print("PROBLEM" if DEBUG else "ALL IS WELL")

if DEBUG:
    print("PROBLEM")
else:
    print("ALL IS WELL")

#  == != > < >= <=
#  is

#  not and or







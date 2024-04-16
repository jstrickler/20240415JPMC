i = 0
while i < 3:
    print(i)
    i += 1

print("Done")

counter = 1
while True:
    print(f"whoo-hooo {counter}")
    user_input = input("Enter q to quit, <ENTER> to continue ")
    counter += 1
    if user_input == 'q':
        break  #  EXIT LOOP


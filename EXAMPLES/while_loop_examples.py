
print("Welcome to ticket sales\n")

while True:  # Loop "forever"
    raw_quantity = input("Enter quantity to purchase (or q to quit): ")
    if raw_quantity == '':
        continue  # Skip rest of loop; start back at top
    if raw_quantity.lower() == 'q':
        print("goodbye!")
        break  # Exit loop

    quantity = int(raw_quantity)  # could validate via try/except
    if quantity > 16:
        print("Sorry, max 16 at one time")
    elif quantity > 0 and quantity % 2 != 0:
        print("Purchase must be a multiple of 2")
    else:
        print(f"sending {quantity} ticket(s)")

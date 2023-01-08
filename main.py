values = []

while True:
    data = input("Enter a list of numbers and in the end press enter to finish: ")
    if data:
        values += [int(x) for x in data.split()]  # '+=' adding values to the 'values' list
    else:
        print("The list is:", values)
        break

biggest = None  # initializing values as None(empty to
smallest = None

for x in values:
    if biggest is None or x > biggest:
        biggest = x
    if smallest is None or x < smallest:
        smallest = x

print("The biggest value is:", biggest, "\nthe smallest value is: ", smallest)

values = []

while True:
    data = input("Enter a list of numbers and in the end press enter to finish: ")
    if data:
        values += [int(x) for x in data.split()]  # '+=' adding values to the 'values' list
    else:
        print("The list is:", values)
        break

biggest = min(values)  # initializing values as None(empty to
smallest = max(values)

print("The biggest value is:", biggest, "\nthe smallest value is: ", smallest)

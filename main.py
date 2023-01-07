values = []

while True:
    data = input("Enter a list of integers, separated by spaces: ")
    if data:
        values += [int(x) for x in data.split()]
    else:
        print(values)
        break

# print(The Smallest integer: 1 (index 5) Largest integer: 10 (index 0))
# count = 0
# for element in my_list:
# count += 1
# The list.append() method is used to add an item to the end of a list.


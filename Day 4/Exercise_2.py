# Give random name. If name is coming he/she will pay the bill.

import random
test_seed = int(input("Enter a random seed number: "))
print(test_seed)

# Split String Method:
nameAsCSV = input("Give me everybody's name, split with comma: ")
name_split = nameAsCSV.split(", ")
names = len(name_split)
pay = random.randint(0, names - 1)
person = name_split[pay]
print(person + " " + "is going to buy a meal")



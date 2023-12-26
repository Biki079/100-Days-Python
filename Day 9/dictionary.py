programming_dictionary = {
    "Bug" : "An error in a program that prevents program from running as expected.",
    "Function": "A piece of code that you can call over an over again."
}

#Retreving information from dictionary
#print (programming_dictionary["Bug"])

# Add items in dictionary:
programming_dictionary ["loop"] = "The action of doing something over and over again."
#print(programming_dictionary)

#Create empty dictionary:
empty_dictionary = {}

# Wiped an existing dictionary:
#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in dictionary:
programming_dictionary["Bug"] = "A moth in your computer. "
#print(programming_dictionary)

#loop through in dictionary:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

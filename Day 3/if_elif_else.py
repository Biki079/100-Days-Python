print ("Welcome to the rollercoaster.")
height = int(input("Enter your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int (input("What is your Age? "))
    if age <= 8:
        print("You can pay Rs 100")
    elif age <= 12:
        print("You can pay Rs 150")
    else:
        print("You can pay Rs 250")
else:
    print("Sorry, you have to grow taller before you ride")
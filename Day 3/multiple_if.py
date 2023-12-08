print ("Welcome to the rollercoaster.")
height = int(input("Enter your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride")
    age = int (input("What is your Age? "))
    if age <= 8:
        bill = 100
        print("Child pay Rs 100")
    elif age <= 12:
        bill = 150
        print("Adults pay Rs 150")
    else:
        bill = 250
        print("Youths pay Rs 250")
    click_photo = input("Do you want Photo taken. Y and N ")
    if click_photo == "Y":
     bill += 50
     print(f"Your final bill is.{bill}")
    else:
        print(f"Your finall bill without taken photo is. {bill}")
else:
    print("Sorry, you have to grow taller before you ride")
print("Welcome to funpark.")
height = int (input ("Enter your height in cm? "))

if height >=100:
    print("You can enter in funpark.")
    age = int (input("What is your age?"))
    if age >= 10:
      print("You can pay RS 250")
    else:
       print("You can pay RS 150")
else:
   print("Sorry, You can grow taller before go to funpark.")
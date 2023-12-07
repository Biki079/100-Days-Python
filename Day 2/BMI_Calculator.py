
height = input("Enter your Height? ")
weight = input("Enter your Weight? ")
BMI = int(weight) / float(height) ** 2
bmi_as_int = int (BMI)
print (round (bmi_as_int , 2))
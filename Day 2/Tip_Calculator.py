print ("Welcome to the tip calculator")
total_bill = input ("What was the total bill? ")
total_bill_as_int = int (total_bill)
per = input ("What percentage tip would you like to give? 10, 12, 15 ")
per_as_int = int(per)
people = input ("How many people to split the bill? ")
people_as_int = int(people)
pay = total_bill_as_int * per_as_int / people_as_int
print (f"Each person should pay {pay}")

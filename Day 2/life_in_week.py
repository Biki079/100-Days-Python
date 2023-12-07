age = input("Enter your current age? ")
age_as_int = int(age)
years_remaining = 70 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print (f"Your current age is {age_as_int}, your remaining years is {years_remaining}, your remaining month is {months_remaining} your weeks remaining is {weeks_remaining}, your days remaining is {days_remaining}")

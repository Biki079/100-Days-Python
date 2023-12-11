student_height = input("Input the list of student heights ").split()

# Convert each height in the list to an integer
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

print(student_height)

# Calculate the total height
total_height = 0
for height in student_height:
    total_height += height

print("Total height:", total_height)

number_of_students = 0
for student in student_height:
    number_of_students += 1
print("Number of student is", number_of_students)

average_height = round(total_height / number_of_students)
print("Average height is", average_height)



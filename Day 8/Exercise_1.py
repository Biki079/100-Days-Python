# To calculate area of wall and find how many Can are used to paint the wall.
import math
def paint_cal(height, width, cover):
 area =( height * width)
 num_of_cans = math.ceil(area / cover)
 print(f"You'll need {num_of_cans} cans to paint.")
test_height = int(input("Enter height: "))
test_width = int(input("Enter width: "))
coverage = 5
paint_cal(height=test_height, width=test_width, cover=coverage)

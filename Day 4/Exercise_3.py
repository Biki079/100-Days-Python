# Treasure Map Game

row1 = ["🤚  ", "🤣 ", "🤣 "]
row2 = ["🤚  ", "🤣 ", "🤣 "]
row3 = ["🤚  ", "🤣 ", "🤣 "]
map = [row1, row2, row3]
print(f"{row1}\n, {row2}\n, {row3} ")
postion = input("Where do you want to put the treasure? ")

horizontal = int(postion[0])
vertical = int(postion[1])
selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"
print(f"{row1}\n, {row2}\n, {row3}")





# A program that marks a spot with x
# First digit is column then the second one is row

# the 3 rows
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\n ")

# The vertical position(column):
vertical = int(position[0])

# The horizontal position(row):
horizontal = int(position[1])

# index of the row
selected_row = map[horizontal - 1]

# The column will be calculated basing on the row, since the row is now known, it will help us with getting the column
selected_row[vertical - 1] = "X"

# Printing
print(f"{row1}\n{row2}\n{row3}")
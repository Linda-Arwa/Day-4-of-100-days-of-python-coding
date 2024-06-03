# A program which selects a random name from a list of names. The person selected will have to pay for everyone's food bill.

# Solution

import random

names = input("Kindly add everyone's name here. Use commas in between each name for separation purposes.\n")

# Using the split() to split the string
names_list = names.split(", ")
print(names_list)

# Getting the number of people in the list
people = len(names_list)
print(people)

# Getting the index of the person paying the bill
# The fact that we are using randint(), it only caters for numbers hence it will give us the random number which in this case is the index to our list 
bill_payer_index = random.randint(0, people - 1)
print(f"The person paying the bill is at index {bill_payer_index}")

# The name of the person paying for the bill
bill_payer = names_list[bill_payer_index]
print(f"Bingoo!!!{bill_payer} is paying the entire bill")
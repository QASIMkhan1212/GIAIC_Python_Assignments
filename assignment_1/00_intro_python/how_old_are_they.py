# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

names = ["Anton", "Beth", "Chen", "Drew", "Ethan"]
ages = [21, 6 , 20 , 41 , 20]

for i in range(5):
    print(f"{names[i]} is {ages[i]}.")
    
# print(f"{names[0]} is {ages[0]} years old.")
# print(f"{names[1]} is {ages[1]} years old.")
# print(f"{names[2]} is {ages[2]} years old.")
# print(f"{names[3]} is {ages[3]} years old.")
# print(f"{names[4]} is {ages[4]} years old.")
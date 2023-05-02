#Lesson 34
#Objective: pizza order
#Author: Archibald Macharia
#Date: 19/4/2023

print("Welcome to Python pizza Deliveries!")
size = input("What size pizza do you want, S, M, L? ")
add_toppings = input("Do you want any toppings, Y or N? ")
extra_cheese = input("Do you want extra cheese, Y or N? ")

bill = 0

if size == "S":
	bill += 15
elif size == "M":
	bill += 20
else:
	bill +=25

if add_toppings == "Y":
	if size == "S":
		bill += 2
	else:
		bill += 3
elif add_toppings == "N":
    bill += 0
if extra_cheese == "Y":
	bill += 1

print(f"Total bill is ${bill}")

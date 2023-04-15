#Author: Archibald Macharia
#Objective: create a tip calculator that asks what percentage to tip
#Date: 4/4/2023

#let's ouptut the greetings
print("Welcome to the tip calculator! \n")

#lets create a variable called total bills
total_bill = float(input("What was the total bill? $"))

#Create the percentage tip that the client would like to give
tip = float(input("What percentage tip would you like to give? 10, 15, 20? "))

print(tip)

#tip variable
tip_percentage = float((tip / 100))

print(tip_percentage)

bill_tip = (total_bill * tip_percentage)


#This is to output the total bill tip
print(bill_tip)

total_bill_tip = 150 + bill_tip
print(total_bill_tip)

#Create a split variable that gives the option to split the total bill
number_of_people_to_split = int(input("How many people to split the bill? "))

#let's create split variable
#split = total_bill_tip / number_of_people_to_split


#let's create total payment that one person or each person would pay
total_Payment = total_bill_tip / number_of_people_to_split

#let's output the total payment
print(round(total_Payment,2))


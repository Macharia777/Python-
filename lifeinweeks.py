#Author: Archibald Macharia
#Objective: calculate time left in a certain number of years
#

#create a variable of the current age
age = int(input("What is your current age: "))

#create a variable for expected age
expected_age = int(input("expected age in: "))

#calculate the difference of the number of years between your age and the expected age
calculated_years = expected_age - age

#create the variables for the days, months and years
#create for months
months = calculated_years * 12

#create for weeks
weeks = calculated_years * 52

#create for days
days = calculated_years * 365

#output the calculated number of years
print(calculated_years)

#Output the time left
timeLeft = print(f"You have {days} days, {weeks} weeks, and {months} months eleft")

print(months)

#Author: Archibald Macharia
#Objective: create a BMI calculator where the user can input user info
#Date: 3/4/2023

# create  a variable that shows height and weight
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

#create the BMI formulae

BMI = int(weight) / int(height * height)

# output the BMI
print(int(BMI))

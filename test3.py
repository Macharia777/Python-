#Interchange the values in the different variables that you have prompted 
#Author: Macharia
#Date/Time: 24/3/2023

#let's create the variable namely a & b

a = input("a: ")
b = input("b: ")

# in order to switch we have to add another variable as a placeholder  

# now let's switch

temp = a
a = b
b = temp

#let's print

print("a = " + a)
print("b = " + b)


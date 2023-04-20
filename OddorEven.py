#Objecive - create a program to check whether a number is odd or even
#Author: Archibald Macharia
#Lang: Python
#Date: 15th April 2023

#Even numbers can be divided by 2 with no remainder

#lets create a variable that well end at 100
a = int(input("Is a an Even or Odd number? "))

#let's create an if statement that will print numbers from 0-100 and to chekif the is divisible by 2

if a % 2 == 0:
	print (f"{a} is even")
else:
	print(f"{a} is odd")


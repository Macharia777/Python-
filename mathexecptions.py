# Let's create a scenario where a user will input an int only and not a string
# while True:
# 	try:
# 		number = int(input("Please Enter a number: "))
# 		break;

# 	except ValueError:
# 		print("You did not enter a number")

# 	except:
# 		print("An unknown Error occured")
# print("Congratulations you have entered a number")

# import random

# while True:
#  try:
#      guess_random = int(input("Guess a number between 1 and 10: "))
#      Random_number = random.randint(1,10) + 1

#      if guess_random != Random_number:
#         print("Not right number")
#      elif guess_random == Random_number:
#          print("You have guessed right")
#          break
#      elif guess_random > Random_number:
#          print("Your number is above 1 - 10")

#  except ValueError:
#      print("You are only allowed to use numbers")

# print("Thank you for playing.")


# Another way to do the random challenge

# secret_number = 7

# while True:
#     guess = int(input("Guess a number between 1 and 10: "))

#     if guess == secret_number:
#         print("You guessed it")
#         break

import math

# Because you used import you can access methods by referencing the module
print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# Factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.factorial(4))

# return remainder or division
print("fmod(6,4) = ", math.fmod(6, 4))

# Receive a float and return and int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.pow(2, 2))

# Return the square root
print("sqrt(4) = ", math.sqrt(4))

# Special Values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# Return e^x
print("exp(4) = ", math.factorial(4))

# Return the natural logarithm e * e * e ~= 20 so log(20) tells
# you that e^3 ~= 20
print("log(1000,10) = ", math.log(1000, 10))

# You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

# we have the following trig functions
# sin cos tan asin, acos, atan, atanZ, asinh, acosh,
# atanh, sinh, cosh, tanh

# convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))

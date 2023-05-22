# num1 = 5
# num2 = 3

# # calc the sum
# sum = num1 + num2
# # calc multiplication
# product = num1 * num2
# # calc Division
# quotient = num1 / num2

# print("{} + {} = {}".format(num1, num2, sum))
# print("{} * {} = {}".format(num1, num2, product))
# print("{} / {} = {}".format(num1, num2, quotient))

# num1, operator, num2 = input("Enter calculations ").split()

# convert strings to integers
# num1 = int(num1)
# num2 = int(num2)

# if operator == "+":
#     print("{} + {} = {}".format(num1, num2, num1 + num2))
# else:
#     print("not working")

# age = eval(input("Enter age: "))

# if age is both greater than or equal to 1 or equal to 18 important
# if (age >= 1) and (age <= 18):
#     print("important")
# elif (age == 21) or (age == 50):
#     print("important")
# elif not (age < 65):
#     print("less")
# else:
#     print("Not important")

# ask for age
age = eval(input("Enter age: "))

# Handle if age < 5
if age < 5:
    print("Too young for school")

# Special output just for age 5
elif age == 5:
    print("Go to Kindergarten")

# since a number is the result for ages 6 - 17 we can check them all with 1 condition
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("go to {} grade".format(grade))
else:
    print("sijui utaenda wapi")

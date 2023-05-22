# for i in range(1, 9):
#     print("i = ", i)

# use for loop through the list from 1 to 21
# for i in range(1, 21):
#     # to check odd numbers
#     if (i % 2) != 0:
#         # print
#         print("i = ", i)

# have the user enter their investment amount and expected interest earned each year
# investment_amount = input("Enter your preferred investment amount: ")
# investment_amount = float(investment_amount)
# interest_rate = input("Enter expected interest earned each year: ")
# interest_rate = float(interest_rate) * 0.01

# # each year their investment will increase by their investment * interest rate
# for year in range(10):
#     investment_amount = investment_amount + (investment_amount * interest_rate)
# # print earning after a 10 year period
# print("Investment after 10 years : {:.2f}".format(investment_amount))

import random

rand_num = random.randrange(1, 51)

i = 1

while i != rand_num:
    i += rand_num

    print("The random value is: ", rand_num)

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

# import random

# rand_num = random.randrange(1, 51)

# i = 1

# using while loops

# while i != rand_num:
#     i += 1

# print("The random value is: ", rand_num)

# while in range of 1 to 20 and finding the odd number
# i = 1

# while i <= 20:
#     if (i % 2) != 0:
#         print("odds: ", i)
#     i += 1
#     # continue

# if i == 15:
#    break

# print("odd: ", i)
# i += 1

# create a christmas tree
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 space : 7 hashes
# 0 spaces : 9 hashes

# Need to do
# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save the spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash

# # Get the number of rows for the tree
# tree_height = input("How tall is the tree: ")
# # Convert into an integer
# tree_height = int(tree_height)
# # Get the starting spaces for the top of the tree
# spaces = tree_height - 1
# # There is one hash to start that will be incremented
# hashes = 1
# # Save stump spaces till later
# stump_spaces = tree_height - 1
# # Make sure the right number of rows are printed
# while tree_height != 0:
#     # Print the spaces
#     for i in range(spaces):
#         print(" ", end="")

#     # Print the hashes
#     for i in range(hashes):
#         print("#", end="")

#     # Newline after each row is printed
#     print()
#     # Spaces is decremented by 1 each time
#     spaces -= 1
#     # Hashes is incremented by 2 each time
#     hashes += 2
#     # Decrement tree height each time to jump out of the loop
#     tree_height -= 1
#     # Print the spaces before the stump and then the hash
#     for i in range(stump_spaces):
#         print(" ", end="")

#     print("#")

height = int(input("What is your height? "))

if height >= 120:
 print("You can ride")
 age = int(input("What is your age? "))
 if age < 12:
  print("You pay $5")
 elif age <= 18:
  print("You pay $7")
 else:
  print("You'll pay $12")
else:
 print("You can't ride the rollercoaster!!!")

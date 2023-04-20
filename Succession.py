#Lesson - day 33
#objective - add price to the rollercoster plus photo
#Author: Archibald Macharia
#Date: 18/4/2023

height = int(input("What is your height? "))

if height > 120:
 print("You can ride the roller coaster")
 age = int(input("What is your age? "))
 if age < 12:
  bill = int(5)
  print(f"You will pay $5")
 elif age > 12 and age < 18:
  bill = int(7) 
  print(f"You will pay $7")
 else:
   bill = int(12)
print(f"You will pay $12")

photo = (input("Do you want a photo, yes or no? "))
if photo == "yes":
  bill += 3
  print(f"Your total bill is{bill}")

else:
  print("error")
  	
  

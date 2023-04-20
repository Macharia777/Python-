leap_year = int(input("Which year do you want to check? "))
even_number = leap_year % 100 == 0

if leap_year / 4 == 0 and leap_year / 4 == 0: 
 print("This is a leap year")
elif leap_year % 100 == 0 and leap_year / 100 == 0:
 print("This is not a leap year")
elif leap_year % 400 == 0:
 print("This is a leap year")
else:
 print("This is not a leap year")

#Let's create a method that shows the number in a string 
#num_char = len(input("What is your name? "))
#print("your name has " + num_char + "characters.") #this will bring an error because num_char returns an integer not a sring

#so we'll have to convert the length function to a string
new_num_char = str(len(input("What is your name? ")))
print("Your name has " + new_num_char + " characters")

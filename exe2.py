#we can do this exe in two ways:
#first way
#a = input("a is: ")
#b = input("b is: ")

#print(a + b)
#print(int(a)+int(b))

two_digit_number = input("Type a two digit number: ")

#Get the first and second digits using subscripting then convert string to int
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

#add the two results
result = int(first_digit) + int(second_digit)

print(result)

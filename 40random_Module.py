#!/usr/bin/python3
import random
import my_module

#we use randint for random integers
random_Integer = random.randint(1,10)

print(random_Integer)

#We use random for floating numbers
random_float = random.random() * 5
print(random_float)

#let's create  a random love score
love_score = random.randint(1,100)
print(love_score)
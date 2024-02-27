import random

start = -1
stop = 11

top_of_range = input("Type a number: ")

#checks if input is a digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("PLease type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time")
    quit()

#generates a pseudorandom number from -1 to 11
#random_number = random.randrange(start, stop)
#for generating random numbers from 0-10 use
# print(random.randrange(stop)) where stop = 11
#randint includes upper range defined by stop variable

random_number = random.randint(0,top_of_range)
print(random_number)
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

#NOTES FOR MYSELF ABOUT random's methods
#generates a pseudorandom number from -1 to 11
#random_number = random.randrange(start, stop)
#for generating random numbers from 0-10 use
# print(random.randrange(stop)) where stop = 11
#randint includes upper range defined by stop variable

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("Your were below the number!")

print("You got it in", guesses, "guesses")
import random

print("Let's see if you can guess the random number..." )
guess = input("Guess a number 1 to 10? ")
comp = random.randrange(1, 11, 1)

if guess == comp:
  print("You guessed correctly!!")
else:
  print("Your guess was incorrect. The number was " + str(comp) +"!")


# the first program that I wrote completely on my own
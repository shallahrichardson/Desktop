import random
number = random.randrange(0,10)
guess = int(input("Pick a number between 0 and 10:"))
while guess != number:
  if guess < number:
    print("Pick a higher number.Try again")
    guess = int(input("Pick a number between 0 and 10:"))
  else:
    print("Pick a lower number.Try again")
    guess = int(input("Pick a number between 0 and 10:"))
print("You guessed correctly !!")
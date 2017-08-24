# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
  while True:
    print('Take a guess.')
    guess = int(input())
    if guess < 1 or guess > 20:
      print('Your guess must be between 1 and 20.')
    else:
      break

  if guess < secretNumber:
    print('Your guess is too low.')
  elif guess > secretNumber:
    print('Your guess is too high.')
  else:
    break # The correct guess!

if guess == secretNumber:
  print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
  print('Nope. The number I was thinking of was ' + str(secretNumber) + '!')

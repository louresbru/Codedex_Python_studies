guess = 0
tries = 0

while guess != 6:
  guess = int(input("Guess the number:  "))
  tries += 1
  if guess != 6 and tries == 3:
    print("No more guesses")
    break 
  if guess == 6 and tries <= 3:
    print('You got it!!!')

import random

keyCode = random.randint(1,100)
print(keyCode)
guessCount = 1

while True:
    guess = int(input("\nGuess the number (1 - 100): "))
    if guess > keyCode:
        print("Guess lower")
    elif guess < keyCode:
        print("Guess higher")
    elif guess == keyCode:
        break
    else:
        print("Enter number between 1-100")
    guessCount+=1

print(f"\nJackpot! The number was {keyCode}")
print(f"It took you {guessCount} attempt")
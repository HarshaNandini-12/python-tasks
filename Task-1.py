import random

words = ["apple", "python", "computer", "school", "program"]

word = random.choice(words)
guessed = []
attempts = 6

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)

    if "_" not in display:
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("You lost!")
    print("The word was:", word)
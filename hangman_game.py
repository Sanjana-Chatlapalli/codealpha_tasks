import random

words = ["apple", "banana", "grapes", "orange", "python"]
word = random.choice(words)

guessed_letters = []
tries = 6

print("Welcome to Hangman Game!")

while tries > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)

    if display_word == word:
        print(" You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong guess! Attempts left:", tries)

if tries == 0:
    print("Game Over! The correct word was:", word)
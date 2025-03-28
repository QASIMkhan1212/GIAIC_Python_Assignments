import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'developer', 'algorithm', 'computer']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed = ''
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + ' '
        else:
            displayed += '_ '
    return displayed.strip()

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6  
    guessed_word = False

    print("Welcome to Hangman!")
    
    while attempts > 0 and not guessed_word:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! You lost an attempt.")

        if all(letter in guessed_letters for letter in word):
            guessed_word = True

    if guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

hangman()


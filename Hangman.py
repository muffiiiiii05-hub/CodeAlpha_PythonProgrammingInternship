import random

WORDS = ["python", "hangman", "keyboard", "internship", "developer"]
MAX_WRONG_GUESSES = 6


def choose_word():
    return random.choice(WORDS)


def display_progress(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(display_progress(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.\n")

    print(f"Game over! You ran out of guesses. The word was: {word}")


if __name__ == "__main__":
    play_hangman()
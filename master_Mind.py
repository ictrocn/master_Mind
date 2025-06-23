import random
# !/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay & password-protected cheat
print("MasterMind")

print("MasterMind")

COLORS = ['R', 'G', 'B', 'Y', 'O', 'C', 'P']


def generate_code(length=4):
    return [str(random.choice(COLORS)) for _ in range(length)]


def get_feedback(secret, guess):
    feedback = [''] * 4
    secret_copy = secret[:]
    guess_copy = list(guess)

    for i in range(4):
        if guess[i] == secret[i]:
            feedback[i] = 'B'
            secret_copy[i] = None
            guess_copy[i] = None

    for i in range(4):
        if guess_copy[i] is not None:
            if guess_copy[i] in secret_copy:
                feedback[i] = 'W'
                secret_copy[secret_copy.index(guess_copy[i])] = None
            else:
                feedback[i] = 'N'

    return feedback


def show_secret(secret_code):
    print(f"The code is: {''.join(secret_code)}")


def play_mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-color code. Use letters: R, G, B, Y, O, C, P. You have 10 attempts.")
    secret_code = generate_code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_guess = False
        while not valid_guess:
            guess = input(f"Attempt {attempt}: ").upper()
            if guess == "CHEAT":
                show_secret(secret_code)
                continue
            valid_guess = len(guess) == 4 and all(c in COLORS for c in guess)
            if not valid_guess:
                print("Invalid input. Enter 4 letters from R, G, B, Y, O, C, P.")

        feedback = get_feedback(secret_code, guess)
        print("Feedback:", ''.join(feedback))

        if feedback == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_code)}")


if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_mastermind()
        again = input("Play again (Y/N) ?").upper()

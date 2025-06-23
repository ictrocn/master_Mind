#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay

import random

print("MasterMind")

kleuren = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']


def generate_Code(length=4):
    return [str(random.choice(kleuren)) for _ in range(length)]


def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))

    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)

    return black_Pegs, white_Pegs


def show_Secret(mystery):
    print(mystery)


def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-color code. the colors are rood, geel, groen, oranje, blauw en paars")
    secret_Code = generate_Code()
    attempts = 10

    admin_password = "admin123"
    admin = False
    password = input("Fill in the admin password or press enter to play:")
    if password == admin_password:
        admin = True
        print("admin mode activated use cheat to see the code.")
    else:
        print("normal mode activated, succces!")

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess_input = input(f"Attempt {attempt} (separate colors with spaces): ").strip().lower()
            if guess_input == "cheat" and admin:
                show_Secret(secret_Code)
                continue

            guess = guess_input.split()
            valid_Guess = len(guess) == 4 and all(c in kleuren for c in guess)
            if not valid_Guess:
                print("invalid guess. Enter 4 valid colors, seperated by spaces")

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")


if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Play again (Y/N) ?").upper()

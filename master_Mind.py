#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
# Last mod by DevJan : added loop for replay & password-protected cheat

import random

print("MasterMind")

COLORS = ['R', 'G', 'B', 'Y', 'O', 'C', 'P']

def generate_code(length=4, digits=6):
    return [str(random.choice(COLORS)) for _ in range(length)]


def get_feedback(secret, guess):
    black_pegs = sum(s == g for s, g in zip(secret, guess))
    
    # Count whites by subtracting black and calculating min digit frequency match
    secret_counts = {}
    guess_counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_counts[s] = secret_counts.get(s, 0) + 1
            guess_counts[g] = guess_counts.get(g, 0) + 1

    white_pegs = sum(min(secret_counts.get(c, 0), guess_counts.get(c, 0)) for c in guess_counts)
    
    return black_pegs, white_pegs


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

        black, white = get_feedback(secret_code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_mastermind()
        again  = input (f"Play again (Y/N) ?").upper()

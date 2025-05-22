#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
print("MasterMind")

import random


# def generate_Code(length=4, digits=6):
#     return [str(random.randint(1, digits)) for _ in range(length)]
colors = ["rood", "blauw", "groen", "paars", "geel", "oranje"]    
def generate_Code(length=4):
    return [random.choice(colors) for _ in range(length)]


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
    print("Guess the 4-color code. Colors: rood, blauw, groen, paars, geel, oranje.")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = []
        valid_Guess = False
        while not valid_Guess:
            guess_input = input(f"Attempt {attempt}: ").strip().lower().split()
            if guess_input == ["admin"]:
                print("welkom bij het adminscherm wil je code zien ja")
                ja = input("ja of nee")
                if ja == "ja":
                    print(f"Secret code: {secret_Code}")
                    continue
            valid_Guess = len(guess_input) == 4 and all(color in colors for color in guess_input)
            if not valid_Guess:
                print("Invalid input. Enter 4 valid colors separated by spaces.")

        guess = guess_input
        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {' '.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {' '.join(secret_Code)}")


if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()


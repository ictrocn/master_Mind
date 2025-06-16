#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay & password-protected cheat
print("MasterMind")

import random

def generate_Code(length=4, digits=6 ) :
    return [str(random.randint(1, digits)) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    secret_Counts={}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    return black_Pegs, white_Pegs

def show_Secret(secret_Code):
    print(f"[Cheat Mode] De geheime code is: {''.join(secret_Code)}")

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    secret_Code = generate_Code()
    attempts = 10
    CHEAT_PASSWORD = "maker123"

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ").strip()

            if guess.lower() == "cheat":
                pw = input("Voer het wachtwoord in om de code te tonen: ").strip()
                if pw == CHEAT_PASSWORD:
                    show_Secret(secret_Code)
                else:
                    print("Onjuist wachtwoord. Toegang geweigerd.")
                continue  # Geen poging telt voor cheat
            elif len(guess) == 4 and all(c in "123456" for c in guess):
                valid_Guess = True
            else:
                print("Invalid input. Enter 4 digits, each from 1 to 6.")

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
        again = input("Play again (Y/N)? ").strip().upper()


import random

def guess_number():
    lower_limit = 1
    upper_limit = 100
    attempts = 0

    print("Think of a number between 1 and 100 and type 'ok' when you're ready.")
    response = input()

    if response.lower() != 'ok':
        print("Sorry, I didn't understand your response. Please type 'ok' to begin.")
        return

    while True:
        guess = random.randint(lower_limit, upper_limit)
        print("I'm guessing the number:", guess)
        response = input("Is the number higher (>), lower (<), or equal (=) to the guess? ")

        if response == '=':
            print("Correct! The number is", guess)
            break
        elif response == '>':
            lower_limit = guess + 1
        elif response == '<':
            upper_limit = guess - 1
        else:
            print("Sorry, I didn't understand your response. Please use '>', '<', or '='.")

        attempts += 1

    print("Number of attempts:", attempts)

guess_number()
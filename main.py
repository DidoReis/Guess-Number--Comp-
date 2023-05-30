import random

def guess_number():
    lower_limit = 1     # Set the lower limit of the number range
    upper_limit = 100   # Set the upper limit of the number range
    attempts = 0        # Initialize the number of attempts

    print("Think of a number between 1 and 100 and type 'ok' when you're ready.")
    response = input()  # Prompt the user to start the game

    if response.lower() != 'ok':
        print("Sorry, I didn't understand your response. Please type 'ok' to begin.")
        return   # Exit the function if the response is not 'ok'

    while True:
        guess = random.randint(lower_limit, upper_limit)  # Generate a random guess within the limits
        print("I'm guessing the number:", guess)  # Display the current guess
        response = input("Is the number higher (>), lower (<), or equal (=) to the guess? ")

        if response == '=':
            print("Correct! The number is", guess)  # The guess is correct, display the message and break the loop
            break
        elif response == '>':
            lower_limit = guess + 1  # Adjust the lower limit based on the guess
        elif response == '<':
            upper_limit = guess - 1  # Adjust the upper limit based on the guess
        else:
            print("Sorry, I didn't understand your response. Please use '>', '<', or '='.")

        attempts += 1  # Increment the number of attempts

    print("Number of attempts:", attempts)  # Display the total number of attempts

guess_number()  # Call the function to start the game

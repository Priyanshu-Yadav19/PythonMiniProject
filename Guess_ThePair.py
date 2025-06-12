import random

# Generate a random 3-digit number
num_digits = 3
choices = list('0123456789')
random.shuffle(choices)
secret_number = ''.join(choices[:num_digits])

def give_hint(secret, guess):
    correct_position = 0
    incorrect_position = 0
    
    for i, digit in enumerate(guess):
        if digit == secret[i]:
            correct_position += 1
        elif digit in secret:
            incorrect_position += 1

    return correct_position, incorrect_position

# Initialize guess counter
guess_counter = 0

# Game loop
print("Welcome to the number guessing game!")
print(f"Guess the {num_digits}-digit number. Enter 'exit' to quit.")
while True:
    user_guess = input("Enter your guess: ")
    guess_counter += 1  # Increment counter for each guess
    
    if user_guess.lower() == 'exit':
        print(f"The secret number was: {secret_number}")
        print(f"You made {guess_counter - 1} guesses before quitting.")
        print("Thanks for playing!")
        break
    
    if len(user_guess) != num_digits or not user_guess.isdigit():
        print(f"Please enter a valid {num_digits}-digit number.")
        guess_counter -= 1  # Don't count invalid guesses
        continue
    
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the number correctly in {guess_counter} guesses!")
        break
    else:
        correct, incorrect = give_hint(secret_number, user_guess)
        print(f"Hint: {correct} digit(s) in the correct place, {incorrect} digit(s) correct but in the wrong place.")

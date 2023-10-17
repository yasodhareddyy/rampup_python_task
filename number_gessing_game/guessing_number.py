import random

print("Welcome to the Number Guessing Game!")

# Get the range from the user
lower_limit = int(input("Enter the lower limit of the range: "))
upper_limit = int(input("Enter the upper limit of the range: "))

# Generate a random number within the specified range
secret_number = random.randint(lower_limit, upper_limit)
#print(secret_number)
print(f"I have selected a random number between {lower_limit} and {upper_limit}.")

attempts = 0
while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Try a higher number.")
        elif user_guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number ({secret_number}) in {attempts} attempts!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer guess.")



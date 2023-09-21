import random

# Function to generate a random username
def generate_username(length=8):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    while True:
        username = ''.join(random.choice(characters) for i in range(length))
        yield username

# Set to store generated usernames to check for uniqueness
used_usernames = set()

# Create a generator for unique usernames
username_generator = generate_username()

# Main loop to generate and check unique usernames
while True:
    new_username = next(username_generator)  # Generate the next random username
    if new_username not in used_usernames:
        used_usernames.add(new_username)  # Add the username to the set of used usernames
        print("Generated Unique Username:", new_username)
    else:
        print("Username already exists:", new_username)

    # Ask the user if they want to generate another username
    response = input("Do you want to generate another username? (yes/no): ").lower()
    if response != "yes":
        break

print("Exiting the program.")

"""
Task 6:
If you are building a function to update a user's profile information in a web application.
You pass the user's profile dictionary to the function. It's crucial to understand how Python handles object references
 to ensure that the changes made to the user's profile inside the function persist outside the function.

"""
def update_profile(profile):
    print("Choose an action:")
    print("1. Update existing data")
    print("2. Add new data")

    action_choice = input("Enter the number of the action you want to perform: ")

    if action_choice == '1':
        print("Choose fields to update:")
        print("1. Name")
        print("2. Email")

        field_choice = input("Enter the number of the field you want to update: ")

        if field_choice == '1':
            new_name = input("Enter the new name: ")
            profile['name'] = new_name
        elif field_choice == '2':
            new_email = input("Enter the new email: ")
            profile['email'] = new_email
        else:
            print("Invalid field choice. No fields were updated.")
    elif action_choice == '2':
        new_field_name = input("Enter the name of the new field: ")
        new_field_value = input(f"Enter the value for {new_field_name}: ")
        profile[new_field_name] = new_field_value
    else:
        print("Invalid action choice. No changes were made.")


# Create a user's profile dictionary
user_profile = {
    'name': 'yash',
    'email': 'yash@gmail.com'
}

# Print the existing profile data
print("Existing Profile Data:")
print(user_profile)

# Call the function to update the profile with user's choice
update_profile(user_profile)

# Print the updated profile data
print("\nUpdated Profile Data:")
print(user_profile)


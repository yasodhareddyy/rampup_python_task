"""
Task 7:
Develop a simple content management system (CMS) in Python for a blogging platform.
How would you use file handling to implement a feature that allows users to create, read, and edit blog posts stored as text files?
Provide code examples for creating, reading, and editing blog posts.

"""
def create_blog_post():
    title = input("Enter the title of the FILE NAME blog post: ")
    content = input("Enter the content of the blog post: ")

    # Create a new text file with the title as the filename
    with open(f"{title}.txt", "w") as file:
        file.write(f"Title: {title}\n")
        file.write(f"Content:\n{content}\n")

    print(f"Blog post '{title}' has been created successfully!")

def read_blog_post():
    title = input("Enter the title of the FILE NAME blog post you want to read: ")

    try:
        with open(f"{title}.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Blog post '{title}' not found!")

def edit_blog_post():
    title = input("Enter the title of the FILE NAME blog post you want to edit: ")

    try:
        with open(f"{title}.txt", "r") as file:
            content = file.read()
            print(f"Current content:\n{content}")

        new_content = input("Enter the updated content of the blog post: ")

        with open(f"{title}.txt", "w") as file:
            file.write(f"Title: {title}\n")
            file.write(f"Content:\n{new_content}\n")

        print(f"Blog post '{title}' has been updated successfully!")
    except FileNotFoundError:
        print(f"Blog post '{title}' not found!")

def main():
    while True:
        print("\nBlog Post Management Menu:")
        print("1. Create FILE NAME Blog Post")
        print("2. Read Blog Post")
        print("3. Edit Blog Post")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            create_blog_post()
        elif choice == '2':
            read_blog_post()
        elif choice == '3':
            edit_blog_post()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()













#
# import os
#
# def create_blog_post():
#     title = input("Enter the title of the blog post: ")
#     content = input("Enter the content of the blog post: ")
#
#     # Create a new text file with the title as the filename
#     with open(f"{title}.txt", "w") as file:
#         file.write(f"Title: {title}\n")
#         file.write(f"Content:\n{content}\n")
#
#     print(f"Blog post '{title}' has been created successfully!")
#
# def read_blog_post():
#     title = input("Enter the title of the blog post you want to read: ")
#
#     try:
#         with open(f"{title}.txt", "r") as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError:
#         print(f"Blog post '{title}' not found!")
#
# def edit_blog_post():
#     title = input("Enter the title of the blog post you want to edit: ")
#
#     try:
#         with open(f"{title}.txt", "r") as file:
#             content = file.read()
#             print(f"Current content:\n{content}")
#
#         new_content = input("Enter the updated content of the blog post: ")
#
#         with open(f"{title}.txt", "w") as file:
#             file.write(f"Title: {title}\n")
#             file.write(f"Content:\n{new_content}\n")
#
#         print(f"Blog post '{title}' has been updated successfully!")
#     except FileNotFoundError:
#         print(f"Blog post '{title}' not found!")
#
# def update_blog_post():
#     title = input("Enter the title of the blog post you want to update: ")
#
#     try:
#         with open(f"{title}.txt", "r") as file:
#             content = file.read()
#             print(f"Current content:\n{content}")
#
#         field_to_update = input("Select field to update (title/content): ").lower()
#
#         if field_to_update == 'title':
#             new_title = input("Enter the updated title: ")
#
#             # Rename the file with the new title
#             os.rename(f"{title}.txt", f"{new_title}.txt")
#
#             print(f"Blog post '{title}' has been updated to '{new_title}' successfully!")
#
#         elif field_to_update == 'content':
#             new_content = input("Enter the updated content: ")
#
#             with open(f"{title}.txt", "w") as file:
#                 file.write(f"Title: {title}\n")
#                 file.write(f"Content:\n{new_content}\n")
#
#             print(f"Content of blog post '{title}' has been updated successfully!")
#
#         else:
#             print("Invalid field selection. Choose 'title' or 'content'.")
#
#     except FileNotFoundError:
#         print(f"Blog post '{title}' not found!")
#
# def main():
#     while True:
#         print("\nBlog Post Management Menu:")
#         print("1. Create Blog Post")
#         print("2. Read Blog Post")
#         print("3. Edit Blog Post")
#         print("4. Update Blog Post")
#         print("5. Quit")
#
#         choice = input("Enter your choice (1/2/3/4/5): ")
#
#         if choice == '1':
#             create_blog_post()
#         elif choice == '2':
#             read_blog_post()
#         elif choice == '3':
#             edit_blog_post()
#         elif choice == '4':
#             update_blog_post()
#         elif choice == '5':
#             break
#         else:
#             print("Invalid choice. Please select a valid option.")
#
# if __name__ == "__main__":
#     main()

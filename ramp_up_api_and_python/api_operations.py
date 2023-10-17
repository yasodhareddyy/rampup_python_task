import requests

# Base URL of your Flask API
base_url = 'http://localhost:5000'

while True:
    print("Select an operation:")
    print("1. List Books")
    print("2. Get Book Details")
    print("3. Add Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter the operation number: ")

    if choice == '1':
        # List Books (GET)
        response = requests.get(f'{base_url}/books')
        print("List of Books:")
        print(response.json())
    elif choice == '2':
        # Get Book Details (GET)
        book_id_to_get = input("Enter the ID of the book you want to get: ")
        response = requests.get(f'{base_url}/books/{book_id_to_get}')
        print(f"Book Details (ID {book_id_to_get}):")
        print(response.json())
    # elif choice == '3':
    #     # Add Book (POST)
    #     book_name = input("Enter the name of the new book: ")
    #     author = input("Enter the author of the new book: ")
    #     new_book = {"book_name": book_name, "author": author}
    #     response = requests.post(f'{base_url}/books', json=new_book)
    #     print("Added Book:")
    #     print(response.json())
    elif choice == '3':
        # Add Book (POST) with a generated unique ID
        book_name = input("Enter the name of the new book: ")
        author = input("Enter the author of the new book: ")

        # Generate a unique ID for the new book
        response = requests.get(f'{base_url}/books')  # Fetch the list of books
        books = response.json()
        if not books:
            new_id = 1  # If there are no existing books, start with ID 1
        else:
            new_id = 1
            list_of_ids = [book['id'] for book in books]
            for i in range(1, len(books) + 1):
                if i not in list_of_ids:
                    new_id = i
                    break

            new_book = {"id": new_id, "book_name": book_name, "author": author}
            response = requests.post(f'{base_url}/books', json=new_book)
            print("Added Book:")
            print(response.json())
    elif choice == '4':
        # Update Book (PUT)
        book_id_to_update = input("Enter the ID of the book you want to update: ")
        updated_book={}
        updated_book_name = input("wish to update book_name enter 'yes' else press Enter: ")
        if updated_book_name=="yes":
            updated_book['book_name']=input("pass book_name : ")

        updated_author = input("wish to update author_name enter 'yes' else press Enter:  ")
        if updated_author == "yes":
            updated_book['author'] = input("pass author_name : ")

        response = requests.put(f'{base_url}/books/{book_id_to_update}', json=updated_book)
        print(f"Updated Book (ID {book_id_to_update}):")
        print(response.json())
    elif choice == '5':
        # Delete Book (DELETE)
        book_id_to_delete = input("Enter the ID of the book you want to delete: ")
        response = requests.delete(f'{base_url}/books/{book_id_to_delete}')
        print(f"Deleted Book (ID {book_id_to_delete}):")
        print(response.json())
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid operation number.")

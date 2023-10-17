class LibraryItem:
    def __init__(self, title, author, item_type):
        self.title = title
        self.author = author
        self.item_type = item_type
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            raise Exception("Item is already borrowed.")

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            raise Exception("Item is not currently borrowed.")

    def display_info(self):
        print(f"{self.item_type}: {self.title} by {self.author}")


class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title, author, "Book")
        self.isbn = isbn

    def display_info(self):
        print(f"Book: {self.title} by {self.author}, ISBN: {self.isbn}")


class Magazine(LibraryItem):
    def __init__(self, title, publisher):
        super().__init__(title, None, "Magazine")
        self.publisher = publisher

    def display_info(self):
        print(f"Magazine: {self.title}, Publisher: {self.publisher}")


class CD(LibraryItem):
    def __init__(self, title, artist):
        super().__init__(title, None, "CD")
        self.artist = artist

    def display_info(self):
        print(f"CD: {self.title} by {self.artist}")


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class BorrowingHistory:
    def __init__(self):
        self.history = {}

    def add_history(self, user, item):
        self.history[(user.user_id, item.title)] = "Borrowed"


class Library:
    def __init__(self):
        self.items = []
        self.users = []
        self.borrowing_history = BorrowingHistory()

    def add_item(self, item):
        self.items.append(item)

    def add_user(self, user):
        self.users.append(user)

    def display_items(self):
        for item in self.items:
            item.display_info()

    def display_users(self):
        for user in self.users:
            print(f"User ID: {user.user_id}, Name: {user.name}")

    def borrow_item(self, user, item_title):
        for item in self.items:
            if item.title == item_title and not item.is_borrowed:
                item.borrow()
                self.borrowing_history.add_history(user, item)
                print(f"{user.name} has borrowed '{item.title}'.")
                return
        raise Exception(f"'{item_title}' not found or already borrowed.")

    def return_item(self, user, item_title):
        for item in self.items:
            if item.title == item_title and item.is_borrowed:
                item.return_item()
                self.borrowing_history.add_history(user, item)
                print(f"{user.name} has returned '{item.title}'.")
                return
        raise Exception(f"'{item_title}' not found or not borrowed.")


library = Library()  # Create a Library object

while True:
    print("\nLibrary System Menu:")
    print("1. Add an item to the library")
    print("2. Add a user to the library")
    print("3. Display available items")
    print("4. Display users")
    print("5. Borrow an item")
    print("6. Return an item")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item_type = input("Enter item type (Book, Magazine, CD): ").capitalize()
        title = input("Enter title: ")
        if item_type == "Book":
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            item = Book(title, author, isbn)
        elif item_type == "Magazine":
            publisher = input("Enter publisher: ")
            item = Magazine(title, publisher)
        elif item_type == "CD":
            artist = input("Enter artist: ")
            item = CD(title, artist)
        else:
            print("Invalid item type. Please enter Book, Magazine, or CD.")
            continue

        library.add_item(item)
        print(f"'{item.title}' has been added to the library.")

    elif choice == "2":
        name = input("Enter user name: ")
        user = User(len(library.users) + 1, name)
        library.add_user(user)
        print(f"{user.name} has been added as User ID {user.user_id}.")

    elif choice == "3":
        print("\nAvailable items:")
        library.display_items()

    elif choice == "4":
        print("\nUsers in the library:")
        library.display_users()

    elif choice == "5":
        user_id = int(input("Enter User ID: "))
        item_title = input("Enter the title of the item you want to borrow: ")
        user = next((u for u in library.users if u.user_id == user_id), None)
        if user:
            try:
                library.borrow_item(user, item_title)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("User not found.")

    elif choice == "6":
        user_id = int(input("Enter User ID: "))
        item_title = input("Enter the title of the item you want to return: ")
        user = next((u for u in library.users if u.user_id == user_id), None)

        if user:
            try:
                library.return_item(user, item_title)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("User not found.")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")

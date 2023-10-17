import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize an empty list to store books
books = []

# Load existing books from a JSON file if it exists
try:
    with open("books.json", "r") as json_file:
        books = json.load(json_file)
except FileNotFoundError:
    pass

@app.route('/')
def index():
    return "Welcome to the Book API"

# Helper function to save books to a JSON file
def save_books_to_file():
    with open("books.json", "w") as json_file:
        json.dump(books, json_file, indent=4)

# Route to list all books
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(books)

# Route to get details of a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    if 'book_name' in data and 'author' in data:
        new_id = len(books) + 1
        new_book = {

            "book_name": data['book_name'],
            "author": data['author']
        }
        new_book['id']= new_id
        books.append(new_book)
        save_books_to_file()
        return jsonify(new_book), 201
    return jsonify({"error": "Invalid request data"}), 400

# Route to update the details of an existing book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    for book in books:
        if book['id'] == book_id:
            if 'book_name' in data:
                book['book_name'] = data['book_name']
            if 'author' in data:
                book['author'] = data['author']
            save_books_to_file()
            return jsonify(book)
    return jsonify({"error": "Book not found or invalid request data"}), 404

# Route to delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    initial_length = len(books)
    books = [book for book in books if book['id'] != book_id]
    if len(books) < initial_length:
        save_books_to_file()
        return jsonify({"message": "Book deleted successfully"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)



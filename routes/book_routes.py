from flask import Blueprint, request, jsonify
from bson import ObjectId
from models.books import Book
from database.db_config import mongo

book_routes = Blueprint("book_routes", __name__)

@book_routes.route('/add_book', methods=['POST'])
def add_book():
    # Get the book data from the request
    data = request.get_json()

    # Ensure data contains the required fields
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({"error": "Missing title or author"}), 400
    
    # Insert data into the MongoDB collection
    books_collection = mongo.db.books
    result = books_collection.insert_one({
        'title': data['title'],
        'author': data['author'],
        'year': data.get('year', None)  # Optional field
    })
    
    return jsonify({"message": "Book added", "id": str(result.inserted_id)}), 201

# Create a book
@book_routes.route("/books", methods=["POST"])
def create_book():
    data = request.json
    book_id = Book.add_book(data)
    return jsonify({"message": "Book added successfully", "id": book_id})

# Get all books
@book_routes.route("/books", methods=["GET"])
def get_books():
    books = Book.get_books()
    return jsonify(books)

# Get book by ID
@book_routes.route("/books/<id>", methods=["GET"])
def get_book_by_id(id):
    book = Book.get_book_by_id(ObjectId(id))
    if not book:
        return jsonify({"error": "Book not found"})
    return jsonify(book)

# Update a book
@book_routes.route("/books/<id>", methods=["PUT"])
def update_book(id):
    data = request.json
    updated = Book.update_book(ObjectId(id), data)
    if not updated:
        return jsonify({"error": "Book not found"})
    return jsonify({"message": "Book updated successfully"})

# Delete a book
@book_routes.route("/books/<id>", methods=["DELETE"])
def delete_book(id):
    deleted = Book.delete_book(ObjectId(id))
    if not deleted:
        return jsonify({"error": "Book not found"})
    return jsonify({"message": "Book deleted successfully"})
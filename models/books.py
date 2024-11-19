from flask import jsonify
from database.db_config import mongo

class Book:
    @staticmethod
    def add_book(data):
        collection = mongo.db.books
        book_id = collection.insert_one(data).inserted_id
        return str(book_id)

    @staticmethod
    def get_books():
        collection = mongo.db.books
        books = list(collection.find({}, {"_id": 1, "title": 1, "author": 1, "isbn": 1, "copiesAvailable": 1}))
        return books

    @staticmethod
    def get_book_by_id(book_id):
        collection = mongo.db.books
        book = collection.find_one({"_id": book_id})
        return book

    @staticmethod
    def update_book(book_id, data):
        collection = mongo.db.books
        result = collection.update_one({"_id": book_id}, {"$set": data})
        return result.matched_count > 0

    @staticmethod
    def delete_book(book_id):
        collection = mongo.db.books
        result = collection.delete_one({"_id": book_id})
        return result.deleted_count > 0

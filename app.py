from flask import Flask
from database.db_config import init_db
from routes.book_routes import book_routes

app = Flask(__name__)

# Configure MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/db"
init_db(app)

# Register Routes
app.register_blueprint(book_routes)

# Start the server
if __name__ == "__main__":
    app.run(debug=True)

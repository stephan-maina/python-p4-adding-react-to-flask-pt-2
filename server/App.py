from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your Movie model in models.py

@app.route('/api/movies', methods=['GET'])
def get_movies():
    # Fetch and return a list of movies from your database
    # You can customize this as per your data model
    return jsonify({'movies': []})  # Replace with your actual movie data

@app.route('/api/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    # Create a new movie entry in your database
    # You can customize this as per your data model
    return jsonify({'message': 'Movie added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)

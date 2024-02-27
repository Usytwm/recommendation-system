import os
from flask import Flask, jsonify, request
from class_Books import Book
from datetime import date
from flask_cors import CORS
from my_code import MRI

app = Flask(__name__, template_folder='./templates')
CORS(app)
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})

@app.route('/api/search', methods=['GET'])
def get_books():
    titles = request.args.getlist('title')
    if not titles:
        return jsonify({'error': 'Missing query parameter'}),  400
    answer = MRI(titles)
    books = [Books("title_"+i, "author_"+i) for i in answer]
    if title:
        return jsonify([book.serialize() for book in books])
    return jsonify({'error': 'Missing query parameter'}), 400

# @app.route('/api/get_sources', methods=['GET'])
# def get_sources():
#     return jsonify(csv_files)
if __name__ == '__main__':
    app.run(debug=True, port=40000)
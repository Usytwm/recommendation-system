import os
from flask import Flask, jsonify, request
from datetime import date
from flask_cors import CORS
from my_code import MRI

CORS(app)


def get_books():
    if not titles:
    answer = MRI(titles)
   
        return jsonify([book.serialize() for book in books])
    return jsonify({'error': 'Missing query parameter'}), 400

# @app.route('/api/get_sources', methods=['GET'])
# def get_sources():
#     return jsonify(csv_files)
if __name__ == '__main__':
    app.run(debug=True, port=40000)
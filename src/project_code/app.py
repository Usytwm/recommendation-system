import os
from flask import Flask, jsonify, request
import pandas as pd
from utils.class_Books import Book
from datetime import date
from flask_cors import CORS
from my_code import MRI
from utils import enviroments

app = Flask(__name__, template_folder="./templates")
CORS(app)


@app.route("/api/search", methods=["GET"])
def get_books():
    titles = request.args.getlist("title")
    if not titles:
        return jsonify({"error": "Missing query parameter"}), 400
    answer = MRI(titles)
    # print(answer.head())
    # Creando la lista de libros
    books = [Book(row["title"], row["summary"]) for index, row in answer.iterrows()]
    # books = [Book("title_" + i, "description_" + i) for i in answer]
    # var = jsonify([book.serialize() for book in books])
    if titles:
        return jsonify([book.serialize() for book in books])
    return jsonify({"error": "Missing query parameter"}), 400


@app.route("/api/all", methods=["GET"])
def get_all_books():
    data = pd.read_csv(enviroments.completedPath)
    # print(answer.head())
    # Creando la lista de libros
    books = [Book(row["title"], row["summary"]) for index, row in data.iterrows()]
    # books = [Book("title_" + i, "description_" + i) for i in answer]
    # var = jsonify([book.serialize() for book in books])
    if data is not None:
        return jsonify([book.serialize() for book in books])
    return jsonify({"error": "Missing query parameter"}), 400


# @app.route('/api/get_sources', methods=['GET'])
# def get_sources():
#     return jsonify(csv_files)
if __name__ == "__main__":
    app.run(debug=True, port=40000)

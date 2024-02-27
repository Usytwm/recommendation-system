import pandas as pd
import os
from utils.preprocessing import PreprocessingUtils
from utils import enviroments
import time

from models.text_model import TfidfModel
from models.similarity_model import SimilarityModel
from models.recommendation_system import RecommendationSystem

"""
Main script to build and run a book recommendation system.

This script integrates various components including data preprocessing, TF-IDF
modeling, similarity modeling, and the recommendation system itself. It loads and
preprocesses book review data, applies TF-IDF vectorization, computes similarity scores,
and finally generates book recommendations based on a given title.

The script also measures the execution time of the recommendation process.

Functions:
    None

Execution Steps:
1. Load and preprocess data.
2. Create a TF-IDF model and transform the data.
3. Create a similarity model using the TF-IDF matrix.
4. Build the recommendation system.
5. Generate book recommendations for a given book title.
6. Measure and display the execution time.
"""


def MRI(query):
    # Measure start time
    start_time = time.time()
    # Preprocessing data
    preprocess = PreprocessingUtils()

    # Load and preprocess dataset
    if os.path.exists(enviroments.completedPath):
        data = pd.read_csv(enviroments.completedPath)
    else:
        data = pd.read_csv(enviroments.rawPaht)
        data["combined_features"] = (
            data["title"].apply(preprocess.clean)
            + " "
            + data["summary"].apply(preprocess.clean)
        )
        data["combined_features"] = data["combined_features"].fillna("")

        # Aplicar preprocesamiento a la columna combinada
        data["combined_features"] = data["combined_features"].apply(
            preprocess.data_preprocessing
        )

        # Guardar datos preprocesados
        data.to_csv(enviroments.completedPath, index=False)

    # Text modeling, similarity modeling, and recommendation system
    text_model = TfidfModel()
    tfidf_matrix_reduced = text_model.fit_transform(data["combined_features"])
    similarity_model = SimilarityModel(tfidf_matrix_reduced)
    recommendation_system = RecommendationSystem(similarity_model)

    # Creating indices for recommendations
    indices = pd.Series(data.index, index=data["title"]).to_dict()

    # Generate and print recommendations
    recommended_books = recommendation_system.get_recommendations(
        titles=query,
        indices=indices,
        df=data,
    )

    # print(recommended_books)

    # Measure and print execution time
    # end_time = time.time()
    # print("Tiempo de ejecución:", end_time - start_time, "segundos")
    return recommended_books

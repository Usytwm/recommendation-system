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

# Measure start time
start_time = time.time()
# Preprocessing data
preprocess = PreprocessingUtils()

# Load and preprocess dataset
if os.path.exists(enviroments.completedPath):
    df = pd.read_csv(enviroments.completedPath)
else:
    df = pd.read_csv(enviroments.rawPaht)
    df.rename(
        columns={
            "Id": "book_id",
            "User_id": "user_id",
            "review/text": "review",
            "Title": "title",
            "review/score": "rating",
        },
        inplace=True,
    )
    df = df.head(10000)
    df["combined_features"] = df["title"] + " " + df["review"]
    df["combined_features"] = df["combined_features"].fillna("")

    # Aplicar preprocesamiento a la columna combinada
    df["combined_features_clean"] = df["combined_features"].apply(
        preprocess.preprocess_data
    )
    # Guardar datos preprocesados
    df.to_csv(enviroments.completedPath, index=False)


# Text modeling, similarity modeling, and recommendation system
text_model = TfidfModel()
tfidf_matrix_reduced = text_model.fit_transform(df["combined_features_clean"])
similarity_model = SimilarityModel(tfidf_matrix_reduced)
recommendation_system = RecommendationSystem(similarity_model)

# Creating indices for recommendations
indices = pd.Series(df.index, index=df["title"]).to_dict()

# Generate and print recommendations
recommended_books = recommendation_system.get_recommendations_by_user(
    user_id="A252PRC1XBMTQJ", user_books_df=df, indices=indices, df=df
)
# print(
#     recommendation_system.get_recommendations(["Dr. Seuss: American Icon"], indices, df)
# )
print(recommended_books)

# Measure and print execution time
end_time = time.time()
print("Tiempo de ejecución:", end_time - start_time, "segundos")

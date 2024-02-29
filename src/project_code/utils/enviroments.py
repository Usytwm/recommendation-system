# Path to the raw dataset file for book ratings
import os

ruta_actual = (os.path.realpath(__file__))[:-len("utils\enviroments.py")] 

rawPaht = (
    ruta_actual + "data/raw/data.csv"
)

# Path to the processed dataset file where the completed book ratings will be stored
completedPath = ruta_actual + "data/processed/Books_rating_completed.csv"

# Path to the file where the TF-IDF matrix will be saved. This matrix is likely used for feature extraction in the recommendation system.
tfidf_matrix_file = ruta_actual + "data/processed/tfidf_matrix.pkl"

# Path to the file where the cosine similarity matrix will be saved. This matrix is probably used to determine the similarity between different items (books) in the recommendation system.
cosine_sim_file = ruta_actual + "data/processed/cosine_sim.pkl"

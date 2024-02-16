from nltk.stem import SnowballStemmer
import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import os
from utils.preprocessing import PreprocessingUtils
from utils import enviroments
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.decomposition import TruncatedSVD
import time
import pickle

from models.text_model import TfidfModel
from models.similarity_model import SimilarityModel
from models.recommendation_system import RecommendationSystem

preprocess = PreprocessingUtils()

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

start_time = time.time()

text_model = TfidfModel()
tfidf_matrix_reduced = text_model.fit_transform(df["combined_features_clean"])


similarity_model = SimilarityModel(tfidf_matrix_reduced)
recommendation_system = RecommendationSystem(similarity_model)

# Crear índices para las recomendaciones
indices = pd.Series(df.index, index=df["title"]).to_dict()

# Obtener recomendaciones
recommended_books = recommendation_system.get_recommendations(
    "The Scarlet Letter A Romance", indices, df
)
print(recommended_books)

end_time = time.time()
print("Tiempo de ejecución:", end_time - start_time, "segundos")

# ===================================
# Verificar si el archivo preprocesado existe
# if os.path.exists(enviroments.completedPath):
#     # Cargar el archivo preprocesado
#     df = pd.read_csv(enviroments.completedPath)
# else:
#     # Cargar y preprocesar los datos

#     # Cargar datos
#     df = pd.read_csv(enviroments.rawPaht)
#     df.rename(
#         columns={
#             "Id": "book_id",
#             "User_id": "user_id",
#             "review/text": "review",
#             "Title": "title",
#             "review/score": "rating",
#         },
#         inplace=True,
#     )

#     df = df.head(10000)
#     print(df.head())

#     # Limpieza de texto
#     def clean_text(text):
#         text = str(text).lower()
#         text = re.sub("\[.*?\]", "", text)
#         text = re.sub("https?://\S+|www\.\S+", "", text)
#         text = re.sub("<.*?>+", "", text)
#         text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
#         text = re.sub("\n", "", text)
#         text = re.sub("\w*\d\w*", "", text)
#         return text

#     # Verificar si los stopwords ya están descargados
#     try:
#         stop_words = set(stopwords.words("english"))
#     except LookupError:
#         nltk.download("stopwords")
#         stop_words = set(stopwords.words("english"))

#     # Inicializar el stemmer solo si no existe
#     if "stemmer" not in globals():
#         stemmer = SnowballStemmer("english")

#     def preprocess_data(text):
#         text = clean_text(text)
#         text = " ".join(word for word in text.split() if word not in stop_words)
#         text = " ".join(stemmer.stem(word) for word in text.split())
#         return text

#     # Combinar título y reseña en una nueva columna
#     df["combined_features"] = df["title"] + " " + df["review"]
#     df["combined_features"] = df["combined_features"].fillna("")

#     # Aplicar preprocesamiento a la columna combinada
#     df["combined_features_clean"] = df["combined_features"].apply(preprocess_data)

#     # Guardar datos preprocesados
#     df.to_csv(enviroments.completedPath, index=False)

# start_time = time.time()


# # Crear o cargar la matriz TF-IDF
# if os.path.exists(enviroments.tfidf_matrix_file):
#     with open(enviroments.tfidf_matrix_file, "rb") as f:
#         tfidf_matrix_reduced = pickle.load(f)
# else:
#     tfidf = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
#     tfidf_matrix = tfidf.fit_transform(df["combined_features_clean"])
#     svd = TruncatedSVD(n_components=100)
#     tfidf_matrix_reduced = svd.fit_transform(tfidf_matrix)
#     with open(enviroments.tfidf_matrix_file, "wb") as f:
#         pickle.dump(tfidf_matrix_reduced, f)

# # Crear o cargar la matriz de similitud del coseno
# if os.path.exists(enviroments.cosine_sim_file):
#     with open(enviroments.cosine_sim_file, "rb") as f:
#         cosine_sim = pickle.load(f)
# else:
#     cosine_sim = linear_kernel(tfidf_matrix_reduced, tfidf_matrix_reduced)
#     with open(enviroments.cosine_sim_file, "wb") as f:
#         pickle.dump(cosine_sim, f)


# indices = pd.Series(df.index, index=df["title"]).to_dict()


# def get_recommendations(title, cosine_sim=cosine_sim, indices=indices):
#     idx = indices.get(title)
#     if idx is None:
#         raise ValueError("Title not found in dataset")
#     # Obtiene el book_id del libro original
#     book_id_original = df.at[idx, "book_id"]
#     print("Book id original:", book_id_original)

#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     # Filtrar para excluir el libro original por book_id
#     book_indices = [
#         i[0] for i in sim_scores if df.at[i[0], "book_id"] != book_id_original
#     ]

#     # Obtiene los 10 libros más similares
#     book_indices = book_indices[0:10]
#     return df.iloc[book_indices].drop(
#         columns=["combined_features_clean", "combined_features"]
#     )


# print(get_recommendations("The Scarlet Letter A Romance"))
# end_time = time.time()
# print("Tiempo de ejecución:", end_time - start_time, "segundos")

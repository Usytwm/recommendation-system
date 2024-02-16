from nltk.stem import SnowballStemmer
import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import os
from project_code.utils import enviroments


# Verificar si el archivo preprocesado existe
if os.path.exists(enviroments.completedPath):
    # Cargar el archivo preprocesado
    df = pd.read_csv(enviroments.completedPath)
else:
    # Cargar y preprocesar los datos

    # Cargar datos
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

    # Limpieza de texto
    def clean_text(text):
        text = str(text).lower()
        text = re.sub("\[.*?\]", "", text)
        text = re.sub("https?://\S+|www\.\S+", "", text)
        text = re.sub("<.*?>+", "", text)
        text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
        text = re.sub("\n", "", text)
        text = re.sub("\w*\d\w*", "", text)
        return text

    # Verificar si los stopwords ya están descargados
    try:
        stop_words = set(stopwords.words("english"))
    except LookupError:
        nltk.download("stopwords")
        stop_words = set(stopwords.words("english"))

    # Inicializar el stemmer solo si no existe
    if "stemmer" not in globals():
        stemmer = SnowballStemmer("english")

    def preprocess_data(text):
        text = clean_text(text)
        text = " ".join(word for word in text.split() if word not in stop_words)
        text = " ".join(stemmer.stem(word) for word in text.split())
        return text

    df["review_clean"] = df["review"].apply(preprocess_data)

    # Guardar datos preprocesados
    df.to_csv(enviroments.completedPath, index=False)

# Mostrar los datos limpios
df.head()

from sklearn.feature_extraction.text import TfidfVectorizer

# Crear una instancia de TfidfVectorizer
tfidf = TfidfVectorizer(
    max_features=1000
)  # Puedes ajustar el número de características según sea necesario

# Asumiendo que 'review_clean' es tu columna de texto preprocesado
tfidf_matrix = tfidf.fit_transform(df["review_clean"])

# tfidf_matrix es una matriz de características TF-IDF para tus reseñas
from sklearn.metrics.pairwise import linear_kernel

# Calcular la matriz de similitud del coseno
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Construir un mapeo inverso de índices y títulos de libros
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()


def get_recommendations(title, cosine_sim=cosine_sim):
    # Obtener el índice del libro que coincide con el título
    idx = indices[title]

    # Obtener las puntuaciones de similitud con ese libro
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Ordenar los libros en función de las puntuaciones de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Obtener los puntajes de los 10 libros más similares
    sim_scores = sim_scores[1:11]

    # Obtener los índices de libros
    book_indices = [i[0] for i in sim_scores]

    # Devolver los títulos de los 10 libros más similares
    return df["title"].iloc[book_indices]


print(get_recommendations("Some Book Title"))

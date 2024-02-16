import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

from utils import enviroments


class TfidfModel:
    def __init__(self, n_components=100, max_features=1000):
        self.tfidf_vectorizer = TfidfVectorizer(
            max_features=max_features, ngram_range=(1, 2)
        )
        self.svd = TruncatedSVD(n_components=n_components)

    def fit_transform(self, data, paht=enviroments.tfidf_matrix_file):
        if os.path.exists(paht):
            with open(paht, "rb") as f:
                tfidf_matrix_reduced = pickle.load(f)
        else:
            tfidf_matrix = self.tfidf_vectorizer.fit_transform(data)
            tfidf_matrix_reduced = self.svd.fit_transform(tfidf_matrix)
            with open(paht, "wb") as f:
                pickle.dump(tfidf_matrix_reduced, f)
        return tfidf_matrix_reduced

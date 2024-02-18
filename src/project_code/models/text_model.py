import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

from utils import enviroments


class TfidfModel:
    """
    A class to create and manage a TF-IDF model with dimensionality reduction using Truncated Singular Value Decomposition (SVD).

    This class is responsible for creating a TF-IDF vector representation of the text data,
    followed by reducing the dimensionality of this representation using SVD.

    Attributes:
        tfidf_vectorizer (TfidfVectorizer): An instance of TfidfVectorizer for text vectorization.
        svd (TruncatedSVD): An instance of TruncatedSVD for dimensionality reduction.

    Methods:
        fit_transform(data, path): Fits the TF-IDF model to the data and reduces its dimensionality.
    """

    def __init__(self, n_components=100, max_features=1000):
        """
        Initializes the TfidfModel with specified settings for the TF-IDF vectorizer and SVD.

        Args:
            n_components (int, optional): The number of components for Truncated SVD. Defaults to 100.
            max_features (int, optional): The maximum number of features for TF-IDF Vectorizer. Defaults to 1000.
        """
        self.tfidf_vectorizer = TfidfVectorizer(
            max_features=max_features, ngram_range=(1, 2)
        )
        self.svd = TruncatedSVD(n_components=n_components)

    def fit_transform(self, data, path=enviroments.tfidf_matrix_file):
        """
        Fits the TF-IDF model to the provided data and performs dimensionality reduction using SVD.
        If a precomputed model exists at the given path, it loads that model instead of fitting a new one.

        Args:
            data (iterable): The raw text data to be vectorized and reduced.
            path (str, optional): The file path for saving or loading the TF-IDF matrix.
                                  Defaults to the path specified in `enviroments.tfidf_matrix_file`.

        Returns:
            numpy.ndarray: The reduced TF-IDF matrix after applying SVD.
        """
        if os.path.exists(path):
            with open(path, "rb") as f:
                tfidf_matrix_reduced = pickle.load(f)
        else:
            tfidf_matrix = self.tfidf_vectorizer.fit_transform(data)
            tfidf_matrix_reduced = self.svd.fit_transform(tfidf_matrix)
            with open(path, "wb") as f:
                pickle.dump(tfidf_matrix_reduced, f)
        return tfidf_matrix_reduced

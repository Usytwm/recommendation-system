import os
import pickle
from sklearn.metrics.pairwise import linear_kernel
from utils import enviroments


class SimilarityModel:
    """
    A class to create and manage a similarity model based on TF-IDF and cosine similarity.

    This class is responsible for either loading a pre-existing cosine similarity matrix from a file
    or calculating a new cosine similarity matrix using a provided TF-IDF reduced matrix. The cosine
    similarity matrix is used to find similarity scores between different items.

    Attributes:
        cosine_sim (numpy.ndarray): A precomputed cosine similarity matrix.

    Methods:
        get_similarity_scores(idx): Retrieves similarity scores for a given index from the cosine similarity matrix.
    """

    def __init__(self, tfidf_matrix_reduced, path=enviroments.cosine_sim_file):
        """
        Initializes the SimilarityModel by either loading an existing cosine similarity matrix or
        computing a new one from the given TF-IDF matrix.

        Args:
            tfidf_matrix_reduced (numpy.ndarray): The reduced TF-IDF matrix used for computing the cosine similarity.
            path (str): The file path for saving or loading the cosine similarity matrix. Defaults to the path specified in `enviroments.cosine_sim_file`.
        """
        if os.path.exists(path):
            with open(path, "rb") as f:
                self.cosine_sim = pickle.load(f)
        else:
            self.cosine_sim = linear_kernel(tfidf_matrix_reduced, tfidf_matrix_reduced)
            with open(path, "wb") as f:
                pickle.dump(self.cosine_sim, f)

    def get_similarity_scores(self, idx):
        """
        Retrieves the cosine similarity scores for a given index from the cosine similarity matrix.

        Args:
            idx (int): The index in the similarity matrix for which similarity scores are to be retrieved.

        Returns:
            list of tuples: A list where each tuple contains an index and its corresponding cosine similarity score.
        """
        return list(enumerate(self.cosine_sim[idx]))

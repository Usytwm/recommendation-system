import os
import pickle
from sklearn.metrics.pairwise import linear_kernel
from utils import enviroments


class SimilarityModel:
    def __init__(self, tfidf_matrix_reduced, path=enviroments.cosine_sim_file):
        if os.path.exists(path):
            with open(path, "rb") as f:
                self.cosine_sim = pickle.load(f)
        else:
            self.cosine_sim = linear_kernel(tfidf_matrix_reduced, tfidf_matrix_reduced)
            with open(path, "wb") as f:
                pickle.dump(self.cosine_sim, f)

    def get_similarity_scores(self, idx):
        return list(enumerate(self.cosine_sim[idx]))

class RecommendationSystem:
    """
    A class to represent a recommendation system.

    This class is designed to provide book recommendations based on a given similarity model.
    It requires a pre-computed similarity model to identify similar items based on a given title.

    Attributes:
        similarity_model (object): An instance of a similarity model that has a method
                                    `get_similarity_scores` which takes an index and
                                    returns similarity scores.
    """

    def __init__(self, similarity_model):
        """
        Initializes the RecommendationSystem with a similarity model.

        Args:
            similarity_model (object): The similarity model to be used for generating recommendations.
        """
        self.similarity_model = similarity_model

    def get_recommendations(self, title, indices, df):
        """
        Generates a list of book recommendations based on the provided title.

        This method first checks if the title exists in the dataset. It then uses the similarity model
        to find similar books. The recommendations are sorted in descending order of similarity.

        Args:
            title (str): The title of the book for which recommendations are to be made.
            indices (dict): A dictionary mapping titles to their respective indices in the dataset.
            df (DataFrame): The dataframe containing book data.

        Returns:
            DataFrame: A DataFrame of the top 10 recommended books, excluding the input book.

        Raises:
            ValueError: If the title is not found in the dataset.
        """
        if title not in indices:
            raise ValueError("Title not found in dataset")

        idx = indices[title]
        book_id_original = df.at[idx, "book_id"]
        sim_scores = self.similarity_model.get_similarity_scores(idx)

        # Sort the similarity scores in descending order
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Exclude the original book and get indices of similar books
        book_indices = [
            i[0] for i in sim_scores if df.at[i[0], "book_id"] != book_id_original
        ]

        # Get the top 10 similar books
        book_indices = book_indices[0:10]

        # Return the recommended book data
        return df.iloc[book_indices].drop(
            columns=["combined_features_clean", "combined_features"]
        )

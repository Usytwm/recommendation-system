import numpy as np


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

    def get_recommendation(self, title, indices, df):
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

    def get_recommendations_by_user(self, user_id, user_books_df, indices, df):
        """
        Generates a list of book recommendations for a given user ID.

        Args:
            user_id (int): The ID of the user for whom recommendations are to be made.
            user_books_df (DataFrame): The dataframe containing user-book associations.
            indices (dict): A dictionary mapping titles to their respective indices in the dataset.
            df (DataFrame): The dataframe containing book data.

        Returns:
            DataFrame: A DataFrame of the top recommended books, excluding the books read by the user.

        Raises:
            ValueError: If the user ID is not found in the dataset.
        """

        if user_id not in user_books_df["user_id"].values:
            raise ValueError("User ID not found in dataset")
        user_books = df[df["user_id"] == user_id]
        user_books_titles = user_books["title"].tolist()
        # Get all books read by the user
        # user_books = user_books_df[user_books_df["user_id"] == user_id][
        #     "book_id"
        # ].tolist()

        # # Convert book IDs to titles
        # user_books_titles = df[df["book_id"].isin(user_books)]["title"].tolist()

        # # Ensure that the books are in the indices dictionary
        # user_books_titles = [title for title in user_books_titles if title in indices]

        # Now use the existing logic to get recommendations based on these titles
        return self.get_recommendations(user_books_titles, indices, df)

    def get_recommendations(self, titles, indices, df):
        total_sim_scores = np.zeros(len(df))  # Inicializar un array de ceros
        print(titles)

        for title in titles:
            if title not in indices:
                raise ValueError(f"Title '{title}' not found in dataset")

            idx = indices[title]
            sim_scores = self.similarity_model.get_similarity_scores(idx)

            # Sumar las puntuaciones de similitud para cada libro en el DataFrame
            for i, score in sim_scores:
                total_sim_scores[i] += score

        # Calcular el promedio de las puntuaciones de similitud
        avg_sim_scores = total_sim_scores / len(total_sim_scores)

        # Ordenar los índices de los libros según las puntuaciones de similitud en orden descendente
        sorted_indices = np.argsort(avg_sim_scores)[::-1]

        # Excluir los libros originales y obtener los índices de los libros similares
        excluded_indices = [indices[title] for title in titles]
        filtered_indices = [i for i in sorted_indices if i not in excluded_indices]

        # Seleccionar los índices de los libros más similares
        top_book_indices = filtered_indices[:10]

        # Devolver los datos de los libros recomendados
        return df.iloc[top_book_indices].drop(
            columns=["combined_features_clean", "combined_features"]
        )

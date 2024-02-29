import numpy as np
import pandas as pd


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

    def get_recommendations(self, titles, indices, df):
        sim_scores_dict = {}  # Diccionario para almacenar las puntuaciones de similitud

        for title in titles:
            if title not in indices:
                continue

            idx = indices[title]
            sim_scores = self.similarity_model.get_similarity_scores(idx)

            # Acumular las puntuaciones de similitud para cada libro en el diccionario
            for i, score in sim_scores:
                title = df.iloc[i]["title"]
                if title in sim_scores_dict:
                    sim_scores_dict[title].append(score)
                else:
                    sim_scores_dict[title] = [score]

        if not sim_scores_dict:
            return pd.DataFrame(columns=df.columns)

        # Calcular el promedio de las puntuaciones de similitud para cada libro
        avg_sim_scores = {
            title: sum(scores) / len(scores)
            for title, scores in sim_scores_dict.items()
        }

        # Crear un DataFrame con los promedios y los títulos
        avg_scores_df = pd.DataFrame(
            list(avg_sim_scores.items()), columns=["title", "avg_score"]
        )

        # Fusionar con el DataFrame original para obtener todos los datos de los libros
        merged_df = pd.merge(avg_scores_df, df, on="title")

        # Excluir los libros originales
        merged_df = merged_df[~merged_df["title"].isin(titles)]

        # Ordenar el DataFrame por avg_score en orden descendente
        ordered_df = merged_df.sort_values(by="avg_score", ascending=False)

        ordered_df = ordered_df.head(10)

        # Eliminar la columna innecesaria
        final_df = ordered_df.drop(columns=["combined_features"])

        return final_df

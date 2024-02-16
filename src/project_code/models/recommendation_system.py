class RecommendationSystem:
    def __init__(self, similarity_model):
        self.similarity_model = similarity_model

    def get_recommendations(self, title, indices, df):
        if title not in indices:
            raise ValueError("Title not found in dataset")

        idx = indices[title]
        book_id_original = df.at[idx, "book_id"]
        sim_scores = self.similarity_model.get_similarity_scores(idx)

        # Ordenar las puntuaciones de similitud en orden descendente
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        book_indices = [
            i[0] for i in sim_scores if df.at[i[0], "book_id"] != book_id_original
        ]

        # Obtiene los 10 libros más similares
        book_indices = book_indices[0:10]

        # Devolver los datos de los libros recomendados
        return df.iloc[book_indices].drop(
            columns=["combined_features_clean", "combined_features"]
        )

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


ratings_dict = {
    "user_id": [1, 1, 1, 2, 2, 3, 3, 3],
    "movie_id": ["Avengers", "Kalki","KleO", "Harry potter", "King kong", "Quiet Place", "Silence", "Deadpool"],
    "rating": [5, 4, 3, 4, 5, 2, 5, 4]
}


ratings_df = pd.DataFrame(ratings_dict)


utility_matrix = ratings_df.pivot_table(values='rating', index='user_id', columns='movie_id')


utility_matrix_filled = utility_matrix.fillna(0)


user_similarity = cosine_similarity(utility_matrix_filled)
user_similarity_df = pd.DataFrame(user_similarity, index=utility_matrix.index, columns=utility_matrix.index)

def get_recommendations(user_id, num_recommendations=2):
   
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    
    
    similar_users_ratings = utility_matrix.loc[similar_users]
    
    
    movie_recommendation_scores = similar_users_ratings.sum(axis=0)
    
 
    user_rated_movies = utility_matrix.loc[user_id].dropna().index
    movie_recommendation_scores = movie_recommendation_scores.drop(user_rated_movies, errors='ignore')
    
   
    top_recommendations = movie_recommendation_scores.sort_values(ascending=False).head(num_recommendations)
    
    return top_recommendations.index

user_id = 1
recommendations = get_recommendations(user_id)
print(f"Recommended movies for user {user_id}: {recommendations.tolist()}")


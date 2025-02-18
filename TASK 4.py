movies = [
    {"genres": "Drama", "ratings": [5, 4, 5, 4, 5]},
    {"genres": "Crime,Drama", "ratings": [5, 5, 5, 5, 4]},
    {"genres": "Action,Crime,Drama", "ratings": [4, 4, 5, 5, 5]},
    {"genres": "Crime,Drama", "ratings": [5, 4, 5, 4, 5]},
    {"genres": "Drama,Romance", "ratings": [4, 5, 4, 5, 5]},
    {"genres": "Action,Adventure,Sci-Fi", "ratings": [5, 5, 4, 4, 5]},
    {"genres": "Action,Sci-Fi", "ratings": [4, 4, 5, 5, 4]},
    {"genres": "Drama", "ratings": [4, 5, 5, 4, 5]}
]

# Calculate average ratings
for movie in movies:
    movie["avg_rating"] = sum(movie["ratings"]) / len(movie["ratings"])

def recommend_movies(user_genre_preference):
    user_genre_preference = user_genre_preference.lower()

    recommended_movies = [
        (movie["genres"], movie["avg_rating"])
        for movie in movies if user_genre_preference in map(str.lower, movie["genres"].split(","))
    ]

    if recommended_movies:
        recommended_movies.sort(key=lambda x: x[1], reverse=True)  # Sort by highest rating
        print("\nRecommended Movies based on your genre preference:")
        for genres, rating in recommended_movies:
            print(f"Genre: {genres}, Avg Rating: {rating:.1f}")
    else:
        print("No movies found with that genre.")

# Simulated user input to avoid I/O error in sandboxed environments
user_genre_preference = "Drama"  # Change this value to test different genres
recommend_movies(user_genre_preference)

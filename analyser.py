import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

genre_names = []
average_ratings = []
def main():
    content = pd.read_csv("movies.csv")
    genre = content["Genre"].dropna()
    print("The most common Genre is:",genre.mode().iloc[0])
    items_in_genre = content["Genre"].unique().tolist()
    i=0
    while i < len(items_in_genre):
        spec_row = content["Genre"] == items_in_genre[i]
        spec_ratings = content[spec_row]["Rating"].dropna()
        list_of_rating = spec_ratings.tolist()
        if list_of_rating:
            average = sum(list_of_rating)/len(list_of_rating)
            rounded = round(average, 1)
            print(f"{items_in_genre[i]} 's average rating is {rounded}")
            genre_names.append(items_in_genre[i])
            average_ratings.append(rounded)
        i+=1
    return genre_names,average_ratings

def visualise(genres, ratings):
    plt.figure(figsize=(10, 6))
    plt.bar(genres, ratings, color='skyblue')
    plt.xlabel("Movie Genre")
    plt.ylabel("Average Rating")
    plt.title("Average Movie Ratings by Genre")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Movie.png")

main()
visualise(genre_names, average_ratings)


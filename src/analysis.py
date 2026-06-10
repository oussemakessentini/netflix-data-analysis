import pandas as pd
import matplotlib.pyplot as plt


DATA_PATH = "../data/netflix_titles.csv"
IMAGES_PATH = "../images/"
RESULTS_PATH = "../results/insights.txt"


def load_dataset():
    return pd.read_csv(DATA_PATH)


def save_movies_vs_tvshows(df):
    df["type"].value_counts().plot(kind="bar")
    plt.title("Movies vs TV Shows")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(IMAGES_PATH + "movies_vs_tvshows_bar.png")
    plt.close()


def save_top_countries(df):
    df["country"].value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 Countries")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(IMAGES_PATH + "top_countries.png")
    plt.close()


def save_content_growth(df):
    year_counts = df["release_year"].value_counts().sort_index()
    year_counts.plot(kind="line")
    plt.title("Netflix Content Released Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")
    plt.tight_layout()
    plt.savefig(IMAGES_PATH + "content_growth.png")
    plt.close()


def save_top_genres(df):
    genres = df["listed_in"].str.split(", ").explode()
    genres.value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 Genres")
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(IMAGES_PATH + "top_genres.png")
    plt.close()


def save_top_directors(df):
    df["director"].value_counts().head(10).plot(kind="bar")
    plt.title("Top Directors")
    plt.xlabel("Director")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(IMAGES_PATH + "top_directors.png")
    plt.close()


def generate_insights(df):
    genres = df["listed_in"].str.split(", ").explode()

    movie_percentage = df["type"].value_counts(normalize=True)["Movie"] * 100
    tv_show_percentage = df["type"].value_counts(normalize=True)["TV Show"] * 100
    top_country = df["country"].value_counts().idxmax()
    top_genre = genres.value_counts().idxmax()
    top_director = df["director"].value_counts().idxmax()

    missing_percentage = (df.isnull().sum() / len(df)) * 100
    most_missing_column = missing_percentage.sort_values(ascending=False).index[0]

    with open(RESULTS_PATH, "w", encoding="utf-8") as file:
        file.write("Netflix Dataset Analysis\n")
        file.write("========================\n\n")
        file.write(f"Movies represent {movie_percentage:.2f}% of all Netflix content.\n")
        file.write(f"TV Shows represent {tv_show_percentage:.2f}% of all Netflix content.\n")
        file.write(f"The most common country is {top_country}.\n")
        file.write(f"The most common genre is {top_genre}.\n")
        file.write(f"The director with the most titles is {top_director}.\n")
        file.write(f"The column with the most missing data is {most_missing_column}.\n")


def main():
    df = load_dataset()

    print("Dataset loaded successfully.")
    print(df.head())

    save_movies_vs_tvshows(df)
    save_top_countries(df)
    save_content_growth(df)
    save_top_genres(df)
    save_top_directors(df)
    generate_insights(df)

    print("Charts saved in images folder.")
    print("Insights saved in results folder.")


if __name__ == "__main__":
    main()
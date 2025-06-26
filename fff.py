# This is our collaborative effort for the work experience event

import functools
import os

# define a method that take as parameter a file name, which contains CSV data and returns a Pandas DataFrame that I can query as I like
import pandas as pd
def load_csv_data(file_name: str) -> pd.DataFrame:
    """
    Load CSV data from a file and return it as a Pandas DataFrame.

    :param file_name: The name of the CSV file to load.
    :return: A Pandas DataFrame containing the CSV data.
    """
    try:
        movies = pd.read_csv(file_name)
        print(f"Data loaded successfully from {file_name}.")
        return movies
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_name} is empty.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is empty
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return pd.DataFrame()  # Return an empty DataFrame for any other errors

# Write a method for me that takes a single parameter a dataframe, asks the user to input a genre, then returns the dataframe filtered by that genre. I want you to validate the value of the genre to be exactly one of the values from the provided dataframe. Make sure you convert the user input to lower case.
def filter_by_genre(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the DataFrame by user-specified genre.

    :param df: The DataFrame containing movie data.
    :return: A DataFrame filtered by the specified genre.
    """
    if 'Genre' not in df.columns:
        print("The DataFrame does not contain a 'Genre' column.")
        return df

    genres = df['Genre'].unique()
    print("Available genres:", ', '.join(genres))

    while True:
        user_genre = input("Enter a genre to filter by (case insensitive): ").strip().lower()
        if user_genre in [genre.lower() for genre in genres]:
            filtered_df = df[df['Genre'].str.lower() == user_genre]
            print(f"Filtered {len(filtered_df)} movies of genre '{user_genre}'.")
            return filtered_df
        else:
            print(f"Invalid genre '{user_genre}'. Please try again.")

#Create a method that takes a dataframe as a parameter and prints all the rows in the dataframe.
def print_dataframe(df: pd.DataFrame):
    """
    Print all rows in the DataFrame.

    :param df: The DataFrame to print.
    """
    if df.empty:
        print("The DataFrame is empty.")
    else:
        print(df.to_string(index=False))

def filter_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the DataFrame by user-specified year.

    :param df: The DataFrame containing movie data.
    :return: A DataFrame filtered by the specified year.
    """
    if 'Year' not in df.columns:
        print("The DataFrame does not contain a 'Year' column.")
        return df

    years = df['Year'].unique()
    print("Available years:", ', '.join(map(str, years)))

    while True:
        year_comparison_expression = input("Enter a expression to filter the year (e.g., '> 2000', '<= 2010'): ").strip()

        try:
            # Evaluate the user input as a comparison expression
            filtered_df = df.query(f"Year {year_comparison_expression}")
            if filtered_df.empty:
                print(f"No movies found for the condition 'Year {year_comparison_expression}'.")
            else:
                print(f"Filtered {len(filtered_df)} movies for the condition 'Year {year_comparison_expression}'.")
            return filtered_df
        except Exception as e:
            print(f"Invalid expression '{year_comparison_expression}': {e}")
        # user_year = input("Enter a year to filter by: ").strip()
        # if user_year.isdigit() and int(user_year) in years:
        #     filtered_df = df[df['Year'] == int(user_year)]
        #     print(f"Filtered {len(filtered_df)} movies from the year '{user_year}'.")
        #     return filtered_df
        # else:
        #     print(f"Invalid year '{user_year}'. Please try again.")

def main():
    movies = load_csv_data("movies.csv")

    while True:
        filtered_df = filter_by_genre(movies)
        print_dataframe(filtered_df)
        filtered_df = filter_by_year(filtered_df)
        print_dataframe(filtered_df)
        choice = input("Would you like to continue? [Y/N]: ").lower()
        if choice != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()

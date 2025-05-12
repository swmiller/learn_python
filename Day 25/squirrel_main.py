import pprint
import pandas as pd


def main():
    """Main entry point of the program."""
    print("Welcome to the Squirrel Census Program!")

    # Load squirrel census data
    squirrel_data = pd.read_csv(
        "csv\\2018_Central_Park_Squirrel_Census_Squirrel_Data.csv"
    )

    # Create a new DataFrame with the primary fur color and count
    fur_color_counts = squirrel_data["Primary Fur Color"].value_counts().reset_index()
    fur_color_counts.columns = ["Fur Color", "Count"]
    pprint.pprint(fur_color_counts)

    # Save the DataFrame to a CSV file
    fur_color_counts.to_csv(
        "csv\\squirrel_fur_color_counts.csv", index=True, header=True
    )


if __name__ == "__main__":
    main()

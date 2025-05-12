"""
This script generates a CSV file with weather data.
The generated file contains a specified number of rows with random weather conditions,
temperatures, and days of the week.
The script uses the csv module to write the data to a file.
"""

import csv
import random


def generate_weather_data(file_path, num_rows):
    # Possible values for days, temperatures, and conditions
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    conditions = ["Sunny", "Rain", "Cloudy", "Snow", "Windy"]

    # Ensure unique days if num_rows <= 7
    selected_days = random.sample(days, min(num_rows, len(days)))

    # Generate weather data
    weather_data = [["day", "temp", "condition"]]
    for i in range(num_rows):
        day = selected_days[i % len(selected_days)]
        temp = random.randint(-10, 35)  # Random temperature between -10 and 35
        condition = random.choice(conditions)
        weather_data.append([day, temp, condition])

    # Write data to CSV file
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(weather_data)

    print(f"Weather data with {num_rows} rows has been written to {file_path}")


if __name__ == "__main__":
    output_file = ".\\csv\\generated_weather_data.csv"
    num_rows = 5_000_000  # Change this value to generate a different number of rows
    generate_weather_data(output_file, num_rows)

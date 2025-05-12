import time
import os
import psutil
import csv
import pprint
import pandas as pd


def stopwatch(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Execution time for {func.__name__}: {end_time - start_time:.2f} seconds"
        )
        return result

    return wrapper


def log_memory_usage():
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB
    print(f"\nMemory usage: {memory_usage:.2f} MB")


BIG_FILE = (
    False  # Set to True to use the generated file, False to use the original file
)


@stopwatch
def main():
    if BIG_FILE:
        weather_data = pd.read_csv(".\\csv\\generated_weather_data.csv")
    else:
        weather_data = pd.read_csv(".\\csv\\weather_data.csv")

    # Adding a column based on existing data
    weather_data["temp_in_fahrenheit"] = weather_data["temp"] * 9 / 5 + 32

    # Extract temperature data as a list of integers from weather_data
    temperature_data = weather_data["temp"].astype(int).tolist()
    if not BIG_FILE:
        pprint.pprint(weather_data)

    if not BIG_FILE:
        print(f"\n{temperature_data}")

    # Calculate the highest, lowest, and average temperature
    highest_temperature = weather_data["temp"].max()
    lowest_temperature = weather_data["temp"].min()
    average_temperature = weather_data["temp"].mean()

    print(f"\nHighest temperature: {highest_temperature}°C")
    print(f"Lowest temperature: {lowest_temperature}°C")
    print(f"Average temperature: {average_temperature:.2f}°C")

    # Using weather_data calculate the average temperature per day
    average_temp_per_day = weather_data.groupby("day")["temp"].mean()
    print("\nAverage temperature per day:")
    print(average_temp_per_day)

    # Print a count of the conditions (use attribute 'condition' rather than string)
    condition_counts = weather_data.condition.value_counts()
    print("\nCondition counts:")
    print(condition_counts)

    # Dataframe row with the highest temperature
    highest_temp_row = weather_data[weather_data["temp"] == highest_temperature]
    print("\nRow with the highest temperature:")
    print(highest_temp_row)

    log_memory_usage()


if __name__ == "__main__":
    main()

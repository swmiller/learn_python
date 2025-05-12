import time
import os
import psutil
import csv
import pprint


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


# Ineration 1
# @stopwatch
# def read_weather_data(file_path):
#     with open(file_path, "r") as file:
#         return [line.strip() for line in file.readlines()]


# Ineration 2
@stopwatch
def read_weather_data(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)

        # Skip the header row
        header = next(reader)

        return [row for row in reader]


def log_memory_usage():
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB
    print(f"Memory usage: {memory_usage:.2f} MB")


@stopwatch
def main():
    weather_data = read_weather_data(".\\csv\\weather_data.csv")
    # weather_data = read_weather_data(".\\csv\\generated_weather_data.csv")
    pprint.pprint(weather_data)

    # Extract temperature data as a list of integers from weather_data
    temperature_data = [int(row[1]) for row in weather_data]

    # Calculate the average temperature
    average_temperature = sum(temperature_data) / len(temperature_data)
    print(f"Average temperature: {average_temperature:.2f}°C")

    print()
    log_memory_usage()


if __name__ == "__main__":
    main()

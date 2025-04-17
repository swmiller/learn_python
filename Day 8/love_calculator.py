def calculate_love_score(name1, name2):
    # Convert names to lowercase and concatenate them
    combined_names = (name1 + name2).lower()

    # Count occurrences of letters in "true" and "love"
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")

    # Combine counts to form a love score
    love_score = int(str(true_count) + str(love_count))

    # Print the love score
    print(f"Love Score = {love_score}")


calculate_love_score(name1="Angela Yu", name2="Jack Bauer")

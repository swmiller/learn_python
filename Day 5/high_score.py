scores = [34, 55, 76, 85, 92, 23, 45, 67, 89, 91]

# Figure the high score from the list (old way or other languages way)
high_score = 0
for score in scores:
    if score > high_score:
        high_score = score

print("The highest score is:", high_score)

# Sum the list using a for loop (old way or other languages way)
score_sum = 0
for score in scores:
    score_sum += score

print("The sum of the scores is:", score_sum)

# Figure the high score from the list using a built in function (best way)
high_score = max(scores)
print("The highest score is:", high_score)

# Sum the list using a built in function (best way)
score_sum = sum(scores)
print("The sum of the scores is:", score_sum)

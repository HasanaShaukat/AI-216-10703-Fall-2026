def calculate_percentage(obtained, total):
    if total == 0:
        return 0
    return (obtained / total) * 100


def is_passing(score, passing_score):
    return score >= passing_score


def count_values_above_threshold(values, threshold):
    count = 0

    for value in values:
        if value >= threshold:
            count += 1

    return count


percentage = calculate_percentage(423, 500)
print("Percentage:", percentage)

print("Passing:", is_passing(70, 60))
print("Passing:", is_passing(50, 60))

values = [70, 85, 90, 55, 40]
result = count_values_above_threshold(values, 70)
print("Values meeting threshold:", result)
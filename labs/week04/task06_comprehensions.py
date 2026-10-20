raw_scores = [78, -5, 92, 110, 67, 85]

valid_scores = [score for score in raw_scores if 0 <= score <= 100]
normalized_scores = [score / 100 for score in valid_scores]

print("Valid:", valid_scores)
print("Normalized:", normalized_scores)

student_scores = {
    "Ali": 72,
    "Sara": 91,
    "Ahmed": 45,
    "Fatima": 88
}

pass_status = {
    name: score >= 50
    for name, score in student_scores.items()
}

print("Pass status:", pass_status)

labels = [
    "Spam",
    "HAM",
    "spam",
    "Ham",
    "UNKNOWN"
]

normalized_labels = {label.lower() for label in labels}
print("Labels:", sorted(normalized_labels))

training_labels = [
    "spam",
    "ham",
    "spam",
    "promotion",
    "ham"
]

test_labels = [
    "spam",
    "ham",
    "unknown",
    "promotion"
]

training_set = set(training_labels)
test_set = set(test_labels)

print("Unique training labels:", sorted(training_set))
print("In both:", sorted(training_set & test_set))
print("Only in test:", sorted(test_set - training_set))
print("In either:", sorted(training_set | test_set))

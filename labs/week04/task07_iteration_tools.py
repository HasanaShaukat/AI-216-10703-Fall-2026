experiments = [
    0.81,
    0.86,
    0.79,
    0.91
]

for number, score in enumerate(experiments, start=1):
    print(f"Experiment {number}: {score}")

predictions = [True, False, True, True]
actual = [True, False, False, True]

correct_count = 0

for predicted, expected in zip(predictions, actual):
    correct = predicted == expected
    if correct:
        correct_count += 1
    print(f"Predicted: {predicted} | Actual: {expected} | Correct: {correct}")

accuracy = correct_count / len(actual)
print("Accuracy:", accuracy)

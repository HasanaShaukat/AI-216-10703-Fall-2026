import copy

original_scores = [70, 80, 90]
processed_scores = original_scores
processed_scores.append(100)

print("Aliased Original:", original_scores)
print("Aliased Processed:", processed_scores)

original_scores = [70, 80, 90]
processed_scores = original_scores.copy()
processed_scores.append(100)

print("Original:", original_scores)
print("Processed:", processed_scores)

raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"}
]

shallow_copy = raw_predictions.copy()
shallow_copy[0]["label"] = "spam"
print("Raw after shallow copy edit:", raw_predictions)

raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"}
]

deep_copy = copy.deepcopy(raw_predictions)
deep_copy[0]["label"] = "spam"

print("Raw after deep copy edit:", raw_predictions)
print("Deep copy:", deep_copy)

def count_by_label(predictions):
    counts = {}

    for prediction in predictions:
        label = prediction["label"]
        counts[label] = counts.get(label, 0) + 1

    return counts


def get_unique_labels(predictions):
    return {prediction["label"] for prediction in predictions}


def find_unexpected_labels(predictions, allowed_labels):
    labels = get_unique_labels(predictions)
    return labels - allowed_labels


def average_confidence(predictions):
    if not predictions:
        return None

    return sum(
        prediction["confidence"] for prediction in predictions
    ) / len(predictions)


def top_predictions(predictions, count):
    return sorted(
        predictions,
        key=lambda prediction: prediction["confidence"],
        reverse=True
    )[:count]

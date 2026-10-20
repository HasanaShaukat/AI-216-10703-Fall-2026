def filter_by_confidence(predictions, min_confidence):
    return [
        prediction
        for prediction in predictions
        if prediction["confidence"] >= min_confidence
    ]


def split_complete_records(predictions, required_fields):
    complete = []
    incomplete = []

    for record in predictions:
        if all(field in record for field in required_fields):
            complete.append(record)
        else:
            incomplete.append(record)

    return complete, incomplete


def normalize_labels(predictions):
    normalized = []

    for record in predictions:
        new_record = record.copy()
        new_record["label"] = new_record["label"].strip().lower()
        normalized.append(new_record)

    return normalized

model_names = ["model_a", "model_b", "model_c"]

image_size = (224, 224)

model_config = {
    "name": "spam_classifier",
    "threshold": 0.80,
    "version": 2,
    "debug": False
}

unique_labels = {"spam", "ham", "promotion"}

prediction_records = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72}
]

allowed_labels = {"spam", "ham", "promotion"}
received_labels = {"spam", "ham", "unknown"}

print("Scenario A:", model_names)
print("Scenario B:", image_size)
print("Scenario C:", model_config)
print("Scenario D:", unique_labels)
print("Scenario E:", prediction_records)
print("Scenario F:", sorted(received_labels - allowed_labels))

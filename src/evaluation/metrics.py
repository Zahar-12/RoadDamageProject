import json


def load_metrics(path="results/metrics.json"):
    with open(path, "r") as f:
        return json.load(f)


def get_model_metrics(model_name, data):
    return data.get(model_name, None)


def compute_best_model(data):
    best = None
    best_map = -1

    for model, metrics in data.items():
        if metrics["mAP50"] > best_map:
            best_map = metrics["mAP50"]
            best = model

    return best, best_map
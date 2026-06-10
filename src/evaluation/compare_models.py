from src.evaluation.plot_metrics import plot_model_comparison

results = {
    "ssd": {
        "precision": 0.6463,
        "recall": 0.1373,
        "mAP50": 0.7289
    },
    "faster_rcnn": {
        "precision": 0.3902,
        "recall": 0.5509,
        "mAP50": 0.7289
    },
    "yolov8n": {
        "precision": 0.5329,
        "recall": 0.3953,
        "mAP50": 0.4086
    },
    "yolo11n": {
        "precision": 0.5116,
        "recall": 0.4016,
        "mAP50": 0.4019
    },
    "detr": {
        "precision": 0.2194,
        "recall": 0.0371,
        "mAP50": 0.6703
    },
    "yolo26n": {
        "precision": 0.4955,
        "recall": 0.3823,
        "mAP50": 0.3688
    }
}

plot_model_comparison(results)
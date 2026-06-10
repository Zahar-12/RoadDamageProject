import matplotlib.pyplot as plt


def plot_model_comparison(results):

    models = list(results.keys())

    precision = [results[m]["precision"] for m in models]
    recall = [results[m]["recall"] for m in models]
    map50 = [results[m]["mAP50"] for m in models]

    x = range(len(models))

    # -------------------------
    # Precision
    # -------------------------
    plt.figure(figsize=(10,5))
    plt.bar(models, precision)
    plt.title("Precision comparison")
    plt.ylim(0, 1)
    plt.grid()
    plt.show()

    # -------------------------
    # Recall
    # -------------------------
    plt.figure(figsize=(10,5))
    plt.bar(models, recall)
    plt.title("Recall comparison")
    plt.ylim(0, 1)
    plt.grid()
    plt.show()

    # -------------------------
    # mAP50
    # -------------------------
    plt.figure(figsize=(10,5))
    plt.bar(models, map50)
    plt.title("mAP50 comparison")
    plt.ylim(0, 1)
    plt.grid()
    plt.show()
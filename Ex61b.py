import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def generate_data(n_points, dimensions, n_classes):
    """Generate random data."""
    return np.random.randint(n_classes, size=(n_points, dimensions))


def memorization_points(data, n_classes):
    """Calculate the average number"""
    knn = KNeighborsClassifier(n_neighbors=1)
    memorization_counts = []
    for i in range(len(data)):
        train_data = np.delete(data, i, axis=0)
        test_point = data[i].reshape(1, -1)
        labels = np.tile(np.arange(n_classes), len(data) // n_classes + 1)[: len(data)]
        train_labels = np.delete(labels, i)
        test_label = labels[i]
        knn.fit(train_data, train_labels)
        if knn.predict(test_point)[0] == test_label:
            memorization_counts.append(1)
        else:
            memorization_counts.append(0)
    return np.mean(memorization_counts)


def main():
    max_dimensions = 10
    n_points = 1000
    n_classes = 3
    for D in range(1, max_dimensions + 1):
        data = generate_data(n_points, D, n_classes)
        avg_mem_size = memorization_points(data, n_classes)
        n_full = n_classes**D
        print(
            f"d={D}: n_full={n_full}, Avg. req. points for memorization n_avg={avg_mem_size:.2f}, n_full/n_avg={(n_full)/avg_mem_size:.2f}"
        )


if __name__ == "__main__":
    main()

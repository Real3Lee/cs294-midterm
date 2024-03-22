import numpy as np
from sklearn.neighbors import KNeighborsClassifier


def generate_data(n_points, dimensions):
    """Generate random binary data."""
    return np.random.randint(2, size=(n_points, dimensions))


def memorization_points(data):
    """Calculate the average number."""
    knn = KNeighborsClassifier(n_neighbors=1)
    memorization_counts = []
    for i in range(len(data)):
        train_data = np.delete(data, i, axis=0)
        test_point = data[i].reshape(1, -1)
        knn.fit(train_data, train_data)
        if np.array_equal(knn.predict(test_point)[0], test_point.flatten()):
            memorization_counts.append(1)
        else:
            memorization_counts.append(0)
            return np.mean(memorization_counts)


def main():
    max_dimensions = 10
    n_points = 1000
    for D in range(1, max_dimensions + 1):
        data = generate_data(n_points, D)
        avg_mem_size = memorization_points(data)
        n_full = 2**D
        print(
            f"d={D}: n_full={n_full}, Avg. req. points for memorization n_avg={avg_mem_size:.2f}, n_full/n_avg={(n_full)/avg_mem_size:.2f}"
        )


if __name__ == "__main__":
    main()

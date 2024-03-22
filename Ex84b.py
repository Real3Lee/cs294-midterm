from math import log2


def memorize(data, labels):
    unique_labels = set(labels)
    thresholds = 0

    for label in unique_labels:
        table = [(data[i], labels[i]) for i in range(len(labels)) if labels[i] == label]

        sorted_table = sorted(table, key=lambda x: x[0][-1])

        current_class = sorted_table[0][1]

        for row in sorted_table:
            if row[1] != current_class:
                current_class = row[1]
                thresholds += 1

    min_thresholds = log2(thresholds + 1)

    mec = (min_thresholds * (len(data[0]) + 1)) + (min_thresholds + 1)

    return mec

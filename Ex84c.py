from math import log2


def memorize_regression(data, labels):

    unique_labels = len(set(labels))

    min_thresholds = log2(unique_labels + 1)

    mec = (min_thresholds * (len(data[0]) + 1)) + (min_thresholds + 1)

    return mec

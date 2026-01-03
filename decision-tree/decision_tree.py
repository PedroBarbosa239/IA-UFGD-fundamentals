import math
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value


def entropy(y):
    counts = Counter(y)
    total = len(y)
    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent


def information_gain(y, y_left, y_right):
    w_left = len(y_left) / len(y)
    w_right = len(y_right) / len(y)
    return entropy(y) - (w_left * entropy(y_left) + w_right * entropy(y_right))


def split_dataset(X, y, feature, threshold):
    X_left, y_left, X_right, y_right = [], [], [], []
    for xi, yi in zip(X, y):
        if xi[feature] <= threshold:
            X_left.append(xi)
            y_left.append(yi)
        else:
            X_right.append(xi)
            y_right.append(yi)
    return X_left, y_left, X_right, y_right


def best_split(X, y):
    best_gain = 0
    best_feature = None
    best_threshold = None
    n_features = len(X[0])

    for feature in range(n_features):
        thresholds = set(x[feature] for x in X)
        for threshold in thresholds:
            X_l, y_l, X_r, y_r = split_dataset(X, y, feature, threshold)
            if not y_l or not y_r:
                continue
            gain = information_gain(y, y_l, y_r)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold

    return best_feature, best_threshold


def build_tree(X, y, depth=0, max_depth=5):
    if len(set(y)) == 1 or depth == max_depth:
        return Node(value=Counter(y).most_common(1)[0][0])

    feature, threshold = best_split(X, y)
    if feature is None:
        return Node(value=Counter(y).most_common(1)[0][0])

    X_l, y_l, X_r, y_r = split_dataset(X, y, feature, threshold)
    left = build_tree(X_l, y_l, depth + 1, max_depth)
    right = build_tree(X_r, y_r, depth + 1, max_depth)

    return Node(feature, threshold, left, right)


def predict(node, x):
    if node.value is not None:
        return node.value
    if x[node.feature] <= node.threshold:
        return predict(node.left, x)
    return predict(node.right, x)


if __name__ == "__main__":
    X = [
        [2, 3],
        [1, 5],
        [2, 1],
        [3, 2]
    ]
    y = [0, 0, 1, 1]

    tree = build_tree(X, y)
    sample = [2, 2]
    print("Predição:", predict(tree, sample))

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# dataset
data = {
    "Feature1": [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    "Feature2": [0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    "Label": [0, 1, 1, 0, 0, 1, 1, 0, 1, 1],
}
df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
    df[["Feature1", "Feature2"]], df["Label"], test_size=0.2, random_state=42
)

X_train = X_train.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)

# if-then
rules = []
for index, row in X_train.iterrows():
    condition = " and ".join([f"Feature{i+1} == {row[i]}" for i in range(len(row))])
    rules.append(f"if {condition} then Label = {y_train[index]}")

# Remove redundant
pruned_rules = list(set(rules))


# Evaluation
def evaluate_rules(rules, X, y):
    predictions = []
    for _, row in X.iterrows():
        prediction = None
        for rule in rules:
            condition, label = rule.split("then Label = ")
            condition = condition.replace("if ", "").split(" and ")
            match = True
            for cond in condition:
                feature, value = cond.split(" == ")
                if row[feature] != int(value):
                    match = False
                    break
            if match:
                prediction = int(label)
                break
        if prediction is None:
            prediction = y_train.mode()[0]
        predictions.append(prediction)
    return accuracy_score(y, predictions)


# accuracy
test_accuracy = evaluate_rules(pruned_rules, X_test, y_test)

print(f"Original Rules:\n{rules}")
print(f"Pruned Rules:\n{pruned_rules}")
print(f"Number of resulting conditional clauses: {len(pruned_rules)}")
print(f"Accuracy: {test_accuracy * 100}%")

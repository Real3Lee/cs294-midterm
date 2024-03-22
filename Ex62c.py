import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

np.random.seed(42)

# random dataset
num_features = np.random.randint(2, 5)
num_instances = np.random.randint(10, 21)

data = {
    f"Feature{i+1}": np.random.randint(0, 2, size=num_instances)
    for i in range(num_features)
}
data["Label"] = np.random.randint(0, 2, size=num_instances)

df = pd.DataFrame(data)

X = df.drop("Label", axis=1)
y = df["Label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train = X_train.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)

# if-then rules
rules = []
for index, row in X_train.iterrows():
    condition = " and ".join([f"{col} == {row[col]}" for col in X_train.columns])
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

print(f"Number of Features: {num_features}")
print(f"Number of Instances: {num_instances}")
print(f"Original Rules:\n{rules}")
print(f"Pruned Rules:\n{pruned_rules}")
print(f"Number of resulting conditional clauses: {len(pruned_rules)}")
print(f"Accuracy: {test_accuracy * 100}%")

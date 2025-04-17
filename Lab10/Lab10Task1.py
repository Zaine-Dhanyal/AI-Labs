import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from collections import Counter
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
def distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))
class KNN:
    def __init__(self, k):
        self.k = k
    def fit(self, X, y):
        self.X = np.array(X)
        self.y = np.array(y)
    def predict(self, X):
        predictions = []
        for point in X:
            distances = [distance(point, x_train) for x_train in self.X]
            k_idx = np.argsort(distances)[:self.k]
            k_labels = [self.y[i] for i in k_idx]
            majority_vote = Counter(k_labels).most_common(1)[0][0]
            predictions.append(majority_vote)
        return predictions
model = KNN(k=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
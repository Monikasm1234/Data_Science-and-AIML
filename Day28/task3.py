import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("diabetes.csv")

# Features and target
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Decision Tree Classifier
model = DecisionTreeClassifier(criterion="gini", max_depth=5)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

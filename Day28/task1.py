import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("C:\\Users\\HP\\Desktop\\AIML\\Day28\\StudentsPerformance.csv")

# Example features: math, reading, writing scores
X = data[['math score','reading score','writing score']]
# Target: Pass/Fail (create binary label)
data['pass_fail'] = (data[['math score','reading score','writing score']].mean(axis=1) >= 50).astype(int)
y = data['pass_fail']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Decision Tree Classifier
model = DecisionTreeClassifier(criterion="entropy", max_depth=3)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

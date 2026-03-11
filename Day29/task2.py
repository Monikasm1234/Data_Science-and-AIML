import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("WineQT.csv")

# Features and target
X = data.drop(['quality','Id'], axis=1)   # predictors
y = data['quality']                       # target (wine quality score)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build Random Forest Regressor
model = RandomForestRegressor(
    n_estimators=200,       # number of trees
    max_depth=10,           # limit depth for generalization
    min_samples_split=5,    # minimum samples to split
    min_samples_leaf=2,     # minimum samples per leaf
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Feature importance visualization
plt.figure(figsize=(10,6))
sns.barplot(x=model.feature_importances_, y=X.columns)
plt.title("Feature Importance in Wine Quality Prediction")
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("C:\\Users\\HP\\Desktop\\AIML\\Day28\\car data.csv")

# Example features
X = data[['Year','Present_Price','Kms_Driven']]
y = data['Selling_Price']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Decision Tree Regressor
model = DecisionTreeRegressor(max_depth=4, min_samples_split=5)
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, predictions))

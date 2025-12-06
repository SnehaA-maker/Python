# Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score

# Step 1: Load Dataset
data = pd.read_csv("data/student_performance.csv")
print("Dataset Head:\n", data.head())

# Step 2: Explore the Dataset
print("Dataset Info:\n", data.info())
print("Summary Statistics:\n", data.describe())

# Step 3: Preprocess Data
if data.isnull().sum().sum() > 0:
    data = data.dropna()  # Drop missing values
    print("Cleaned Data:\n", data)

# Features and Targets
X = data[['StudyHours', 'AttendanceRate', 'PreviousScores']]
y_score = data['FinalScore']
y_pass = data['PassStatus']

# Step 4: Linear Regression for Score Prediction
X_train_score, X_test_score, y_train_score, y_test_score = train_test_split(X, y_score, test_size=0.2, random_state=42)

linear_model = LinearRegression()
linear_model.fit(X_train_score, y_train_score)

score_predictions = linear_model.predict(X_test_score)
mse = mean_squared_error(y_test_score, score_predictions)
print(f"Mean Squared Error (Score Prediction): {mse}")

# Step 5: Logistic Regression for Pass/Fail Classification
X_train_pass, X_test_pass, y_train_pass, y_test_pass = train_test_split(X, y_pass, test_size=0.2, random_state=42)

logistic_model = LogisticRegression()
logistic_model.fit(X_train_pass, y_train_pass)

pass_predictions = logistic_model.predict(X_test_pass)
accuracy = accuracy_score(y_test_pass, pass_predictions)
print(f"Accuracy (Pass Prediction): {accuracy}")

# Step 6: Save Results to CSV
results = pd.DataFrame({
    'StudyHours': X_test_pass['StudyHours'],
    'AttendanceRate': X_test_pass['AttendanceRate'],
    'PreviousScores': X_test_pass['PreviousScores'],
    'PredictedScore': score_predictions,
    'ActualScore': y_test_score.values,
    'PredictedPass': pass_predictions,
    'ActualPass': y_test_pass.values
})
results.to_csv("results/prediction_results.csv", index=False)
print("Results saved to results/prediction_results.csv")

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Step 1 – Loading the Dataset
# Loading dataset
df = pd.read_csv("data/study_data_300_days.csv")

# Showing first 5 rows
print(df.head())

# Step 2 – Preprocessing the Data
# Features (X) and Target (y)
X= df[['start_hour', 'end_hour', 'energy_level']]
y= df['focus_level']

# Spliting into training (80%) and testing (20%) data
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=42)

print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Step 3 – Training the Regression Model
# Creating and training model
model= LinearRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred= model.predict(X_test)

# Evaluating model
mse= mean_squared_error(y_test, y_pred)
r2= r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Saving model
joblib.dump(model, "study_planner_model.pkl")
print("Model saved as study_planner_model.pkl")

# Step 4 – Creating a Prediction Function
loaded_model= joblib.load("study_planner_model.pkl")

def predict_focus(start_hour, end_hour, energy_level):
    # Put inputs into a DataFrame so it matches training format
    input_data= pd.DataFrame({
        'start_hour':[start_hour],
        'end_hour':[end_hour],
        'energy_level':[energy_level]
    })
        
    # Make prediction
    prediction= loaded_model.predict(input_data)
    return prediction[0]

# Example usage
# result = predict_focus(20, 22, 4)
# print(f"Predicted focus level: {result:.2f}")
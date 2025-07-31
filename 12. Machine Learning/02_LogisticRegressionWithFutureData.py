import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

# Step 2: Load Dataset (used in Day 50)
dataset = pd.read_csv(r"C:\DataScience-GenerativeAI-AgenticAI\Practical\DS-GenAi-AgenticAI-Bootcamp\6-month-AI-Roadmap_2025\6. Shared\Social_Network_Ads.csv") # Make sure it's in your working directory
# Show top rows
dataset.head()

# Step 3: Feature Selection
X = dataset[["Age", "EstimatedSalary"]].values
y = dataset["Purchased"].values

X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, test_size=0.25, random_state=0)

scaler2 = StandardScaler()
X_train2 = scaler2.fit_transform(X_train2)
X_test2 = scaler2.transform(X_test2)

model2 = LogisticRegression()
model2.fit(X_train2, y_train2)

# Predict on test set
y_pred2 = model2.predict(X_test2)

# Accuracy & Confusion Matrix
print("Accuracy:", accuracy_score(y_test2, y_pred2))
print("Confusion Matrix:\n", confusion_matrix(y_test2, y_pred2))


future_data = {
    "User ID": [15724611, 15725621, 15725622, 15720611, 15588044,
                15746039, 15704887, 15746009, 15876009, 15886009],
    "Gender": ["Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female"],
    "Age": [45, 79, 23, 34, 29, 70, 86, 46, 32, 100],
    "EstimatedSalary": [60000, 64000, 78000, 45000, 76000,
                        89000, 120000, 23000, 70000, 90000]
}

future_df = pd.DataFrame(future_data)



X_future = future_df[["Age", "EstimatedSalary"]]
X_future_scaled = scaler2.transform(X_future)


# Step 9: Predict
y_pred_future = model2.predict(X_future_scaled)
future_df["y_pred1"] = y_pred_future


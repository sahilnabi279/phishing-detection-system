import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Create model folder if not exists
os.makedirs("model", exist_ok=True)

# Dummy dataset
data = pd.DataFrame({
    'url_length': [10, 50, 70, 20],
    'has_https': [1, 0, 0, 1],
    'dots': [1, 3, 5, 2],
    'has_at': [0, 1, 1, 0],
    'has_suspicious': [0, 1, 1, 0],
    'label': [0, 1, 1, 0]
})

X = data.drop("label", axis=1)
y = data["label"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model/model.pkl", "wb"))

print("Model trained and saved!")
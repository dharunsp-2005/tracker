import pandas as pd
from sklearn.linear_model import LogisticRegression

# Dummy dataset
data = pd.DataFrame({
    "prior_records": [0, 1, 2, 3, 4],
    "location_match": [0, 1, 1, 1, 0],
    "age": [22, 30, 40, 35, 50],
    "suspect": [0, 0, 1, 1, 1]
})

X = data[["prior_records", "location_match", "age"]]
y = data["suspect"]

model = LogisticRegression()
model.fit(X, y)

def predict_suspect(prior_records, location_match, age):
    prob = model.predict_proba([[prior_records, location_match, age]])
    return round(prob[0][1], 2)

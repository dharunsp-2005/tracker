from fastapi import FastAPI
from ml_predictor import predict_suspect
from immigration_check import immigration_clearance

app = FastAPI(title="Criminal Investigation Tracker")

@app.get("/")
def home():
    return {"message": "Criminal Investigation Tracker Running"}

@app.get("/predict_suspect/")
def suspect_prediction(prior_records: int, location_match: int, age: int):
    probability = predict_suspect(prior_records, location_match, age)
    return {"suspect_probability": probability}

@app.get("/immigration_check/")
def immigration(passport_valid: bool, visa_status: str, watchlist: bool):
    status = immigration_clearance(passport_valid, visa_status, watchlist)
    return {"immigration_status": status}

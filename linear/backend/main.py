from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load trained model
model = joblib.load("model/house_price_model.pkl")


class HouseData(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: str
    guestroom: str
    basement: str
    hotwaterheating: str
    airconditioning: str
    parking: int
    prefarea: str
    furnishingstatus: str


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }


@app.post("/predict")
def predict(data: HouseData):

    input_data = pd.DataFrame([{
        "area": data.area,
        "bedrooms": data.bedrooms,
        "bathrooms": data.bathrooms,
        "stories": data.stories,
        "mainroad": data.mainroad,
        "guestroom": data.guestroom,
        "basement": data.basement,
        "hotwaterheating": data.hotwaterheating,
        "airconditioning": data.airconditioning,
        "parking": data.parking,
        "prefarea": data.prefarea,
        "furnishingstatus": data.furnishingstatus
    }])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_price": float(prediction)
    }

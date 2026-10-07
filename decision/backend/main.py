from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load the trained Decision Tree pipeline
model = joblib.load("model/mushroom_model.pkl")
@app.get("/")
def home():
    return {"message": "Mushroom Classification API is running"}
from pydantic import BaseModel


class MushroomData(BaseModel):
    cap_shape: str
    cap_surface: str
    cap_color: str
    bruises: str
    odor: str
    gill_attachment: str
    gill_spacing: str
    gill_size: str
    gill_color: str
    stalk_shape: str
    stalk_root: str
    stalk_surface_above_ring: str
    stalk_surface_below_ring: str
    stalk_color_above_ring: str
    stalk_color_below_ring: str
    ring_number: str
    ring_type: str
    spore_print_color: str
    population: str
    habitat: str
    veil_color: str
import pandas as pd


@app.post("/predict")
def predict(data: MushroomData):

    input_data = pd.DataFrame([{
        "cap-shape": data.cap_shape,
        "cap-surface": data.cap_surface,
        "cap-color": data.cap_color,
        "bruises": data.bruises,
        "odor": data.odor,
        "gill-attachment": data.gill_attachment,
        "gill-spacing": data.gill_spacing,
        "gill-size": data.gill_size,
        "gill-color": data.gill_color,
        "stalk-shape": data.stalk_shape,
        "stalk-root": data.stalk_root,
        "stalk-surface-above-ring": data.stalk_surface_above_ring,
        "stalk-surface-below-ring": data.stalk_surface_below_ring,
        "stalk-color-above-ring": data.stalk_color_above_ring,
        "stalk-color-below-ring": data.stalk_color_below_ring,
        "veil-color": data.veil_color,
        "ring-number": data.ring_number,
        "ring-type": data.ring_type,
        "spore-print-color": data.spore_print_color,
        "population": data.population,
        "habitat": data.habitat
    }])

    prediction = model.predict(input_data)[0]

    result = "Edible" if prediction == "e" else "Poisonous"

    return {
        "prediction": prediction,
        "result": result
    }
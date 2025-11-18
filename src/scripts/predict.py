# import the packages
import pickle
import xgboost as xgb
from pydantic import BaseModel, Field
from fastapi import FastAPI
import uvicorn


class Water(BaseModel):
    ph : float
    hardness : float = Field(..., le=1000000.0)
    solids : float = Field(..., le=1000000.0)
    chloramines : float = Field(..., le=1000000.0)
    sulfate : float = Field(..., le=1000000.0)
    conductivity : float
    organic_carbon : float = Field(..., le=1000000.0)
    trihalomethanes : float = Field(..., le=1000000.0)
    turbidity : float


class PredictResponse(BaseModel):
    potability_proba: float
    potability: bool


app = FastAPI(title="water-potability-prediction")

# load the model and other pipelines
with open('./models/model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


def predict_single(water):
    X = dv.transform(water)
    dX = xgb.DMatrix(X, feature_names=list(dv.get_feature_names_out()))
    result = model.predict(dX)[0]
    return round(float(result),2)

@app.post("/predict")
def predict(water: Water) -> PredictResponse:
    prob = predict_single(water.model_dump())
    return PredictResponse(
        potability_proba = prob,
        potability = prob>=0.5
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)

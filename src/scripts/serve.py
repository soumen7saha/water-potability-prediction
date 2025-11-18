# for all API points, same as ping.py
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from predict import *

app = FastAPI(title="Homepage")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit_form", response_class=HTMLResponse)
def submit_home(
    request: Request,
    ph: float = Form(...),
    hardness: float = Form(...),
    solids: float = Form(...),
    chloramines: float = Form(...),
    sulfate: float = Form(...),
    conductivity: float = Form(...),
    organic_carbon: float = Form(...),
    trihalomethanes: float = Form(...),
    turbidity: float = Form(...)
):
    water = Water(
        ph=ph, hardness=hardness, solids=solids,
        chloramines=chloramines, sulfate=sulfate, conductivity=conductivity,
        organic_carbon=organic_carbon, trihalomethanes=trihalomethanes, turbidity=turbidity
    )

    resp = predict(water)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction": resp}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)

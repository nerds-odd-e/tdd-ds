# model.feature_names_in_
from contextlib import asynccontextmanager
import joblib
from fastapi import FastAPI

model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    model = joblib.load("./titanic_ml/titanic.joblib")
    yield


app = FastAPI(title="Titanic API", description="Titanic survival prediction",
              lifespan=lifespan)


@app.get("/")
async def index():
    return {"message": "Hello World!"}


@app.get("/hello/{name}")
async def hello(name):
    return {"message": f"Hello {name}!"}


@app.get("/model")
async def model_info():
    global model
    acc = round(model.accuracy, 3)
    model = {
        "dataset": model.dataset,
        "classifier": type(model).__name__,
        "accuracy": acc}
    return {"model": model}

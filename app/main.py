from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Heart attack prediction": "v0.1.0"}


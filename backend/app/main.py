from fastapi import FastAPI

app = FastAPI(title="Field Ops Tracker API")

@app.get("/")
def health_check():
    return {"status": "ok"}

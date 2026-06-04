from fastapi import FastAPI

app = FastAPI(title="ACIP-X1 - Automotive Cognitive Intelligence Platform")

@app.get("/")
def home():
    return {
        "status": "running",
        "project": "ACIP-X1"
    }
import uvicorn
from fastapi import FastAPI
from LegalEaseAPI.routes import router

app = FastAPI(title="LegalEase API")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "LegalEase API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
from fastapi import FastAPI
from rabbits import router as rabbits

app = FastAPI()
app.include_router(rabbits.router)

@app.get("/")
def read_root():
    return "Server is running"

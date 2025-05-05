from fastapi import FastAPI
from monitor import router as monitoring

app = FastAPI()
app.include_router(monitoring.router)

@app.get("/")
def read_root():
    return "Server is running"

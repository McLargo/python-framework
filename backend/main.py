from fastapi import FastAPI

from src.routers import monitoring_router


app = FastAPI()
app.include_router(monitoring_router)

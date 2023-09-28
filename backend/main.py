from fastapi import FastAPI

from src.routers import monitoring_router

# app
app = FastAPI()

# include router
app.include_router(monitoring_router)

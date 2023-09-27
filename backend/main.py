from fastapi import FastAPI

from src.routers.monitoring import router as monitoring_router

# sentry
app = FastAPI()

# include router
app.include_router(monitoring_router)

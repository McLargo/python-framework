from fastapi import APIRouter

router = APIRouter(
    tags=["monitoring"],
)


# liveness endpoint
@router.get(
    "/liveness",
    response_model=dict,
    summary="Liveness and health checks.",
    description="Health checks of the service and its dependencies.")
def liveness() -> dict:
    return {
        "backend_liveness": True,
    }

from fastapi import APIRouter

from src.models import LivenessModel

router = APIRouter(
    tags=["monitoring"],
)


@router.get(
    "/liveness",
    response_model=LivenessModel,
    summary="Liveness and health checks.",
    description="Health checks of the service and its dependencies.")
def liveness() -> LivenessModel:
    return LivenessModel(
        backend_liveness=True
    )

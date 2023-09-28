from pydantic import BaseModel


class LivenessModel(BaseModel):
    backend_liveness: bool

import pytest

from src.models import LivenessModel


def test_liveness() -> None:
    liveness_model: LivenessModel = LivenessModel(backend_liveness=True)
    assert isinstance(liveness_model, LivenessModel)
    assert liveness_model.backend_liveness is True
    assert isinstance(liveness_model.backend_liveness, bool)


def test_liveness_ko() -> None:
    with pytest.raises(ValueError):
        LivenessModel()

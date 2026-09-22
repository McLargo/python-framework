import pytest

from src.models import LivenessModel


@pytest.mark.unit
@pytest.mark.parametrize("backend_liveness", [True, False])
def test_liveness(backend_liveness: bool) -> None:
    liveness_model: LivenessModel = LivenessModel(
        backend_liveness=backend_liveness,
    )
    assert isinstance(liveness_model, LivenessModel)
    assert liveness_model.backend_liveness is backend_liveness
    assert isinstance(liveness_model.backend_liveness, bool)


@pytest.mark.unit
def test_liveness_ko() -> None:
    with pytest.raises(ValueError):
        LivenessModel()  # pyrefly: ignore[missing-argument]

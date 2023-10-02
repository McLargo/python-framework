import pytest

from src.dependencies import Processor
from src.dependencies.sample_processor import SampleProcessor
from src.factory import SampleFactory


def test_factory_ok() -> None:
    storage_factory: Processor = SampleFactory.get_processor(
        processor_type="sample",
    )

    assert isinstance(storage_factory, SampleProcessor)
    assert isinstance(storage_factory, Processor)


def test_factory_ko() -> None:
    with pytest.raises(ValueError) as exc:
        SampleFactory.get_processor(processor_type="invalid")
        assert exc.value == "Invalid processor type"

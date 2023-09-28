from src.dependencies.sample_processor import SampleProcessor


def test_sample_processor() -> None:
    sample_processor: SampleProcessor = SampleProcessor()
    assert sample_processor.sample_method() == "Sample processor method"

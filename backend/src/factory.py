from src.dependencies import Processor
from src.dependencies.sample_processor import SampleProcessor


class SampleFactory:

    @staticmethod
    def get_processor(
        processor_type: str
    ) -> Processor:
        if processor_type == "sample":
            return SampleProcessor()
        else:
            raise ValueError("Invalid processor type")

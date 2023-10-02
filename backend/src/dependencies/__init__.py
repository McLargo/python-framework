from abc import ABC, abstractmethod


class Processor(ABC):
    @abstractmethod
    def sample_method(self) -> str:
        pass  # pragma: no cover

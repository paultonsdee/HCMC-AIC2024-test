from abc import ABC, abstractmethod
from typing import Any

class BaseTool(ABC):

    @abstractmethod
    def run(self, input):
        raise NotImplementedError

    @abstractmethod
    def build_engine(self) -> Any:
        raise NotImplementedError
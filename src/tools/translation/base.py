from abc import ABC, abstractmethod
from typing import Any

class BaseTranslator(ABC):

    def __init__(self,
                 from_lang:str,
                 to_lang:str,
                 auto_clean:bool=False):

        self.from_lang = from_lang
        self.to_lang = to_lang
        self.auto_clean = auto_clean

    @abstractmethod
    def translate(self, text) -> str:
        raise NotImplementedError

    @abstractmethod
    def build_engine(self) -> Any:
        raise NotImplementedError
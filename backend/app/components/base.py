from abc import ABC, abstractmethod


class BaseTool(ABC):

    @abstractmethod
    def run(self, input): 
        raise NotImplementedError
    

class BaseToolFactory(ABC): 

    @abstractmethod
    @staticmethod
    def produce(provider:str, **kwargs): 
        raise NotImplementedError
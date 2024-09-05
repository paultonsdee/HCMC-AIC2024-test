from typing import Optional, Union

from src.tools.base import BaseTool
from src.tools.llms.prompts import SYSTEM_PROMPT

class BaseAgent(BaseTool): 
    def __init__(self,
                api_key: Optional[str],
                model_name: Optional[str]
                ):

        self.api_key = api_key
        self.model_name = model_name


class LLMConfig:
    def __init__(self, 
                 temperature: float = 0.8, 
                 max_tokens: int = 512, 
                 system_prompt: str = SYSTEM_PROMPT):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.system_prompt = system_prompt

    def to_dict(self) -> dict:
        return {
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "system_prompt": self.system_prompt
        }
import requests

try: 
    import openai
except ImportError as ie:
    raise ImportError("`openai` is not installed. Please try `pip install openai`!") from ie

from src.tools.llms import BaseAgent
from src.tools.llms.prompts import PERSONA_PROMPT

class SambaNova(BaseAgent):
  SAMBANOVA_API_URL = "https://fast-api.snova.ai/v1"
  SUPPORTED_MODEL = [
                    "Meta-Llama-3.1-8B-Instruct",          # CL-OL: 8192-1000
                    "Meta-Llama-3.1-70B-Instruct",         # CL-OL: 8192-1000
                    "Meta-Llama-3.1-405B-Instruct"         # CL-OL: 8192-1000
                     ]
  def __init__(self, api_key, model_name="Meta-Llama-3.1-8B-Instruct"):

    self.client = openai.OpenAI(base_url=self.SAMBANOVA_API_URL, 
                                api_key=api_key)

  
    self.SYS_PROMPT = PERSONA_PROMPT
    self.MODEL_NAME = model_name

    super().__init__(api_key=api_key, model_name=model_name)
    
  def run(self, prompt, **kwargs):
    try:
      completion = self.client.chat.completions.create(
        model=self.MODEL_NAME,
        messages=[{"role": "system", "content": self.SYS_PROMPT}, 
                  {"role": "user", "content": prompt}],
        stream=False,
        **kwargs,
      )
      response = ""
      for chunk in completion:
        response += chunk.choices[0].delta.content or ""
      return response
  
    except ValueError as ve: 
      raise ValueError("Got something wrong with the input") from ve
    except requests.exceptions.HTTPError as httpe: 
        raise httpe
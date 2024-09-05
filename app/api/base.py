import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from src.tools.translation import PyTranslator
from src.tools.llms import GeminiAgent

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
llm = GeminiAgent()
translator = PyTranslator()

def translate_to_en(input) -> str: 
    result = translator.run(input)
    return result

def talk_to_llm(prompt) -> str: 
    result = llm.run(input=prompt)
    return result
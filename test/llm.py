import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # Root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

import unittest

from src.tools.llms.gemini import GeminiAgent
from src.tools.llms.groq import GroqAgent

PROMPT = "Tell me a joke"

class TestGemini(unittest.TestCase): 
    def setUp(self): 
        os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
        self.llm = GeminiAgent()

    def test_result(self):
        result = self.llm.run(input=PROMPT)
        self.assertIsInstance(result, str)


class TestGroq(unittest.TestCase): 
    def setUp(self): 
        os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
        self.llm = GroqAgent()

    def test_result(self):
        result = self.llm.run(input=PROMPT)
        self.assertIsInstance(result, str)

if __name__ == "__main__": 
    unittest.main()
import unittest

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

from src.tools.translation import PyTranslator, GoogleTranslator

test_samples = [
        "Tôi muốn tìm hiểu về khoa học.",
        "Bạn có thể cho tôi một gợi ý?",
        "Tôi muốn học cách chơi đàn.",
        "Bạn có thể cho tôi một câu chuyện?",
        "Tôi muốn biết thêm về nghệ thuật.",
        "Bạn có thể cho tôi một bài thơ?",
        "Tôi muốn tìm hiểu về công nghệ.",
        "Bạn có thể cho tôi một bài hát?",
        "Tôi muốn học cách viết.",
        "Bạn có thể cho tôi một câu nói hay?",
        "Tôi muốn tìm hiểu về triết học.",
        "Bạn có thể cho tôi một bài báo?",
        "Tôi muốn học cách vẽ.",
        "Bạn có thể cho tôi một bức tranh?",
        "Tôi muốn tìm hiểu về âm nhạc.",
        "Bạn có thể cho tôi một bản nhạc?",
        "Tôi muốn học cách nấu ăn.",
        "Bạn có thể cho tôi một công thức?",
        "Tôi muốn tìm hiểu về văn học.",
        "Bạn có thể cho tôi một cuốn sách?",
        "Tôi muốn học cách viết thơ.",
        "Bạn có thể cho tôi một bài thơ?",
        "Tôi muốn tìm hiểu về lịch sử.",
        "Bạn có thể cho tôi một cuốn sách về lịch sử?",
        "Tôi muốn học cách chơi đàn.",
        "Bạn có thể cho tôi một bài hát?",
        "Tôi muốn tìm hiểu về văn hóa.",
        "Bạn có thể cho tôi một cuốn sách về văn hóa?",
        "Tôi muốn học cách viết truyện ngắn.",
        "Bạn có thể cho tôi một câu chuyện?",
        "Tôi muốn tìm hiểu về khoa học.",
        "Bạn có thể cho tôi một bài báo khoa học?",
]

class TestPyTranslate(unittest.TestCase):
    def setUp(self):
        self.translator = PyTranslator(auto_clean=True)

    def test_sample(self):
        data = test_samples[0]
        result = self.translator.run(text=data)
        self.assertIsInstance(result, str)

    def test_samples(self):
        for data in test_samples:
            result = self.translator.run(text=data)
            self.assertIsInstance(result, str)

class TestGoogleTranslate(unittest.TestCase):
    def setUp(self):
        self.translator = GoogleTranslator(auto_clean=True)

    def test_sample(self):
        data = test_samples[0]
        result = self.translator.run(text=data)
        self.assertIsInstance(result, str)

    def test_samples(self):
        for data in test_samples:
            result = self.translator.run(text=data)
            self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()

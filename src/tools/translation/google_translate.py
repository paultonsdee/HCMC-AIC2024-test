from src.tools.translation import BaseTranslation
from src.pre_processing import clean

class GoogleTranslator(BaseTranslation):

    def __init__(self, from_lang=None, to_lang='en', auto_clean=False):
        super().__init__(from_lang=from_lang, to_lang=to_lang, auto_clean=auto_clean)
        if from_lang is None:
            self.from_lang = 'vi'
        self.translator = self.build_engine()

    def run(self, text: str) -> str:
        if self.auto_clean:
            text = clean(text)
        result = self.translator.translate(text).text
        return result

    def build_engine(self):
        try:
            import googletrans
            translator = googletrans.Translator()
            return translator
        except ValueError as ve:
            raise ValueError('`googletrans` is not installed. Please try `pip install googletrans`') from ve
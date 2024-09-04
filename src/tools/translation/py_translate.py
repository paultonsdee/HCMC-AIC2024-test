from src.tools.translation import BaseTranslation
from src.pre_processing import clean

class Translator(BaseTranslation):

    def __init__(self, from_lang='vi', to_lang='en', auto_clean=False):

        if from_lang is None:
            self.from_lang = 'autodetect'
        self.translator = self.build_engine()
    
    def run(self, text: str) -> str:
        if self.auto_clean:
            text = clean(text)
        result = self.translator.translate(text)
        assert type(result) == str
        return result

    def build_engine(self):
        try:
            import translate
            translator = translate.Translator(from_lang=self.from_lang, to_lang=self.to_lang)
            return translator
        except ValueError:
            raise ValueError('`translate` is not installed. Please try `pip install translate`')
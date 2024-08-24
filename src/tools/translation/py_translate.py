from src.tools.translation.base import BaseTranslator
from src.tools.pre_processing import clean

class Translator(BaseTranslator):

    def __init__(self, from_lang='vi', to_lang='en', auto_clean=False):
        super().__init__(from_lang=from_lang, to_lang=to_lang, auto_clean=auto_clean)

        if from_lang is None:
            self.from_lang = 'autodetect'
        self.translator = self.build_engine()

    def translate(self, text: str) -> str:
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
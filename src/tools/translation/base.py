from src.tools.base import BaseTool


class BaseTranslation(BaseTool): 
    def __init__(self, from_lang=None, to_lang='en', auto_clean=False):
        self.from_lang = from_lang
        self.to_lange = to_lang
        self.auto_clean = auto_clean
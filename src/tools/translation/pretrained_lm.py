from typing import Any

from src.tools.translation.base import BaseTranslator
from src.tools.pre_processing import clean


# TODO: Refactor `model_id` as a dictionary of supported models
# TODO: Develop `PretrainedConfig` for `PretrainedModelTranslator`


class PretrainedModelTranslator(object):
    
    @staticmethod
    def from_pretrained(model_id:str, config) -> Any:
        """_summary_

        Args:
            type (str): All supported model.
            config (_type_): Configuration of translation (from_lang, to_lang, etc.) and 
                                language model (temperature, num_beams, etc.)

        Raises:
            ValueError: Raised when input type is not valid.

        Returns:
            Any: A Translation tool which is implemented HuggingFace's pretrained model. 
        """
        try: 
            match model_id:
                case 'm2m100':
                    return M2M100Translator(**config)
                case "marian": 
                    return MarianTranslator(**config)
                case "envt5": 
                    return EnvT5Translator(**config)
        except ValueError: 
            raise ValueError(f"{model_id} is not supported. Please try again")
            

# HuggingFace's model card: Helsinki-NLP/opus-mt-vi-en
class MarianTranslator(BaseTranslator):
    def __init__(self, from_lang=None, to_lang='en', auto_clean=False):
        super().__init__(from_lang=from_lang, to_lang=to_lang, auto_clean=auto_clean)
        self.model_id = "Helsinki-NLP/opus-mt-vi-en"
        self.tokenizer, self.model = self.build_engine(self.model_id)

    def build_engine(self, model_id):
        try:
            from transformers import MarianMTModel, MarianTokenizer
            tokenizer = MarianTokenizer.from_pretrained(model_id)
            model = MarianMTModel.from_pretrained(model_id).eval()
            return (tokenizer, model)
        except:
            raise ValueError('`transformers` is not installed. Please try `pip install transformers`')

    def translate(self, text):
        if self.auto_clean: 
            text = clean(text)
        input_ids = self.tokenizer(text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        assert type(result) == str
        return result
    

# HuggingFace's model card: Helsinki-NLP/opus-mt-vi-en
class M2M100Translator(BaseTranslator):
    def __init__(self, from_lang=None, to_lang='en', auto_clean=False):
        super().__init__(from_lang=from_lang, to_lang=to_lang, auto_clean=auto_clean)
        self.model_id = "facebook/m2m100_418M"
        self.tokenizer, self.model = self.build_engine(self.model_id)

    def build_engine(self, model_id):
        try:
            from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
            tokenizer = M2M100Tokenizer.from_pretrained(model_id)
            model = M2M100ForConditionalGeneration.from_pretrained(model_id).eval()
            return (tokenizer, model)
        except:
            raise ValueError('`transformers` is not installed. Please try `pip install transformers`')

    def translate(self, text):
        if self.auto_clean: 
            text = clean(text)
        self.tokenizer.src_lang = "vi"
        input_ids = self.tokenizer(text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, forced_bos_token_id=self.tokenizer.get_lang_id("en"))
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        assert type(result) == str
        return result
    

# HuggingFace's model card: VietAI/envit5-translation
class EnvT5Translator(BaseTranslator):
    def __init__(self, from_lang=None, to_lang='en', auto_clean=False):
        super().__init__(from_lang=from_lang, to_lang=to_lang, auto_clean=auto_clean)
        self.model_id = "VietAI/envit5-translation"
        self.tokenizer, self.model = self.build_engine(self.model_id)

    def build_engine(self, model_id):
        try:
            from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
            tokenizer = AutoTokenizer.from_pretrained(model_id)
            model = AutoModelForSeq2SeqLM.from_pretrained(model_id).eval()
            return (tokenizer, model)
        except:
            raise ValueError('`transformers` is not installed. Please try `pip install transformers`')

    def translate(self, text) -> str:
        if self.auto_clean: 
            text = clean(text)
        input_ids = self.tokenizer(text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids)
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        assert type(result) == str
        return result

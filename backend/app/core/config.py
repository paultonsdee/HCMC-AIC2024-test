from dataclasses import dataclass

import torch

from app.models.translation import GoogleTranslator
from app.models.embedding.blip_ import BlipTool
from app.services.vector_store import VectorStore


class Environment:
    def __init__(self):
        self.device = "cuda"
        self.root = "./db"
        self.features = "features"
        self.lst_keyframes = Keyframes()
        self.vid_url = "vid_url.json"


class Keyframes:
    def __init__(self):
        self.path = "s_optimized_keyframes"
        self.format = ".webp"

# class LLM:
#     def __init__(self):
#         self.provider = "groq"
#         self.api_key = None
#         self.llm_config = LLMConfig()

#     class LLMConfig:
#         def __init__(self):
#             self.temperature = 1.0

@dataclass
class Config:
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    environment = Environment()
    translator = GoogleTranslator()
    embedding_model = BlipTool()

    # TODO: Make this fix based on settings on this file, not in `setup_lifespan`
    vector_store = VectorStore

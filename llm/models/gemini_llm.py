import os
from openai import OpenAI
from llm.llm import LLM
from openai.resources.chat import Chat
import tiktoken

class GeminiLLM(LLM):

    TOKENIZER = tiktoken.get_encoding("cl100k_base")
    
    def __init__(self, model_id : str, token_limit : int):
        super().__init__()
        self.client = OpenAI(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.model_id = model_id
        self.token_limit = token_limit

    def _get_model_id(self) -> str:
        return self.model_id

    def _get_chat(self) -> Chat:
        return self.client.chat
    
    def get_token_limit(self) -> int:
        return self.token_limit
    
    def get_token_count(self, role : str, content : str) -> int:
        return len(GeminiLLM.TOKENIZER.encode(f"{role}: {content}"))
    
    def get_rpm_limit(self) -> int:
        return 10
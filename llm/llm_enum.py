from enum import Enum
from llm.llm import LLM
from llm.models.gemini_llm import GeminiLLM


class LLMEnum(Enum):

    Gemini_2_5_Flash = GeminiLLM("gemini-2.5-flash-preview-05-20", 250000)


    def default_llm() -> LLM:
        return LLMEnum.Gemini_2_5_Flash.value
from functools import cache
import os


class PromptHandler:

    PARENT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    CUSTOM_INSTRUCTIONS = "custom_instructions"
    SUPERIOR_NAME = "superior_name"
    SUPERIOR_DESCRIPTION = "superior_description"

    @staticmethod
    def get_agent_prompt(custom_instructions : str, superior_name : str, superior_description : str) -> str:
        main_prompt = PromptHandler._get_main_prompt()
        return main_prompt.format(**{
            PromptHandler.CUSTOM_INSTRUCTIONS : custom_instructions,
            PromptHandler.SUPERIOR_NAME : superior_name,
            PromptHandler.SUPERIOR_DESCRIPTION : superior_description
        })
    
    @staticmethod
    def _get_main_prompt() -> str:
        return PromptHandler._read_file("brood")

    @staticmethod
    @cache
    def _read_file(file_name : str) -> str:
        file_path = os.path.join(PromptHandler.PARENT_FILE_PATH, "prompts", f"{file_name}.md")
        with open(file_path, "r") as file:
            return file.read()
    

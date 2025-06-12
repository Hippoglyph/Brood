from actions.action import Action
from llm.llm import LLM
from prompts_utils.prompt_handler import PromptHandler

class Agent:

    def __init__(self, *, name : str, llm : LLM, custom_instructions : str, actions : list[Action],
                 spawner : "Agent", description : str):
        self.name = name
        self.llm = llm
        self.system_message = None
        self.custom_instructions = custom_instructions
        self.desciption = description
        self.actions = {action.get_name() : action for action in actions}
        self.chat_history = []
        self.spawner = spawner
        self.spawn = []

    def get_name(self) -> str:
        return self.name
    
    def get_description(self) -> str:
        return self.desciption
    
    def add_spawn(self, spawn : "Agent") -> None:
        self.spawn.append(spawn)

    def get_spawner(self) -> "Agent":
        return self.spawner
    
    def get_system_message(self) -> str:
        if self.system_message:
            return self.system_message
        superior_name = "Human"
        superior_description = "The only human in the loop. Responsible to make initial requests and is the stakeholder."
        if self.spawner:
            superior_name = self.spawner.get_name()
            superior_description = self.spawner.get_description()
        self.system_message = PromptHandler.get_agent_prompt(self.custom_instructions, superior_name, superior_description)
        return self.system_message

    def send_message(self, message : str) -> str:
        self.chat_history.extend(LLM.package_user(message))
        response = None
        while (response is None or response.has_action_calls()):
            response = self.llm.query(self.get_system_message(), self.actions.values(), self.chat_history)

            if response.has_action_calls():
                action_responses = [self.actions[action_call.get_name()].execute(action_call.get_arguments()) for action_call in response.get_action_calls()]
                self.chat_history.extend(LLM.package_tool(response.get_action_calls(), action_responses))
            elif response.has_message():
                self.chat_history.extend(LLM.package_response(response.get_message()))
            else:
                raise RuntimeError("Agent failed to produce a response")
        return response.get_message()

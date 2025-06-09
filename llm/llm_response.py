from actions.action_call import ActionCall


class LLMResponse:

    def __init__(self, message : str = None, action_calls : list[ActionCall] = None):
        self.message = message
        self.action_calls = action_calls

    def has_message(self) -> bool:
        return self.message is not None
    
    def has_action_calls(self) -> bool:
        return self.action_calls is not None
    
    def get_message(self) -> str:
        return self.message
    
    def get_action_calls(self) -> list[ActionCall]:
        return self.action_calls
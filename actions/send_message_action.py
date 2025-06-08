from actions.action import Action

class SendMessageAction(Action):

    RECEIVER = "receiver"
    CONTENT = "content"

    def __init__(self, relations_names : list[str]):
        self.relations_names = relations_names

    def get_name(self) -> str:
        return "SendMessage"

    def get_description(self) -> str:
        return "Sends a message to an agent."

    def get_arguments(self) -> dict:
        return {SendMessageAction.RECEIVER : f"The name of the agent that you wish to send a message to. Agent names: {", ".join(self.relations_names)}",
            SendMessageAction.CONTENT : "The message content"
        }
    
    def _sanity_check(arguments : dict) -> str:
        if SendMessageAction.RECEIVER not in arguments:
            print(arguments)
            return "Could not find a receiver"
        if SendMessageAction.CONTENT not in arguments:
            return "Message contained no content"
        # expand
        return None
    
    def execute(self, arguments : dict) -> str:
        if SendMessageAction._sanity_check(arguments):
            print(SendMessageAction._sanity_check(arguments))
            arguments[SendMessageAction.RECEIVER] = arguments[Action.CALLER_AGENT]
            return SendMessageAction._sanity_check(arguments)
        
        header = f"{arguments[Action.CALLER_AGENT].get_name()}:\n"
        return header + arguments[SendMessageAction.CONTENT]
    
    def get_receiver_name(self, arguments : dict) -> str:
        return arguments[SendMessageAction.RECEIVER]
    
    def get_relations_names(self) -> list[str]:
        return self.relations_names
        
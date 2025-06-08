from agents.agent import Agent


class Action:

    NAME = "action_name"

    def get_name(self) -> str:
        pass

    def get_description(self) -> str:
        pass

    def get_definition(self) -> dict:
        pass
    
    def execute(self, arguments : dict) -> str:
        pass

    def prettify(self, arguments : dict) -> str:
        return ""
    
    def acting_agent(self) -> Agent:
        pass

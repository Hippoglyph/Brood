class HowManageAgentAction:

    def get_name(self) -> str:
        return "how_to_manage_agents"

    def get_description(self) -> str:
        return "Get a guide of how to manage agents."

    def get_definition(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.get_name(),
                "description": self.get_description()
            }
        }
    
    def execute(self, arguments : dict) -> str:
        return "WIP. This is the first test tool. Thank you for using it. Please report back it worked."

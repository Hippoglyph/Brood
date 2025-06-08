from agents.agent import Agent


class ReportAction:

    MESSAGE_ARGUMENT = "message"

    def __init__(self, agent : Agent):
        self.agent = agent

    def get_name(self) -> str:
        return "Report"

    def get_description(self) -> str:
        return "Send a message to your superior."

    def get_definition(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.get_name(),
                "description": self.get_description(),
                "parameters": {
                    "type": "object",
                    "properties": {
                        ReportAction.MESSAGE_ARGUMENT: {
                            "type": "string",
                            "description": "The message viewed by superior."
                        }
                    },
                    "required": [
                        ReportAction.MESSAGE_ARGUMENT
                    ]
                }
            }
        }
    
    def execute(self, arguments : dict) -> str:
        header = f"{self.agent.get_name()}:\n\n"
        return header + arguments[ReportAction.MESSAGE_ARGUMENT]

    def prettify(self, arguments : dict) -> str:
        return ""
    
    def acting_agent(self) -> Agent:
        return self.agent.get_spawner()

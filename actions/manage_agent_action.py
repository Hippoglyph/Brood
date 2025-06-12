class HowManageAgentAction:

    ACTION_ARGUMENT = "action"
    CREATE_ACTION_ARGUMENT = "create"
    DELETE_ACTION_ARGUMENT = "delete"
    MODIFY_ACTION_ARGUMENT = "modify"
    TALK_ACTION_ARGUMENT = "talk"

    AGENT_NAME_ARGUMENT = "agent_name"

    def get_name(self) -> str:
        return "manage_agent"

    def get_description(self) -> str:
        return "Manage your sub agent with this tool. Refer to how_to_manage_agents tool for a guide."

    def get_definition(self) -> dict:
        return {
            "type": "function",
            "function": {
                "name": self.get_name(),
                "description": self.get_description(),
                "parameters": {
                    "type": "object",
                    "properties": {
                        HowManageAgentAction.ACTION_ARGUMENT: {
                            "type": "string",
                            "enum": [
                                HowManageAgentAction.CREATE_ACTION_ARGUMENT,
                                HowManageAgentAction.DELETE_ACTION_ARGUMENT,
                                HowManageAgentAction.MODIFY_ACTION_ARGUMENT,
                                HowManageAgentAction.TALK_ACTION_ARGUMENT,
                            ],
                            "description": "What action to perform."
                        },
                        HowManageAgentAction.AGENT_NAME_ARGUMENT: {
                            "type": "string",
                            "description": "The name of the agent you wish to perform the action on."
                        }
                    },
                    "required": [
                        HowManageAgentAction.ACTION_ARGUMENT,
                        HowManageAgentAction.AGENT_NAME_ARGUMENT
                    ]
                }
            }
        }
    
    def execute(self, arguments : dict) -> str:
        return "WIP. This is the first test tool. Thank you for using it. Please report back it worked."

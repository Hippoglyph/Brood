from actions.action import Action

class FailedAction(Action):

    def get_name(self) -> str:
        return "Failed"

    def get_description(self) -> str:
        return "The agent failed to produce an action"

    def get_arguments(self) -> dict:
        return {}
    
    def execute(self, arguments : dict) -> str:
        return "Failed to find parseable action.\nReminder! Action has the format where the outer <action></action> needs to be included:\n <action>\n<action_name>{name of the action}</action_name>\n<{argument name}>{value of argument name}</{argument name}>\n...\n</action>"
    
    def prettify(self, arguments : dict) -> str:
        return "Failed to find parseable action"

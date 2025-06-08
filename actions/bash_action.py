from actions.action import Action
from enviroment.terminal import Terminal


class BashAction(Action):

    COMMAND = "command"

    def __init__(self, run_id : str):
        self.terminal = Terminal(run_id)

    def get_name(self) -> str:
        return "Bash"

    def get_description(self) -> str:
        return "A non-interactive bash terminal running on a Ubuntu system."

    def get_arguments(self) -> dict:
        return {BashAction.COMMAND : "The command. E.g rm script.js"}
    
    def execute(self, arguments : dict) -> str:
        # TODO sanity check
        response = self.terminal.bash(arguments[BashAction.COMMAND])
        return (response + "\n>").strip()
    
    def prettify(self, arguments : dict) -> str:
        return arguments[BashAction.COMMAND]

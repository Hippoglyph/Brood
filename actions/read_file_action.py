from actions.action import Action
from enviroment.terminal import Terminal


class ReadFileAction(Action):

    FILE_PATH = "file_path"

    def __init__(self, run_id : str):
        self.terminal = Terminal(run_id)

    def get_name(self) -> str:
        return "ReadFile"

    def get_description(self) -> str:
        return "Read the content to the file_path. Relative to root."

    def get_arguments(self) -> dict:
        return {ReadFileAction.FILE_PATH : "The path to the file. E.g folder/subfolder/executeable.typ"}
    
    def execute(self, arguments : dict) -> str:
        # TODO sanity check
        relative_path = arguments[ReadFileAction.FILE_PATH]
        if self.terminal.file_exists(relative_path):
            file_content = self.terminal.bash(f"cat {relative_path}")
            return f"The file {relative_path} contained:\n{file_content}"
        return f"The file {relative_path} does not exists"
    
    def prettify(self, arguments : dict) -> str:
        return f"Read from {arguments[ReadFileAction.FILE_PATH]}"
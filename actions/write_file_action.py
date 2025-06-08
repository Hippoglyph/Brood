from actions.action import Action
from enviroment.terminal import Terminal


class WriteFileAction(Action):

    FILE_PATH = "file_path"
    CONTENT = "content"

    def __init__(self, run_id : str):
        self.terminal = Terminal(run_id)

    def get_name(self) -> str:
        return "WriteFile"

    def get_description(self) -> str:
        return "Writes the content to the file_path. Relative to root. Can not override files. Use bash command to delete files if you wish to override."

    def get_arguments(self) -> dict:
        return {WriteFileAction.FILE_PATH : "The path to the file. E.g folder/subfolder/executeable.typ",
            WriteFileAction.CONTENT : "The intended content in the file"
        }
    
    def execute(self, arguments : dict) -> str:
        # TODO sanity check
        return self.terminal.write_file(arguments[WriteFileAction.FILE_PATH], arguments[WriteFileAction.CONTENT])
    
    def prettify(self, arguments : dict) -> str:
        return f"Write to {arguments[WriteFileAction.FILE_PATH]}\n\n{arguments[WriteFileAction.CONTENT]}"

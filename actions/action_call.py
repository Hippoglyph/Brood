class ActionCall:

    def __init__(self, name : str, arguments : dict, raw_tool_call : dict):
        self.name = name
        self.arguments = arguments
        self.raw_tool_call = raw_tool_call

    def get_name(self) -> str:
        return self.name
    
    def get_arguments(self) -> dict:
        return self.arguments
    
    def get_raw_tool_call(self) -> dict:
        return self.raw_tool_call

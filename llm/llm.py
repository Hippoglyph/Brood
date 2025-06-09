import json
import random
import sys
import time
from openai.resources.chat import Chat
from actions.action import Action
from actions.action_call import ActionCall
from llm.llm_response import LLMResponse

class LLM:

    ROLE = "role"
    CONTENT = "content"
    TOOL_CALLS = "tool_calls"
    TOOL_CALL_ID = "tool_call_id"
    TOOL_NAME = "name"
    ROLE_USER = "user"
    ROLE_ASSISTANT = "assistant"
    ROLE_SYSTEM = "system"
    ROLE_TOOL = "tool"

    def __init__(self):
        self.request_count = 0
        self.last_request_time = 0.0  # Time of the last request

    def query(self, system_message : str, actions : list[Action] = [], chat_history : list [dict] = []) -> LLMResponse:
        messages = LLM._package_messages(system_message, chat_history)
        max_retries = 5
        for attempt in range(max_retries):
            try:
                self.enforce_rpm_limit()
                chat_completion = self._get_chat().completions.create(
                    messages=messages,
                    model=self._get_model_id(),
                    temperature=0,
                    top_p=0.95,
                    tools=[action.get_definition() for action in actions]
                )
                break
            except Exception as e:
                if self.is_retry_exception(e):
                    print(f"Rate limit exceeded. Retrying in a moment (attempt {attempt + 1}/{max_retries})")
                    LLM.exponential_backoff(attempt)
                else:
                    raise e
                
        if not chat_completion:
            raise Exception("Failed to get a chat completion after retries.")

        # Parse the tool call
        message_from_llm = chat_completion.choices[0].message
        
        if message_from_llm.tool_calls:
            tool_calls = []
            for tool in message_from_llm.tool_calls:
                tool_name = tool.function.name
                tool_arguments = json.loads(tool.function.arguments)

                tool_calls.append(ActionCall(tool_name, tool_arguments, tool))
            return LLMResponse(action_calls=tool_calls)
        return LLMResponse(message=message_from_llm.content)
    
    def exponential_backoff(attempt, max_delay=60):
        delay = min(2 ** attempt + random.random(), max_delay)
        time.sleep(delay)

    def enforce_rpm_limit(self) -> None:
        self.request_count += 1
        current_time = time.time()
        if self.request_count >= self.get_rpm_limit():
            time_since_last_request = current_time - self.last_request_time
            sleep_time = max(0, 60.0 - time_since_last_request)  # Calculate remaining time in the minute
            if sleep_time > 0:
                print(f"RPM limit reached. Sleeping for {sleep_time:.2f} seconds.")
                time.sleep(sleep_time)
        # Reset count at the start of a new minute (approximated by checking time elapsed)
        if current_time - self.last_request_time >= 60:
            self.request_count = 0  # Reset count at the start of a new minute
        self.last_request_time = current_time

    @staticmethod
    def _package_messages(system_message : str, message : str, chat_history : list [dict]) -> list[dict]:
        messages = [
            {
                LLM.ROLE : LLM.ROLE_SYSTEM,
                LLM.CONTENT : system_message
            }
        ]
        messages.extend(chat_history)
        return messages
    
    def package_user(message : str) -> list[dict]:
        return [
            {
                LLM.ROLE : LLM.ROLE_USER,
                LLM.CONTENT : message
            }
        ]
    
    def package_response(message : str) -> list[dict]:
        return [
            {
                LLM.ROLE : LLM.ROLE_ASSISTANT,
                LLM.CONTENT : message
            }
        ]
    
    def package_tool(action_calls : list[ActionCall], responses : list[str]) -> list[dict]:
        history = [
            {
                LLM.ROLE : LLM.ROLE_ASSISTANT,
                LLM.TOOL_CALLS : [action.get_raw_tool_call() for action in action_calls]
            }
        ]
        for i in range(len(action_calls)):
            actions_call = action_calls[i]
            response = responses[i]
            history.append({
                LLM.ROLE : LLM.ROLE_TOOL,
                LLM.TOOL_CALL_ID : actions_call.get_raw_tool_call().id,
                LLM.TOOL_NAME : actions_call.get_name(),
                LLM.CONTENT : response
            })
    
    def _get_model_id(self) -> str:
        pass

    def _get_chat(self) -> Chat:
        pass
    
    def is_retry_exception(self, exception : Exception) -> bool:
        return False
    
    def get_token_limit(self) -> int:
        return 0
    
    def get_token_count(self, role : str, content : str) -> int:
        return 0
    
    def get_tokens_count(self, history : list[dict]) -> int:
        total_tokens = 0

        for message in history:
            total_tokens += self.get_token_count(message[LLM.ROLE], message[LLM.CONTENT])

        return total_tokens
    
    def get_rpm_limit(self) -> int:
        return sys.maxsize
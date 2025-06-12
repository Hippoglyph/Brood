
from actions.how_manage_agents_action import HowManageAgentAction
from agents.agent import Agent
from llm.llm_enum import LLMEnum


def run():

    mother = Agent(name = "Brood Mother", llm = LLMEnum.default_llm(), 
                   custom_instructions = "You are Brood Mother. You are a special agent. You are the source and the only agent that speaks to a human. Use The Brood to fulfill the user's request to the best of your ability",
                   actions = [HowManageAgentAction()], spawner=None, description="The Brood Mother is the source of The Brood and the only contact to humans.")
    
    while True:
        user_input = input("> ")
        print(mother.send_message(user_input))

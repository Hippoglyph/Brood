
from agents.agent import Agent
from llm.llm_enum import LLMEnum


def run():

    mother = Agent("Brood Mother", LLMEnum.default_llm(), 
                   "You are Brood Mother. You are a special agent. You are the source and the only agent that speaks to a humna. ")

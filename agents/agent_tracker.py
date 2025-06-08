from agents.agent import Agent


class AgentTracker:

    agent_map = {}

    @staticmethod
    def init(agents : list[Agent]) -> None:
        for agent in agents:
            AgentTracker.agent_map[agent.get_name()] = agent

    @staticmethod
    def get(agent_name : str) -> Agent:
        return AgentTracker.agent_map.get(agent_name)
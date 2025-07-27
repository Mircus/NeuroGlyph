# ng_engine/__init__.py

"""
NG Engine Runtime: Executes NeuroGlyph ACTs by interpreting structured cognitive acts
and mapping them to live agent systems (e.g., LangChain agents).
"""

__version__ = "0.1.0"

# ng_engine/parser.py

import re
from typing import Dict, Any, List, Union

class NeuroGlyphParser:
    def __init__(self):
        self.pattern = re.compile(r"\s*/(?P<key>[a-zA-Z0-9_]+):(?P<value>.+)")

    def parse_block(self, text: str) -> Dict[str, Union[str, List[str], Dict[str, Any]]]:
        result = {}
        for line in text.strip().split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            match = self.pattern.match(line)
            if match:
                key = match.group("key").strip()
                raw_value = match.group("value").strip()
                if raw_value.startswith("[") and raw_value.endswith("]"):
                    items = [item.strip() for item in raw_value[1:-1].split(";")]
                    result[key] = items
                elif raw_value.startswith("(") and raw_value.endswith(")"):
                    result[key] = {"nested": raw_value[1:-1].strip()}
                else:
                    result[key] = raw_value
        return result

    def render(self, data: Dict[str, Any]) -> str:
        lines = []
        for key, value in data.items():
            if isinstance(value, list):
                line = f"/{key}:[{' ; '.join(value)}]"
            elif isinstance(value, dict):
                inner = value.get("nested", "")
                line = f"/{key}:({inner})"
            else:
                line = f"/{key}:{value}"
            lines.append(line)
        return "\n".join(lines)

# ng_engine/runtime.py

from ng_engine.parser import NeuroGlyphParser
from ng_engine.agent_registry import AgentRegistry
from ng_engine.state_manager import StateManager
from ng_engine.deliverables import DeliverableEngine

class NGRuntime:
    def __init__(self):
        self.parser = NeuroGlyphParser()
        self.registry = AgentRegistry()
        self.state = StateManager()
        self.deliverables = DeliverableEngine()

    def execute(self, ng_input: str) -> str:
        ng_act = self.parser.parse_block(ng_input)
        agent_key = ng_act.get("mind", "default_agent")
        agent_name = agent_key if isinstance(agent_key, str) else agent_key[0]
        agent = self.registry.get_agent(agent_name)
        result = agent.act(ng_act)
        if "deliverable" in ng_act:
            self.deliverables.generate(ng_act, result)
        self.state.update(agent.name, ng_act)
        return result

# ng_engine/agent_registry.py

from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.llm = ChatOpenAI(temperature=0.5)
        self.agent = initialize_agent([], self.llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    def act(self, ng_act):
        prompt = f"Act: {ng_act.get('act')}\nFocus: {ng_act.get('focus')}\nIntent: {ng_act.get('intent', '')}"
        return self.agent.run(prompt)

class AgentRegistry:
    def __init__(self):
        self.agents = {
            "agent_philo": BaseAgent("philo"),
            "agent_ethno": BaseAgent("ethno"),
            "default_agent": BaseAgent("default")
        }

    def get_agent(self, name: str):
        return self.agents.get(name.strip(), self.agents["default_agent"])

# ng_engine/state_manager.py

class StateManager:
    def __init__(self):
        self.memory = {}

    def update(self, agent_name, ng_act):
        self.memory.setdefault(agent_name, []).append(ng_act)

# ng_engine/deliverables.py

class DeliverableEngine:
    def generate(self, ng_act, result):
        print(f"[Deliverable] Generated symbolic output for {ng_act.get('focus')} → {result}")

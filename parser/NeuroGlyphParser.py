
import re
from typing import Union, Dict, List

class NeuroGlyphParser:
    def __init__(self):
        self.token_pattern = re.compile(r"^\s*/(?P<token>[\w_]+):\s*(?P<value>.+)$")
        self.list_pattern = re.compile(r"\[(.*?)\]")
        self.nested_pattern = re.compile(r"\((.*?)\)", re.DOTALL)

    def parse_line(self, line: str) -> Union[Dict[str, Union[str, List[str]]], None]:
        line = line.strip()
        if not line or line.startswith("#"):
            return None

        match = self.token_pattern.match(line)
        if not match:
            return None

        token = match.group("token")
        raw_value = match.group("value").strip()

        # Handle list
        if raw_value.startswith("[") and raw_value.endswith("]"):
            items = [item.strip() for item in raw_value[1:-1].split(";")]
            return {token: items}

        # Handle nested (flat for now)
        elif raw_value.startswith("(") and raw_value.endswith(")"):
            return {token: {"nested": raw_value[1:-1].strip()}}

        # Fallback to plain text
        else:
            return {token: raw_value}

    def parse_block(self, block: str) -> Dict[str, Union[str, List[str], Dict]]:
        lines = block.strip().split("\n")
        result = {}
        for line in lines:
            parsed = self.parse_line(line)
            if parsed:
                result.update(parsed)
        return result

    def render(self, data: Dict[str, Union[str, List[str], Dict]]) -> str:
        lines = []
        for token, value in data.items():
            if isinstance(value, list):
                line = f"/{token}: [{{'; '.join(value)}}]"
            elif isinstance(value, dict) and "nested" in value:
                line = f"/{token}: ({{value['nested']}})"
            else:
                line = f"/{token}: {{value}}"
            lines.append(line)
        return "\n".join(lines)

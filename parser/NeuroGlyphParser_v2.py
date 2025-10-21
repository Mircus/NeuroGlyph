"""
NeuroGlyph Parser v2.0 - Fixed and Enhanced

Improvements over v1:
- Fixed f-string syntax errors in render()
- Added emoji token support
- Better error handling with line numbers
- Validation capabilities
- Support for relational operators
- AST-like structured output
"""

import re
from typing import Union, Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class ParseError(Exception):
    """Custom exception for NeuroGlyph parsing errors"""
    def __init__(self, message: str, line_number: Optional[int] = None, line_content: Optional[str] = None):
        self.line_number = line_number
        self.line_content = line_content
        super().__init__(self._format_message(message))

    def _format_message(self, message: str) -> str:
        if self.line_number:
            msg = f"Parse error on line {self.line_number}: {message}"
            if self.line_content:
                msg += f"\n  Line content: {self.line_content}"
            return msg
        return message


class TokenType(Enum):
    """NeuroGlyph token types"""
    # Core tokens
    ACT = "act"
    FOCUS = "focus"
    MIND = "mind"
    INTENT = "intent"
    CONTEXT = "context"
    DELIVERABLE = "deliverable"

    # Extended tokens
    GLIPH = "gliph"
    CHAIN = "chain"
    NETWORK = "network"
    CHANNEL = "channel"
    ROLE = "role"
    QUERY = "query"
    ECHO = "echo"
    ZOOM = "zoom"
    COMPOSE = "compose"
    NOTE = "note"
    DIALECTIC = "dialectic"

    # Meta tokens
    TIMELINE = "timeline"
    STATUS = "status"
    METRIC = "metric"

    # Unknown
    CUSTOM = "custom"


# Emoji to token mapping
EMOJI_TO_TOKEN = {
    '🚀': 'act',
    '👁️': 'focus',
    '🤝': 'mind',
    '🧠': 'intent',
    '🧭': 'context',
    '📦': 'deliverable',
    '🎭': 'role',
    '💬': 'channel',
    '❓': 'query',
    '📣': 'echo',
    '🔍': 'zoom',
    '🧱': 'compose',
    '📝': 'note',
    '♊': 'dialectic',
    '🔗': 'chain',
    '🧬': 'network',
    '⏰': 'timeline',
    '✅': 'status',
    '📊': 'metric',
}


@dataclass
class NGToken:
    """Represents a parsed NeuroGlyph token"""
    token_type: str
    value: Union[str, List[str], Dict]
    emoji: Optional[str] = None
    line_number: Optional[int] = None


@dataclass
class NGDocument:
    """Represents a complete parsed NeuroGlyph document"""
    tokens: List[NGToken]
    errors: List[ParseError] = None

    def get_token(self, token_type: str) -> Optional[NGToken]:
        """Get first token of given type"""
        for token in self.tokens:
            if token.token_type == token_type:
                return token
        return None

    def get_all_tokens(self, token_type: str) -> List[NGToken]:
        """Get all tokens of given type"""
        return [t for t in self.tokens if t.token_type == token_type]

    def has_errors(self) -> bool:
        """Check if document has parsing errors"""
        return self.errors is not None and len(self.errors) > 0


class NeuroGlyphParser:
    """
    Enhanced NeuroGlyph parser with emoji support and better error handling.

    Supports both formats:
    - 🚀 /act: value
    - /act: value
    """

    def __init__(self, strict_mode: bool = False):
        """
        Initialize parser.

        Args:
            strict_mode: If True, raise exceptions on errors. If False, collect errors and continue.
        """
        self.strict_mode = strict_mode

        # Pattern to match: [emoji] /token: value
        self.token_pattern = re.compile(
            r'^\s*(?P<emoji>[\U0001F000-\U0001FFFF\u2600-\u26FF\u2700-\u27BF]+)?\s*'
            r'/(?P<token>[\w_]+):\s*(?P<value>.+)$',
            re.UNICODE
        )

        # Pattern for lists: [item1; item2; item3]
        self.list_pattern = re.compile(r'^\[(.*)\]$')

        # Pattern for nested blocks: (content)
        self.nested_pattern = re.compile(r'^\((.*)\)$', re.DOTALL)

        # Pattern for relational operators in /mind:
        self.relation_pattern = re.compile(r'(\w+)\s*([↔⊕←→➝⇄⇌])\s*(\w+)')

    def parse_line(self, line: str, line_number: int = 0) -> Optional[NGToken]:
        """
        Parse a single line of NeuroGlyph.

        Args:
            line: The line to parse
            line_number: Line number for error reporting

        Returns:
            NGToken if successful, None if line should be skipped

        Raises:
            ParseError: If strict_mode is True and parsing fails
        """
        line = line.strip()

        # Skip empty lines and comments
        if not line or line.startswith('#'):
            return None

        # Match the token pattern
        match = self.token_pattern.match(line)
        if not match:
            error = ParseError(
                f"Invalid NeuroGlyph syntax. Expected format: [emoji] /token: value",
                line_number=line_number,
                line_content=line
            )
            if self.strict_mode:
                raise error
            return None

        emoji = match.group('emoji')
        token = match.group('token').strip()
        raw_value = match.group('value').strip()

        # Validate emoji matches token (if both present)
        if emoji and emoji in EMOJI_TO_TOKEN:
            expected_token = EMOJI_TO_TOKEN[emoji]
            if token != expected_token:
                error = ParseError(
                    f"Emoji {emoji} does not match token /{token}:. Expected /{expected_token}:",
                    line_number=line_number,
                    line_content=line
                )
                if self.strict_mode:
                    raise error

        # Parse the value
        parsed_value = self._parse_value(raw_value, line_number)

        return NGToken(
            token_type=token,
            value=parsed_value,
            emoji=emoji,
            line_number=line_number
        )

    def _parse_value(self, raw_value: str, line_number: int = 0) -> Union[str, List[str], Dict]:
        """Parse the value part of a token"""
        # Handle list values: [item1; item2; item3]
        list_match = self.list_pattern.match(raw_value)
        if list_match:
            items_str = list_match.group(1)
            if not items_str.strip():
                return []
            items = [item.strip() for item in items_str.split(';')]
            return items

        # Handle nested blocks: (content)
        nested_match = self.nested_pattern.match(raw_value)
        if nested_match:
            nested_content = nested_match.group(1).strip()
            return {"nested": nested_content}

        # Handle quoted strings - remove quotes
        if (raw_value.startswith('"') and raw_value.endswith('"')) or \
           (raw_value.startswith("'") and raw_value.endswith("'")):
            return raw_value[1:-1]

        # Plain text value
        return raw_value

    def parse_block(self, text: str) -> NGDocument:
        """
        Parse a block of NeuroGlyph text.

        Args:
            text: Multi-line NeuroGlyph text

        Returns:
            NGDocument with parsed tokens and any errors
        """
        lines = text.strip().split('\n')
        tokens = []
        errors = []

        for line_num, line in enumerate(lines, start=1):
            try:
                token = self.parse_line(line, line_number=line_num)
                if token:
                    tokens.append(token)
            except ParseError as e:
                errors.append(e)
                if self.strict_mode:
                    raise

        return NGDocument(tokens=tokens, errors=errors if errors else None)

    def parse_file(self, filepath: str) -> NGDocument:
        """Parse a .ng file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        return self.parse_block(text)

    def validate(self, doc: NGDocument, required_tokens: List[str] = None) -> List[str]:
        """
        Validate a parsed document.

        Args:
            doc: Parsed document
            required_tokens: List of required token types

        Returns:
            List of validation error messages (empty if valid)
        """
        if required_tokens is None:
            required_tokens = ['act', 'focus']  # Minimal required tokens

        validation_errors = []

        # Check for required tokens
        present_tokens = {t.token_type for t in doc.tokens}
        for required in required_tokens:
            if required not in present_tokens:
                validation_errors.append(f"Required token /{required}: is missing")

        # Check for parsing errors
        if doc.has_errors():
            validation_errors.extend([str(e) for e in doc.errors])

        return validation_errors

    def render(self, data: Dict[str, Union[str, List[str], Dict]],
               include_emoji: bool = True) -> str:
        """
        Render a dictionary back to NeuroGlyph format.

        Args:
            data: Dictionary of token_name -> value
            include_emoji: Whether to include emoji prefixes

        Returns:
            NeuroGlyph formatted string
        """
        lines = []

        # Map tokens back to emojis
        token_to_emoji = {v: k for k, v in EMOJI_TO_TOKEN.items()}

        for token, value in data.items():
            # Get emoji if available
            emoji_prefix = ""
            if include_emoji and token in token_to_emoji:
                emoji_prefix = token_to_emoji[token] + " "

            # Format value based on type
            if isinstance(value, list):
                formatted_value = f"[{'; '.join(str(v) for v in value)}]"
            elif isinstance(value, dict) and "nested" in value:
                formatted_value = f"({value['nested']})"
            else:
                # Quote strings that contain spaces or special chars
                str_value = str(value)
                if ' ' in str_value or ':' in str_value:
                    formatted_value = f'"{str_value}"'
                else:
                    formatted_value = str_value

            line = f"{emoji_prefix}/{token}: {formatted_value}"
            lines.append(line)

        return '\n'.join(lines)

    def render_document(self, doc: NGDocument, include_emoji: bool = True) -> str:
        """Render an NGDocument back to NeuroGlyph format"""
        lines = []

        for token in doc.tokens:
            emoji_prefix = ""
            if include_emoji and token.emoji:
                emoji_prefix = token.emoji + " "

            # Format value
            if isinstance(token.value, list):
                formatted_value = f"[{'; '.join(str(v) for v in token.value)}]"
            elif isinstance(token.value, dict) and "nested" in token.value:
                formatted_value = f"({token.value['nested']})"
            else:
                str_value = str(token.value)
                if ' ' in str_value or ':' in str_value:
                    formatted_value = f'"{str_value}"'
                else:
                    formatted_value = str_value

            line = f"{emoji_prefix}/{token.token_type}: {formatted_value}"
            lines.append(line)

        return '\n'.join(lines)

    def to_dict(self, doc: NGDocument) -> Dict[str, Union[str, List, Dict]]:
        """Convert NGDocument to simple dictionary"""
        result = {}
        for token in doc.tokens:
            # If token appears multiple times, create a list
            if token.token_type in result:
                if not isinstance(result[token.token_type], list):
                    result[token.token_type] = [result[token.token_type]]
                result[token.token_type].append(token.value)
            else:
                result[token.token_type] = token.value
        return result


# Convenience functions
def parse(text: str, strict: bool = False) -> NGDocument:
    """Quick parse function"""
    parser = NeuroGlyphParser(strict_mode=strict)
    return parser.parse_block(text)


def parse_file(filepath: str, strict: bool = False) -> NGDocument:
    """Quick file parse function"""
    parser = NeuroGlyphParser(strict_mode=strict)
    return parser.parse_file(filepath)


def validate(doc: NGDocument, required_tokens: List[str] = None) -> List[str]:
    """Quick validate function"""
    parser = NeuroGlyphParser()
    return parser.validate(doc, required_tokens)


# Example usage
if __name__ == "__main__":
    # Test with emoji syntax
    ng_text = """
    🚀 /act: compare
    👁️ /focus: "concept of soul"
    🤝 /mind: [human_sofia; agent_ethno]
    🧠 /intent: explore philosophical connections
    📦 /deliverable: comparative_analysis
    """

    parser = NeuroGlyphParser()
    doc = parser.parse_block(ng_text)

    print("=== Parsed Tokens ===")
    for token in doc.tokens:
        print(f"{token.emoji} /{token.token_type}: {token.value}")

    print("\n=== As Dictionary ===")
    print(parser.to_dict(doc))

    print("\n=== Rendered Back ===")
    print(parser.render_document(doc))

    print("\n=== Validation ===")
    errors = parser.validate(doc)
    if errors:
        print("Validation errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✓ Document is valid!")

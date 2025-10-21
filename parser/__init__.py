"""
NeuroGlyph Parser Module

Handles parsing of NeuroGlyph symbolic language
"""

try:
    from .NeuroGlyphParser_v2 import (
        NeuroGlyphParser,
        NGDocument,
        NGToken,
        ParseError,
        TokenType,
        EMOJI_TO_TOKEN,
        parse,
        parse_file,
        validate,
    )

    __all__ = [
        'NeuroGlyphParser',
        'NGDocument',
        'NGToken',
        'ParseError',
        'TokenType',
        'EMOJI_TO_TOKEN',
        'parse',
        'parse_file',
        'validate',
    ]
except ImportError:
    pass

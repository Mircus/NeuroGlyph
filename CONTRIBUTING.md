# Contributing to NeuroGlyph

Thank you for your interest in contributing to NeuroGlyph! 🎉

NeuroGlyph is an open-source symbolic communication protocol designed for structured, multimodal, and multi-agent dialogue. We welcome contributions from everyone.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Development Setup](#development-setup)
4. [Coding Standards](#coding-standards)
5. [Pull Request Process](#pull-request-process)
6. [Issue Guidelines](#issue-guidelines)
7. [Community](#community)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

### Our Standards

**Examples of behavior that contributes to a positive environment:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Examples of unacceptable behavior:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**When creating a bug report, include:**
- **Clear title** - Describe the issue concisely
- **Steps to reproduce** - Detailed steps to recreate the bug
- **Expected behavior** - What you expected to happen
- **Actual behavior** - What actually happened
- **Environment** - OS, Python version, NeuroGlyph version
- **Code samples** - Minimal reproducible example if applicable

**Example:**
```markdown
**Title:** Parser crashes on nested parentheses

**Steps to reproduce:**
1. Create .ng file with nested blocks: `/intent: ((inner content))`
2. Run `parser.parse_file('test.ng')`
3. Parser crashes with TypeError

**Expected:** Should parse nested blocks correctly
**Actual:** TypeError: unhashable type: 'dict'

**Environment:** Windows 11, Python 3.11, NeuroGlyph v0.2.0
```

### Suggesting Enhancements

We love feature suggestions! Before suggesting:
- Check the [5-month roadmap](ACTIONLIST_5MONTH.md) - your idea might already be planned
- Search existing issues to see if someone else suggested it

**When suggesting an enhancement:**
- **Clear use case** - Explain why this feature is useful
- **Proposed solution** - Describe how it might work
- **Alternatives** - Any other approaches you considered

### Writing Documentation

Documentation improvements are always welcome:
- Fix typos or unclear explanations
- Add examples to make concepts clearer
- Translate documentation (if multilingual support is added)
- Write tutorials or guides

### Contributing Code

1. **Check existing issues** or create a new one discussing what you'd like to work on
2. **Fork the repository**
3. **Create a branch** for your feature: `git checkout -b feature/amazing-feature`
4. **Make your changes** following our coding standards
5. **Write tests** for your changes
6. **Ensure all tests pass**: `pytest`
7. **Submit a pull request**

---

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Git
- pip

### Setup Instructions

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/NeuroGlyph.git
cd NeuroGlyph

# 2. Create a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. Install in development mode with dev dependencies
pip install -e ".[dev]"

# 4. Install pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install

# 5. Run tests to verify setup
pytest
```

### Project Structure

```
NeuroGlyph/
├── parser/          # Parser implementation
├── engine/          # Runtime engine
├── ui/              # Visual interface specs
├── examples/        # Example .ng files
├── docs/            # Documentation
├── tests/           # Test files (to be created)
├── setup.py         # Package configuration
└── requirements.txt # Dependencies
```

---

## Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

- **Line length:** 100 characters (not 79)
- **Formatting:** Use `black` for automatic formatting
- **Linting:** Use `ruff` for linting
- **Type hints:** Use type hints for all public functions

### Code Quality Tools

```bash
# Format code with black
black neuroglyph/ tests/

# Lint code with ruff
ruff neuroglyph/ tests/

# Type check with mypy
mypy neuroglyph/

# Run all checks
black . && ruff . && mypy neuroglyph/
```

### Writing Good Code

**Do:**
- ✅ Write clear, descriptive variable names
- ✅ Add docstrings to all public functions and classes
- ✅ Keep functions small and focused (Single Responsibility Principle)
- ✅ Write unit tests for new functionality
- ✅ Handle errors gracefully with helpful error messages

**Don't:**
- ❌ Leave commented-out code
- ❌ Use obscure abbreviations
- ❌ Ignore linting warnings without good reason
- ❌ Submit code without tests

### Example: Good Function

```python
from typing import List, Optional

def parse_ng_tokens(text: str, strict: bool = False) -> List[NGToken]:
    """
    Parse NeuroGlyph tokens from text.

    Args:
        text: NeuroGlyph formatted text to parse
        strict: If True, raise exceptions on errors. If False, collect errors.

    Returns:
        List of parsed NGToken objects

    Raises:
        ParseError: If strict=True and parsing fails

    Example:
        >>> tokens = parse_ng_tokens("🚀 /act: reflect")
        >>> len(tokens)
        1
        >>> tokens[0].token_type
        'act'
    """
    # Implementation here
    ...
```

---

## Pull Request Process

### Before Submitting

1. **Update documentation** if you changed behavior
2. **Add tests** for new functionality
3. **Ensure all tests pass**: `pytest`
4. **Run code quality checks**: `black . && ruff . && mypy neuroglyph/`
5. **Update CHANGELOG.md** if applicable

### PR Title Format

Use clear, descriptive titles:

**Good:**
- `Fix: Parser crash on nested parentheses`
- `Feature: Add emoji validation to parser`
- `Docs: Add examples for modal logic tokens`

**Not ideal:**
- `Fix bug`
- `Update parser`
- `Changes`

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran to verify your changes.

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Related Issues
Fixes #123 (if applicable)
```

### Review Process

1. **Automated checks** will run (tests, linting)
2. **Maintainers review** your code
3. **Address feedback** if requested
4. **Approval** - Once approved, maintainers will merge

**Review timeline:** We aim to review PRs within 3-5 days.

---

## Issue Guidelines

### Issue Labels

We use labels to organize issues:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `priority: high` - Should be addressed soon
- `priority: low` - Nice to have but not urgent

### Issue Templates

When creating an issue, please use the appropriate template:

**For Bugs:**
- Bug report template (includes environment, steps to reproduce)

**For Features:**
- Feature request template (includes use case, proposed solution)

**For Questions:**
- Use GitHub Discussions instead of issues

---

## Community

### Communication Channels

- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - Questions, ideas, and general discussion
- **Pull Requests** - Code contributions and reviews

### Getting Help

- **Documentation:** Check [docs/](docs/) and [README.md](README.md)
- **Examples:** See [examples/](examples/) for usage patterns
- **Roadmap:** See [ACTIONLIST_5MONTH.md](ACTIONLIST_5MONTH.md) for planned features
- **Ask a question:** Open a GitHub Discussion

### Recognition

Contributors will be recognized in:
- **README.md** - Contributors section
- **CHANGELOG.md** - Release notes
- **GitHub contributors graph**

We truly appreciate all contributions, no matter how small! 🙏

---

## Development Roadmap

NeuroGlyph is following a [5-month development plan](ACTIONLIST_5MONTH.md):

- **Month 1:** Foundation & Package Structure
- **Month 2:** Core Parser & Validation
- **Month 3:** Runtime Engine & LLM Integration
- **Month 4:** Advanced Features & Testing
- **Month 5:** Polish & v1.0 Release

**Want to help?** Check the roadmap for tasks that need attention!

---

## Questions?

If you have questions about contributing, feel free to:
- Open a GitHub Discussion
- Comment on an existing issue
- Reach out to maintainers

**Thank you for contributing to NeuroGlyph!** 🚀

---

## Attribution

This Contributing Guide is adapted from:
- [Contributor Covenant](https://www.contributor-covenant.org/)
- [GitHub's Open Source Guides](https://opensource.guide/)
- Best practices from successful open-source projects

**License:** This document is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

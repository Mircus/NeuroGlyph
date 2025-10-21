"""
NeuroGlyph setup configuration
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / 'README.md'
long_description = readme_file.read_text(encoding='utf-8') if readme_file.exists() else ''

setup(
    name='neuroglyph',
    version='0.2.0',
    description='A symbolic communication protocol for structured multi-agent dialogue',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mirco and the NeuroGlyph collective',
    author_email='',  # Add email if desired
    url='https://github.com/Mircus/NeuroGlyph',
    license='MIT',

    packages=find_packages(exclude=['tests', 'docs', 'examples', 'notebooks']),

    install_requires=[
        'pydantic>=2.0.0',
        'pyyaml>=6.0',
        'regex>=2023.0.0',  # For better Unicode emoji support
    ],

    extras_require={
        'runtime': [
            'langchain>=0.1.0',
            'langchain-openai>=0.0.5',
            'langchain-anthropic>=0.1.0',
            'openai>=1.0.0',
            'anthropic>=0.18.0',
        ],
        'viz': [
            'networkx>=3.0',
            'matplotlib>=3.7.0',
            'graphviz>=0.20.0',
        ],
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'black>=23.0.0',
            'mypy>=1.5.0',
            'ruff>=0.1.0',
        ],
        'notebook': [
            'jupyter>=1.0.0',
            'ipywidgets>=8.0.0',
        ],
    },

    python_requires='>=3.9',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='ai, language, protocol, multi-agent, dialogue, symbolic',

    entry_points={
        'console_scripts': [
            'neuroglyph=neuroglyph.cli:main',  # Future CLI tool
        ],
    },

    include_package_data=True,
    zip_safe=False,
)

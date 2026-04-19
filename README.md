# Coding Agent Workshop: Data Analysis

Welcome to the Agentic Coding Workshop repository. This project is set up for to illustate the use of AI-assisted "agentic" development practices, focusing on a data analysis use case. ("Data analysis" spanning EDA to journal-quality figure production.)

## Overview

This repository demonstrates best practices for:
- Using GitHub Copilot in VS Code for code generation and assistance
- Organizing [Skills](GLOSSARY.md#using-coding-models) and [Agents](GLOSSARY.md#using-coding-models) for specialized workflows
- Collaborating with AI-powered coding tools

## Quick Start

See **[GettingStarted.md](./GettingStarted.md)** for setup instructions and first steps.

## Project Structure

```
.
├── .github/
│   ├── skills/              # Reusable skill modules
│   ├── agents/              # Custom agent configurations
│   └── copilot-instructions.md
├── .python-version          # Specifies Python 3.12+
├── .gitignore              # Excludes venv and build artifacts
├── README.md                # This file
├── GettingStarted.md        # Setup guide
└── requirements.txt         # Python dependencies
```

**Note:** The virtual environment is not included in the repository (excluded by `.gitignore`). Each user creates their own environment — see [GettingStarted.md](./GettingStarted.md) for setup instructions.

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [Agent Customization Guide](./.github/copilot-instructions.md)

## Contributing

When adding new skills or agents:
1. Create a subdirectory under `.github/skills/` or `.github/agents/`
2. Include a `SKILL.md` or `.agent.md` file with documentation
3. Update the relevant [instructions file](GLOSSARY.md#prompting-retrieval-context--instructions)

## License

This project is open source and available under the MIT License.

# Getting Started

This guide will help a user set up the Coding Agent Workshop on Data Analysis repository and use it to introduce various concepts relevant to AI-assisted code development in support of data analysis.

## Key Concepts
- Overall goals and guidelines for [Coding Agents](GLOSSARY.md#using-coding-models). See `.github/copilot-instructions.md`
- [Skills](GLOSSARY.md#using-coding-models): These are more detailed instructions that an agent should use for specific data analysis or coding tasks. Use skills to define specific task/processing steps for a coding agent. See `SkillsOveriew.md` for an overview of skills included in the repository. Skills can embed/use helper scripts that prescribe exactly how to perform steps, process a specific kind of data file, etc.
- [Custom Agents](GLOSSARY.md#using-coding-models): These are specialized agents that you can define to perform specific tasks. Custom agents are especially useful for workflows that require decisions (cannot be fully automated) but require specific, non-routine/non-obvious steps. 

## Prerequisites

- **VS Code** (latest version)
- **GitHub Copilot** extension installed and authenticated
- **Python 3.12+** (for running Python code in this repo)

## Setup Steps

### 1. Clone and Open the Repository

In a terminal (bash or zsh), open a directory where you want to install the repo. Then:

```bash
git clone https://github.com/wrayre/Agentic_Coding_Workshop.git
cd Agentic_Coding_Workshop
code .
```
`code` is the name of the VS Code program. This line tells VS Code to open in the current directory (`.`).

### 2. Create a Virtual Environment

If you already have python 3.12+ installed, create a Python 3.12+ virtual environment using that version of python:

```bash
python3 -m venv venv
```

If you do not have 3.12+ installed, we recommend using `uv` (faster than pip) to create a virtual environment with a custom version of python:

```bash
uv venv myvenv --python 3.12.9
```
This command will install a virtual environment called "myvenv" (change to whatever you want) and locally install the indicated version of python. (Note that `uv` does not automatically install `pip`.)

If you do not have uv installed: use `curl -LsSf https://astral.sh/uv/install.sh | sh` to install `uv`


### 3. Activate the Virtual Environment

```bash
source myvenv/bin/activate
```

On Windows:
```bash
myvenv\Scripts\activate
```

#### Check environment:

Check your version of python: 
```bash
which python
```
Generally, you should see the a path to an installation of python specific to the local environment. For example, I see:
`<full path to my project dir>/Agentic_Coding_Workshop/codagwksp/bin/python` (where codagwksp is the name of my virtual env.)


### 4. Install Dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```
OR (if using uv)

```bash
uv pip install -r requirements.txt
```

### 5. Configure VS Code

- Open VS Code if not already open
- Install the **GitHub Copilot** extension from the marketplace
- Sign in with your GitHub account
- Copilot will automatically detect the workspace customizations in `.github/` (which is where most of our work will focus in this workshop)

## Using the Workspace

### Copilot Instructions

The `.github/copilot-instructions.md` file provides workspace-level [System Prompt / Instructions](GLOSSARY.md#prompting-retrieval-context--instructions) guidance to Copilot. This will automatically be applied to all interactions in this workspace.

### Understanding Skills

[Skills](GLOSSARY.md#using-coding-models) are domain-specific workflows stored in `.github/skills/`. Each skill:
- Contains a `SKILL.md` file with approach and guidelines
- May include templates, examples, or helper scripts
- Can be referenced when working on related tasks

To use a skill:
1. Look for the relevant skill folder in `.github/skills/`
2. Read the `SKILL.md` file for guidance
3. Follow the recommended workflow or best practices

### Working with Agents

Custom agents in `.github/agents/` can be configured for specialized tasks. Check the individual agent files for their specific purposes and capabilities.

## Next Steps

1. Explore the skills in `.github/skills/`
2. Read individual skill files to understand domain-specific workflows
3. Check the project README for resources and additional documentation
4. Ask a coding model to perform EDA on one the data sets in the repository.

## Troubleshooting

**Copilot not appearing?**
- Ensure GitHub Copilot is installed and you're signed in
- Reload VS Code (Cmd+K, Cmd+Q on macOS)

**Virtual environment not activating?**
- Verify you have Python 3.12+: `python3 --version`
- Check that the venv was created successfully: `ls venv/bin/python`
- Try recreating: `rm -rf venv && python3 -m venv venv && source venv/bin/activate`

**Dependencies not installing?**
- Ensure the virtual environment is activated
- Run: `pip install --upgrade pip` first if using pip
- Check `requirements.txt` for syntax errors

Happy coding!

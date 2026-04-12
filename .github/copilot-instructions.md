# Copilot Instructions

This workspace is configured for agentic coding workflows. Refer to the documentation and skill files for guidance on specific tasks.

## Getting Started

- **[README.md](../README.md)** — Project overview
- **[GettingStarted.md](../GettingStarted.md)** — Setup and first steps

## Skills

Skills are located in `.github/skills/`. Each skill contains a `SKILL.md` file with specific workflows for domain tasks.

## Agents

Custom agents are located in `.github/agents/`. Agents can be configured for specialized, multi-step workflows.

## Repository Creation

You will provide guidance and support for the tutorial developers in creating the repository structure, including the `.github/` directory and its contents. This includes:
- Creating helper scripts and tools to support lesson development. The tutorial will focus on scikit-learn data sources and we will create some helper scripts to that create data directories for scikit-learn datasets to show users how to load and use various kinds of data. Helper scripts should be stored in `./scikit_learn_helpers/`.
- For each dataset you are asked to analyze, create a directory in the root with the name of the dataset followed by analysis. For instance, the `iris` dataset would have a directory called `iris_analysis/`. 
  - Every analysis directory should have an `output/` subdirectory where you will save any output files related to the analysis, such as markdown reports, visualizations, or processed data files. 
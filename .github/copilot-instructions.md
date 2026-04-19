# Copilot Instructions

This workspace is configured for data analysis workflows with AI assistance. Refer to the documentation and skill files for guidance on specific tasks.

## Getting Started

- **[README.md](../README.md)** — Project overview
- **[GettingStarted.md](../GettingStarted.md)** — Setup and first steps

## Custom Agents

Custom agents are located in `.github/agents/`. Each custom agent is configured for specialized, multi-step data analysis workflows. Agents are **user-directed**: the user explicitly invokes them for specific analysis tasks rather than operating autonomously.

## Skills

Skills are located in `.github/skills/`. Each skill contains a `SKILL.md` file with specific workflows for data analysis tasks. Custom agents reference and orchestrate these skills. Users can also reference skills directly for focused tasks. Users are welcome to add their own skills as needed for their analysis workflows (use the `skill-creator` skill to help with this).

## Analysis Scope

In-scope tasks include:
- Exploratory data analysis (EDA) and data loading
- Data preprocessing and cleaning
- Statistical analysis and testing
- Data visualization and charts
- Reporting and presentation of results
- Communicating findings via slides, summaries, or interactive outputs

All analysis-related work—from data exploration to communicating results—follows the structured directory organization outlined below.

## Repository Organization

This respository is intended to support users in various data analysis tasks using python (and python libraries such as pandas, numpy, matplotlib, seaborn, etc.). The repository is organized as follows:
- The root directory contains the main project files and directories.
- The `.github/` directory contains configuration files for GitHub Copilot and other repository-level settings, as well as subdirectories for skills and agents.
- The `.github/skills/` directory contains subdirectories for each skill, with each skill having its own `SKILL.md` file
- The `.github/agents/` directory contains subdirectories for each custom agent, with each agent having its own configuration file.
- The `./data/` directory contains subdirectories for each dataset of interest to the user. The user will create subdirectories for each dataset they want to analyze.
- Analysis for each dataset will be stored in a separate directory in the root. The directory for each dataset will be named with the dataset name followed by `_analysis`. For instance, the `iris` dataset would have a directory called `iris_analysis/`.
  - Each analysis directory will contain a `scripts/` subdirectory where any scripts related to the analysis will be stored. For instance, the `iris_analysis/` directory would contain a `scripts/` subdirectory for any scripts related to the analysis of the iris dataset. 
  - Each analysis directory will also contain a `processed-data/` subdirectory where any intermedite data products (pickle files, CSV files, etc.) generated for the analysis will be stored. For instance, the `iris_analysis/` directory would contain a `processed-data/` subdirectory for any data generated during the analysis of the iris dataset.
  - Each analysis directory will contain an `output/` subdirectory where any output files related to the analysis will be saved, such as markdown reports, visualizations, or processed data files. For instance, the `iris_analysis/` directory would contain an `output/` subdirectory for all output files related to the analysis of the iris dataset.
    - Each `output/` subdirectory will contain a `reports/` subdirectory where any markdown summaries generated for the analysis will be stored. 
    - Each `output/` subdirectory will contain a `charts/` subdirectory where any visualizations generated for the analysis will be stored.
    - Each `output/` subdirectory will contain a `slides/` subdirectory where any PPT or PDF slides generated for the analysis will be stored.
  - Each analysis directory should include a `tmp/` subdirectory for any temporary files generated during the analysis, such as intermediate outputs or logs. The `tmp/` subdirectory can be cleaned up after the analysis is complete to remove any unnecessary files.

## Workflow for Analysis of a Dataset

With the exception of subagents, this respository is intended to support user-directed analysis of data. The user will select a dataset of interest and then direct codings agent to perform specific tasks to support that analysis, including initial planning for an analysis, initial data loading and exploratory data analysis, data preprocessing, statistical analysis, visualization, and presentation of results. The user will also have the option to perform any of these steps themselves without the use of an agent, if they prefer.

## Rules for Maintaining Repository Organization
These rules should always be followed, regardless of the specific dataset being analyzed or the specific tasks being performed. The rules are as follows:
1. The coding agent should NEVER modify or remove any files in the `./data/` directory. The `./data/` directory is intended to be a read-only directory that contains the original datasets. Any data processing or analysis should be performed in the corresponding analysis directory, not in the `./data/` directory. (The user will be responsible for adding datasets to the `./data/` directory, but once a dataset is added, the coding agent should not modify or remove any files in that directory.)
2. For each dataset analyzed, create a directory in the root with the name of the dataset followed by `_analysis`. For instance, the `iris` dataset would have a directory called `iris_analysis/`. When creating the analysis directory, also create all the subdirectories as outlined above.
3. All scripts related to the analysis of a dataset should be stored in the `scripts/` subdirectory of the corresponding analysis directory. For instance, any scripts related to the analysis of the `iris` dataset should be stored in the `iris_analysis/scripts/` subdirectory.
4. All intermediate data products generated during the analysis of a dataset should be stored in the `processed-data/` subdirectory of the corresponding analysis directory. For instance, any intermediate data products generated during the analysis of the `iris` dataset should be stored in the `iris_analysis/processed-data/` subdirectory.
5. All temporary files generated during the analysis of a dataset should be stored in the `tmp/` subdirectory of the corresponding analysis directory. For instance, any temporary files generated during the analysis of the `iris` dataset should be stored in the `iris_analysis/tmp/` subdirectory. The `tmp/` subdirectory can be cleaned up after the analysis is complete to remove any unnecessary files. The user may choose to keep some temporary files if they think they will be useful for future reference, but the agent should not keep any temporary files that are not likely to be useful for future reference.
6. All output files related to the analysis of a dataset should be saved in the `output/` subdirectory of the corresponding analysis directory. Put outputs files in the appropriate subdirectory of `output/` based on the type of output. 
7. Unless otherwise specified by the user, output files should generally be descriptive of the type of the analysis and include the date of creation in the name. Long, descriptive names are preferred over short names or abbreviations. For instance, a markdown report summarizing the results of an analysis of the `iris` dataset created on June 1, 2024 might be named `iris_analysis_report_2024-06-01.md` and would be stored in the `iris_analysis/output/reports/` subdirectory. 
8. The agent should never save any output files to the root directory or to any directory other than the `output/` subdirectory of the corresponding analysis directory. All output files should be organized within the appropriate analysis directory, not in the root or in any other directory.

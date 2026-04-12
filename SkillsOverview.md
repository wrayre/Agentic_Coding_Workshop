# Skills Overview

Skills are domain-specific workflows and best practices bundled with this repository. Each skill provides detailed guidance, templates, and helper scripts for specific coding tasks or problem domains.

## What Are Skills?

Skills help Copilot understand how to approach specific types of work in this repository. When you're working on a task that matches a skill's domain, the skill automatically loads relevant guidance—ensuring consistent, high-quality approaches across your codebase.

Each skill contains:
- **Best practices** for the task domain
- **Step-by-step workflows** 
- **Code templates** (where applicable)
- **Helper scripts** for specialized operations
- **Common pitfalls** and how to avoid them

## How to Use Skills

1. **Look for the relevant skill** — Find the skill that matches your current task
2. **Read the `SKILL.md` file** — Each skill has detailed documentation in `.github/skills/<skill-name>/SKILL.md`
3. **Follow the recommended workflow** — Use the step-by-step guidance in the skill
4. **Reference templates and scripts** — Skills often include reusable code or helper scripts

## Available Skills

Skills are located in `.github/skills/`. Current skills include:

### Data Analysis & Visualization

- **Exploratory Data Analysis** — Comprehensive analysis of scientific data files across 200+ formats. Automatically detects file types and generates detailed markdown reports with format-specific analysis, quality metrics, and downstream recommendations. Covers chemistry, bioinformatics, microscopy, spectroscopy, proteomics, and metabolomics.

- **Matplotlib** — Low-level plotting library for full customization of visualizations. Use when you need fine-grained control over plot elements, creating novel plot types, or integrating with specific scientific workflows. Export to PNG/PDF/SVG for publication.

- **Statistical Analysis** — Guided statistical analysis with test selection and reporting. Helps choose appropriate tests, check assumptions, perform power analysis, and generate APA-formatted results for academic research.

### Presentations & Documentation

- **PPTX** — Comprehensive PowerPoint skill for creating, reading, editing, or modifying presentations. Use for decks, pitch presentations, extracting content, or working with templates and layouts.

### Specialized Tools

- **PubMed Database** — Direct REST API access to PubMed with advanced Boolean/MeSH queries, E-utilities API, batch processing, and citation management. For Python workflows, integrates with BioPython.

- **Skill Creator** — Create new skills, modify and improve existing ones, and measure skill performance. Includes evaluation tools, benchmarking with variance analysis, and description optimization for better triggering accuracy.

## Adding a New Skill

There are three obvious ways to add a new skill to your project:
1. Write a new skill yourself. 
- This could be a good choice if you already have helper sripts and references you want the coding agent to use for your dataset. 
2. Download an existing skill someone else created
- There are 1000s of skills available. See https://skills.sh for one very large connection.
- If you use skills from others, carefully read thru them to guard against prompt injection attacks. Skills.sh includes some helpful assessments of a skill, but, as always for anything you download on the internet, caveat emptor!
3. Use a coding model to write a skill. The repo includes a `skill-creator` skill that can guide a coding model to write a new skill. Very meta. Check what it produces!

To contribute a new skill to this project:

1. Create a directory with the name of the skill: `.github/skills/<skill-name>/`
2. Add a `SKILL.md` file with:
   - Appropriate header (see other skills for examples)
   - Clear description of when to use the skill
   - Step-by-step workflow guidance
   - Any templates, examples, or helper scripts
3. Include helper scripts (Python, shell, etc.) in the skill folder
4. Update this file to list the new skill
5. (Optional) Add a README.md for additional context

Example structure:
```
.github/skills/my-skill/
├── SKILL.md              # Main documentation
├── README.md             # (Optional) Additional context
├── template.py           # (Optional) Code template
└── helper-script.py      # (Optional) Utility script
```

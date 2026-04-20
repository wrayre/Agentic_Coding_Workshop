import os
import time
# use pip or uv to install python-dotenv, dspy, and requests before running this code
import requests

# DSPy is a framework for building agents that can use tools and interact with language models.
# This code defines a ReAct agent that answers questions about gene-function associations by searching Wikipedia.
# ReAct is a prompting technique that encourages the agent to interleave reasoning steps with tool calls, 
# allowing it to iteratively gather information and refine its answer.
import dspy
from dotenv import load_dotenv

# DEBUGGING FLAGS
track_timing = False # Whether to print timing for each major step (agent creation, each question)
trace_debug = False  # Whether to print detailed search logs for each question
show_history = False  # Whether to print the full agent history after each question. Set to True to see the full reasoning trace, including intermediate steps and tool calls.
    
start_total = time.time()
start = time.time()

# Load environment variables from .env file
load_dotenv()

# This program requires an API key to a language model.
# You can set this in a .env file in the same directory with a line like:
# OPENAI_API_KEY=sk-abc123...
# Use environment variables for the model key to avoid hardcoding it in the code
project_key = os.getenv("OPENAI_API_KEY")

# Define a typed signature for gene-function lookup
class GeneFunctionQA(dspy.Signature):
    """Given a human biological function, use Wikipedia search results to identify the gene most
    associated with it. First, search Wikipedia and then reason over the results. 
    For search, do not assume or name a gene before searching. Search using only the biological function description, 
    then identify the gene from what the results return. For reasoning/results: if you identified a gene
    during your search steps, set found=True and populate the other fields.
    Set found=False only if the search failed entirely or returned no information relevant to
    any gene associated with the biological function."""

    biological_function: str = dspy.InputField(
        desc="A human biological function or process (e.g., 'regulation of blood sugar levels')"
    )
    found: bool = dspy.OutputField(
        desc="True if your search steps identified a gene associated with the function; False only if all searches failed or returned completely irrelevant results"
    )
    gene: str = dspy.OutputField(
        desc="The HGNC gene symbol most associated with the biological function (e.g., 'INS', 'BRCA1'); empty string if found=False"
    )
    rationale: str = dspy.OutputField(
        desc="Short, 1-2 sentence explanation of why this gene is associated with the biological function; empty string if found=False"
    )
    citation: str = dspy.OutputField(
        desc="The journal/publication cited for the gene-function association; empty string if found=False"
    )


# Tracks search outcomes within each agent call (reset per question)
_search_log: list[str] = []


# Wikipedia REST API endpoint for page summaries
_WIKI_API = "https://en.wikipedia.org/w/api.php"
# Wikipedia policy requires a descriptive User-Agent to avoid 403 rejections
_WIKI_HEADERS = {"User-Agent": "DSPyExploration/1.0 (gene-function research; github.com/DSPyExploration)"}


# Define a simple search tool
def search(query: str) -> str:
    """Search Wikipedia for information about a gene or biological function.

    Args:
        query: The search query

    Returns:
        Search results as a string, or a message indicating no results were found
    """
    try:
        # Step 1: find the top matching page titles
        search_resp = requests.get(
            _WIKI_API,
            headers=_WIKI_HEADERS,
            params={
                "action": "query",
                "list": "search",
                "srsearch": query,
                "srlimit": 3,
                "format": "json",
            },
            timeout=10,
        )
        search_resp.raise_for_status()
        hits = search_resp.json().get("query", {}).get("search", [])

        if not hits:
            _search_log.append(f"[query={query!r}] empty results: Wikipedia returned no matches")
            return "NO_RESULTS: Wikipedia search returned no results for this query."

        # Step 2: fetch plain-text extracts for each matching page
        titles = "|".join(h["title"] for h in hits)
        extract_resp = requests.get(
            _WIKI_API,
            headers=_WIKI_HEADERS,
            params={
                "action": "query",
                "titles": titles,
                "prop": "extracts",
                "exintro": True,
                "explaintext": True,
                "format": "json",
            },
            timeout=10,
        )
        extract_resp.raise_for_status()
        pages = extract_resp.json().get("query", {}).get("pages", {}).values()
        texts = [p.get("extract", "") for p in pages if p.get("extract")]

        if not texts:
            _search_log.append(f"[query={query!r}] empty results: pages found but no extract text")
            return "NO_RESULTS: Wikipedia pages found but contained no readable text."

        _search_log.append(f"[query={query!r}] success: {len(texts)} page(s) returned")
        # Trim each extract to 2000 chars to give the model enough context
        return " ".join(t[:2000] for t in texts)

    except Exception as e:
        _search_log.append(f"[query={query!r}] exception: {type(e).__name__}: {e}")
        return f"NO_RESULTS: Search failed ({e}). Do not guess; set found=False."


# Configure DSPy with the project key and nano model
start = time.time()
dspy.configure(lm=dspy.LM("openai/gpt-5.4-nano", api_key=project_key))
if track_timing:   
    print(f"Time to configure DSPy: {time.time() - start:.2f} seconds")

# Create a ReAct agent with the search tool
start = time.time()
agent = dspy.ReAct(
    signature=GeneFunctionQA,
    tools=[search],
    max_iters=5
)
if track_timing:
    print(f"Time to create ReAct agent: {time.time() - start:.2f} seconds")

# Test the agent
questions = [
    "regulation of blood sugar levels",
    "variation in human height",
    "contribution to obesity",
]

for biological_function in questions:
    _search_log.clear()
    start = time.time()
    print("\n--- Gene Function Lookup ---")
    print(f"Biological function: {biological_function}")
    result = agent(biological_function=biological_function)
    if track_timing:
        print(f"Time to run ReAct agent: {time.time() - start:.2f} seconds")   
    if trace_debug:
        print(f"Search calls ({len(_search_log)}):")
        for entry in _search_log:
            print(f"  {entry}")
    if result.found:
        print(f"Gene:      {result.gene}")
        print(f"Rationale: {result.rationale}")
        print(f"Citation:  {result.citation}")
    else:
        print("Result:    No Wikipedia evidence found for this biological function.")
    if show_history:
        print(dspy.inspect_history())
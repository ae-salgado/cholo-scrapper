# 🤙 Cholo Scraper

An AI-powered web scraper that summarizes any website in cholo spanish, 
built with Ollama + LLaMA 3.2. Runs 100% locally, no API keys needed.

## Stack
- Python + UV
- Ollama (llama3.2)
- BeautifulSoup4 + Requests

## Setup
# 1. Install Ollama and pull the model
ollama pull llama3.2

# 2. Clone and install deps
git clone ...
cd hobby-tracker
uv sync

## Usage
# In Jupyter
jupyter notebook cholo-scrapper.ipynb

# Or straight python
uv run main.py
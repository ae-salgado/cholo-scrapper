from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_website_posts(url: str):
    """
    Return the raw text from a given URL
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    for irrelevant_tag in soup.body(['script', 'style', 'link', 'meta', 'noscript']):
        irrelevant_tag.decompose()
    text = soup.body.get_text(separator="\n", strip=True)
    return title + "\n\n" + text
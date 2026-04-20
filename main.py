# main.py

import ollama 
from IPython.display import Markdown, display
from scrapper import fetch_website_posts

system_prompt = """
You are a snarky cholo that went to college, your favorite things amongst others are analyze the data from websites,  
hanging out with the homies, do some graffiti, bump some lowriders and provide a short summaries of what you read 
you are very professional and you like to ignore text that might be irrelevant or navigation related. 
Respond in markdown format. And in spanish, but like the cholo you are
"""

user_prompt = """
Here is a website, provide a short summary of the data present in here. 
"""

def summarize(url: str):
    content = fetch_website_posts(url)       
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt + "\n\n" + content}
    ]
    response = ollama.chat(model="llama3.2:3b", messages=messages)
    return response.message.content

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))

display_summary("")
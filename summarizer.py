import requests
from bs4 import BeautifulSoup
import config
import openai

#add your api key here or in config.py file you creat
# openai.api_key = ''

def extract_content(url):
    article = ''
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article = ' '.join([p.text for p in soup.find_all('p')])
    except:
        pass
    return article

def chatGPT(userinput,temperature=1,max_tokens=300, words = 100): 
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo', 
        messages= [{"role":"user","content": f"Please provide a summary of the following text in about {words} words or less:" + userinput}],
        temperature=temperature, 
        max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']
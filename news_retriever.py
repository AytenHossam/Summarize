import requests
import os
from dotenv import load_dotenv

load_dotenv()  

class NewsRetriever:
    def __init__(self):
        self.api_key = "31e59b1754444852bd181e01a065be54"
        self.base_url = "https://newsapi.org/v2/everything"

    def fetch_articles(self, topic, page_size=5):
        params = {
            "q": topic,
            "apiKey": self.api_key,
            "pageSize": page_size,
            "language": "en"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json().get("articles", [])
        else:
            raise Exception("Failed to fetch articles. Check your API key and internet connection.")

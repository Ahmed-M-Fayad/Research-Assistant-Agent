"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment configuration
config_path = "configs/.env"
load_dotenv(config_path)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="nvidia/nemotron-nano-9b-v2:free",   # You can swap this for any available model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! How are you?"}
    ]
)

for msg in response.choices[0].message
    print(choice)
"""

from newsapi import NewsApiClient

client = NewsApiClient(api_key="cb1ad0e60f314d2b87044da82576e850")

articles = client.get_everything(q="Quantum Mechanics", language="en", sort_by="relevancy")
if not articles["articles"]:
    print("❌ No articles found for this query.")

formatted_results = []
for article in articles["articles"][:5]:
    print("source:", article["source"]["name"])
    print("title:", article.get("title"))
    print("url:", article.get("url"))

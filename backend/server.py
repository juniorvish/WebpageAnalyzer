import requests
from bs4 import BeautifulSoup
import openai
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = "your_openai_api_key"

def get_response(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    truncated_text = text[:6000]

    prompt = f"From the below given data tell what does this company do?{truncated_text}"
    message = [
        {"role": "system", "content": "You are a friendly AI Developer"},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=0.2,
        max_tokens=4000,
        frequency_penalty=0.9
    )

    gpt_message = response.choices[0].message.content
    return gpt_message.strip()

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    url = data["url"]
    company_description = get_response(url)
    return jsonify({"companyDescription": company_description})

if __name__ == "__main__":
    app.run()
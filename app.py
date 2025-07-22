import webbrowser
import threading
from flask import Flask, request, jsonify, session, render_template
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "studivize-secret")
CORS(app)

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gemini", methods=["POST"])
def gemini():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        present_country = data.get("presentCountry")
        gpa = data.get("gpa")
        target_country = data.get("country")
        purpose = data.get("purpose")

        prompt = f"""
        Hello AI, I am {name} from {present_country}. I want to study in {target_country}.
        My GPA is {gpa}. My purpose of studying abroad is {purpose}.
        Based on this, please provide:
        1. 🎓 Top universities in {target_country} **with their official website links** (in the format: University Name - https://example.edu).
        2. 💰 Scholarships available for students from {present_country}.
        3. 🛤️ A detailed, month-wise personalized roadmap to achieve my study abroad dream.
        Format each section clearly.
        """
       
        payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful career guidance assistant."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]

        # Split into sections using regex
        def split_sections(text):
            sections = {"universities": "", "scholarships": "", "steps": ""}
            parts = re.split(r'\d+\.\s+', text)
            if len(parts) >= 4:
                sections["universities"] = parts[1].strip()
                sections["scholarships"] = parts[2].strip()
                sections["steps"] = parts[3].strip()
            return sections

        session["roadmap"] = split_sections(reply)
        session["name"] = name

        return jsonify({"redirect": "/roadmap"})

    except Exception as e:
        return jsonify({"error": "Failed to generate response", "details": str(e)}), 500

@app.route("/roadmap")
def roadmap():
    roadmap_data = session.get("roadmap", {})
    name = session.get("name", "Student")
    return render_template("roadmap.html", roadmap=roadmap_data, name=name)

if __name__ == "__main__":
    threading.Timer(1.2, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=True)


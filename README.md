# 🌍 Studivize: AI-Powered Study Abroad Roadmap Generator

Studivize is a smart, AI-powered web application that helps students from any country generate a personalized roadmap to study abroad. It provides:

- 🎓 Top university recommendations
- 💰 Scholarships based on your background
- 🛤️ A detailed, month-wise study abroad roadmap

All based on your country, GPA, and goals.

---

## 🚀 Features

- Built using **Flask** + **HTML/CSS/JS**
- Uses **OpenRouter AI (GPT-3.5)** to generate intelligent responses
- Students get:
  - University list with clickable website links
  - Scholarships relevant to their country
  - Personalized month-wise preparation plan
- Mobile and desktop responsive layout
- Clean UI with clear sectioning of results

---
STUDIVIZE SCREENSHOTS:
![Studivize Screenshot](https://github.com/PRANAYPIPPOJI/Studivize/blob/main/Screenshot%202025-07-26%20203309.png?raw=true)
![Studivize Screenshot]


## 🔧 Technologies Used

- Python (Flask)
- HTML, CSS, JavaScript
- OpenRouter AI API
- dotenv for environment management

---

## 🛠️ Setup Instructions

1. Clone this repository  
   `git clone https://github.com/your-username/studivize.git`

2. Navigate to the project folder  
   `cd studivize`

3. Install required Python packages  
   `pip install -r requirements.txt`

4. Create a `.env` file and add your OpenRouter API key:
    OPENROUTER_API_KEY=your_api_key_here
    FLASK_SECRET_KEY=any_random_secret

5. Run the app  
`python app.py`

6. Open in browser:  
`http://127.0.0.1:5000`

---

## 📁 Folder Structure
studivize/
│
├── templates/
│ ├── index.html
│ └── roadmap.html
│
├── static/
│ ├── (Optional: Add CSS/JS files here)
│
├── app.py
├── .env
├── .gitignore
└── README.md


---

🌐 For Users
To run Studivize on your system:

You must create your own .env file

Get your own OpenRouter API key from
👉 https://openrouter.ai

Without your API key, the AI responses will not work.

## 👤 Author

**Pranay Pippoji**  
Connect on [LinkedIn](https://linkedin.com/in/pranay-pippoji-855979297)

---

## 📝 License

This project is open-source and free to use.

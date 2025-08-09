# 📅 AI Study Planner

An AI-powered tool that predicts your focus level based on your study schedule and energy levels, and optionally schedules optimal study sessions directly into your Google Calendar.

## 🚀 Features
- Predicts **focus level** using a machine learning regression model.
- Interactive **Streamlit** web interface.
- Integrates with **Google Calendar API** to auto-schedule study sessions.
- Dataset of **300 days** of study patterns for model training.
- Simple, beginner-friendly ML workflow.

---

## 🛠 Tech Stack
- **Python**
- **Pandas**, **Scikit-learn**
- **Streamlit** for the web app
- **Google Calendar API**
- **Joblib** for model saving/loading

---

## 📂 Project Structure
AI-Study-Planner/
│
├── data/
│ └── study_data_300_days.csv # Dataset used for training
│
├── app.py # Model training script
├── calendar_helper.py # Google Calendar helper functions
├── requirements.txt # Python dependencies
├── streamlit_app.py # Main Streamlit app
├── study_planner_model.pkl # Trained ML model
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation & Setup

1️⃣ **Clone this repository**
```bash
git clone https://github.com/YOUR_USERNAME/AI-Study-Planner.git
cd AI-Study-Planner
2️⃣ Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
3️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the app

bash
Copy
Edit
streamlit run streamlit_app.py
🔑 Google Calendar API Setup
To enable Google Calendar integration:

Go to Google Cloud Console.

Create a new project & enable Google Calendar API.

Create OAuth 2.0 credentials and download credentials.json.

Place credentials.json in your local project folder (DO NOT commit to GitHub).

The first time you run the app and add an event, it will ask for Google login & create token.json.

📊 Model Information
The ML model is a Linear Regression model trained on:

Start Hour

End Hour

Energy Level (1–5)

Output: Predicted Focus Level (1–5).

⚠️ Security Notes
DO NOT upload credentials.json or token.json to GitHub.

Use Streamlit Secrets Manager for deployment to store API keys securely.

📸 Demo
(Add a screenshot or GIF of your app here)

📜 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

If you want, I can also make a **shorter GitHub-friendly version** with an image preview so it looks good at the top of your repo page.  
Do you want me to prepare that too?

from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

# ===== MASTER POOLS FOR EACH CATEGORY =====
MASTER_POOL = {
    "Geography": [
        "China","India","USA","Indonesia","Pakistan","Brazil","Nigeria","Bangladesh",
        "Russia","Mexico","Canada","Chile","Cameroon","Curacao","Croatia"
    ],
    "History": [
        "WWII","Napoleon","Genghis Khan","French Revolution","Industrial Revolution",
        "Renaissance","Cold War","American Revolution","Roman Empire","Mongol Empire",
        "Caesar","Cleopatra","Churchill","Charlemagne","Civil War"
    ],
    "General Knowledge": [
        "Mount Everest","K2","Kangchenjunga","Lhotse","Makalu","Cho Oyu","Dhaulagiri",
        "Manaslu","Nanga Parbat","Annapurna","Cheetah","Compass","Celsius","Carbon","Canberra"
    ],
    "Soccer": [
        "Lionel Messi","Cristiano Ronaldo","Luis Suarez","Andres Iniesta","Xavi Hernandez",
        "Ronaldinho","Zlatan Ibrahimovic","Paolo Maldini","Thierry Henry","Francesco Totti",
        "Neymar","Mbappe","Cafu","Cantona","Casillas"
    ],
    "American Football": [
        "Tom Brady","Drew Brees","Peyton Manning","Brett Favre","Ben Roethlisberger",
        "Matt Ryan","Dan Marino","Eli Manning","John Elway","Troy Aikman","Terrell Owens",
        "Tony Gonzalez","Cam Newton","Christian McCaffrey"
    ]
}

# ===== QUESTIONS PER CATEGORY =====
CATEGORY_QUESTIONS = {
    "Geography": "Name the top 10 countries by population.",
    "History": "Name the top 10 most significant historical events.",
    "General Knowledge": "Name the top 10 highest mountains or famous facts.",
    "Soccer": "Name the top 10 footballers of all time.",
    "American Football": "Name the top 10 NFL players by career stats."
}

# ===== FUNCTION TO GENERATE TOP 10 PER CATEGORY FOR TODAY =====
def generate_daily_questions():
    daily_questions = {}
    for category, pool in MASTER_POOL.items():
        daily_questions[category] = random.sample(pool, 10)
    return daily_questions

# ===== ROUTE =====
@app.route("/", methods=["GET", "POST"])
def home():
    date_str = datetime.now().strftime("%Y-%m-%d")
    questions = generate_daily_questions()
    categories = list(questions.keys())

    selected_category = request.form.get("category", categories[0])
    top_ten = questions.get(selected_category, [])
    question_text = CATEGORY_QUESTIONS.get(selected_category, f"Name the top 10 {selected_category}")

    return render_template(
        "index.html",
        categories=categories,
        selected_category=selected_category,
        top_ten=top_ten,
        current_date=date_str,
        question_text=question_text
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)






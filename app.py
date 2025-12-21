from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

# Load all questions once
with open("questions.json", "r") as f:
    all_questions = json.load(f)

def get_today_questions():
    """Return the questions for today based on the current date."""
    today_str = datetime.now().strftime("%Y-%m-%d")
    if today_str in all_questions:
        return all_questions[today_str]
    else:
        # If today's date not in JSON, return last available day
        last_date = sorted(all_questions.keys())[-1]
        return all_questions[last_date]

@app.route("/", methods=["GET", "POST"])
def home():
    today_questions = get_today_questions()
    categories = list(today_questions.keys())
    selected_category = request.form.get("category", categories[0])  # Default to first category

    top_ten = today_questions.get(selected_category, [])

    return render_template(
        "index.html",
        categories=categories,
        selected_category=selected_category,
        top_ten=top_ten
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)



from flask import Flask, render_template, request
from datetime import date
import json

app = Flask(__name__)

# Load daily questions from JSON file
with open("questions.json") as f:
    daily_answers = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    today_str = str(date.today())  # e.g., "2025-12-21"
    today_questions = daily_answers.get(today_str)

    # If no questions are set for today, show a message
    if not today_questions:
        return "<h2>No questions set for today. Please check back later.</h2>"

    result = []
    selected_category = None
    correct_count = 0

    if request.method == "POST":
        selected_category = request.form.get("category")
        # Get user's 10 answers
        user_answers = [request.form.get(f"answer{i}", "").strip() for i in range(1, 11)]
        correct_answers = today_questions.get(selected_category, [])
        
        # Compare user's answers with correct answers
        for i in range(10):
            correct = user_answers[i].lower() == correct_answers[i].lower()
            if correct:
                correct_count += 1
            result.append({
                "your_answer": user_answers[i],
                "correct_answer": correct_answers[i],
                "correct": correct
            })

    return render_template(
        "index.html",
        categories=list(today_questions.keys()),
        result=result,
        selected_category=selected_category,
        correct_count=correct_count
    )

if __name__ == "__main__":
    app.run()


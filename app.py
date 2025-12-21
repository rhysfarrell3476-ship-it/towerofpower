from flask import Flask, render_template, request
import json
from datetime import datetime, timedelta

app = Flask(__name__)

# Load all questions once
with open("questions.json", "r") as f:
    all_questions = json.load(f)

# Sort dates for easier navigation
sorted_dates = sorted(all_questions.keys())

def get_questions_by_date(date_str):
    """Return questions for a given date string, or last available if not found."""
    if date_str in all_questions:
        return all_questions[date_str]
    else:
        return all_questions[sorted_dates[-1]]

@app.route("/", methods=["GET", "POST"])
def home():
    # Default number of lives
    lives = 3

    # Get current date or date from form (for Next Day preview)
    date_str = request.form.get("date", datetime.now().strftime("%Y-%m-%d"))
    
    # Convert to index in sorted_dates for navigation
    try:
        current_index = sorted_dates.index(date_str)
    except ValueError:
        current_index = -1  # Default to last date if not found

    # Check if "Next Day" button was clicked
    if "next_day" in request.form:
        current_index = (current_index + 1) % len(sorted_dates)
        date_str = sorted_dates[current_index]

    questions = get_questions_by_date(date_str)
    categories = list(questions.keys())
    selected_category = request.form.get("category", categories[0])  # Default to first category
    top_ten = questions.get(selected_category, [])

    return render_template(
        "index.html",
        categories=categories,
        selected_category=selected_category,
        top_ten=top_ten,
        current_date=date_str,
        lives=lives  # <-- Add this line to fix the template error
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)





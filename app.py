from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined answers for simplicity
answers = {
    "Geography": ["China", "India", "USA", "Indonesia", "Brazil", "Pakistan", "Nigeria", "Bangladesh", "Russia", "Mexico"],
    "History": ["WWII", "Napoleon", "Genghis Khan", "French Revolution", "Industrial Revolution", "Renaissance", "Cold War", "American Revolution", "Roman Empire", "Mongol Empire"],
    "General Knowledge": ["Earth", "Water", "Sun", "Moon", "Oxygen", "Python", "Elephant", "Mount Everest", "Amazon", "Gravity"],
    "Soccer": ["Messi", "Ronaldo", "Pele", "Maradona", "Neymar", "Mbappe", "Zidane", "Beckham", "Ronaldinho", "Kane"],
    "American Football": ["Tom Brady", "Patrick Mahomes", "Joe Montana", "Jerry Rice", "Lawrence Taylor", "Peyton Manning", "Aaron Rodgers", "Jim Brown", "Reggie White", "Emmitt Smith"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    selected_category = None
    correct_count = 0

    if request.method == "POST":
        selected_category = request.form.get("category")
        user_answers = []
        for i in range(1, 11):
            answer = request.form.get(f"answer{i}", "").strip()
            user_answers.append(answer)
        correct_answers = answers.get(selected_category, [])
        result = []
        for i in range(10):
            correct = user_answers[i].lower() == correct_answers[i].lower()
            if correct:
                correct_count += 1
            result.append({"your_answer": user_answers[i], "correct_answer": correct_answers[i], "correct": correct})

    return render_template("index.html", categories=list(answers.keys()), result=result, selected_category=selected_category, correct_count=correct_count)

if __name__ == "__main__":
    app.run()


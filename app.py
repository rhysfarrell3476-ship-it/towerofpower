from flask import Flask, render_template, request

app = Flask(__name__)

def word_pyramid_logic(word):
    return [word[:i+1] for i in range(len(word))]

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        word = request.form.get("word", "").strip().upper()
        if word:
            result = word_pyramid_logic(word)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()

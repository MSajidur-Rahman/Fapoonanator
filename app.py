from flask import Flask, request, render_template
from Fapoonanator import fapoonanator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        word1 = request.form["word1"]
        word2 = request.form["word2"]
        result = fapoonanator(word1, word2)
    return render_template("home.html", result=result)

if __name__ == "__main__":
    app.run()


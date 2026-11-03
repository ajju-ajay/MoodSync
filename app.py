from flask import Flask, render_template, request
from recommender import recommend_songs

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    selected_emotion = ""
    selected_language = "All"

    if request.method == "POST":

        selected_emotion = request.form.get("emotion", "")
        selected_language = request.form.get("language", "All")

        recommendations = recommend_songs(
            selected_emotion,
            selected_language
        )

    return render_template(
        "index.html",
        recommendations=recommendations,
        selected_emotion=selected_emotion,
        selected_language=selected_language
    )


if __name__ == "__main__":
    app.run(debug=True)
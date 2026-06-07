from flask import Flask, render_template, request
from sentiment_utils import get_youtube_comments, analyze_sentiment

app = Flask(__name__)

API_KEY = "AIzaSyBJk_hrKiiA11qckKs2UUy_jVMsVRRlD18"

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    video_id = ""

    if request.method == "POST":
        video_id = request.form.get("video_id", "").strip()
        if video_id:
            comments = get_youtube_comments(video_id, API_KEY, 50)  
            results = [(c, analyze_sentiment(c)) for c in comments]

    return render_template("index.html", results=results, video_id=video_id)

if __name__ == "__main__":
    app.run(debug=True) 
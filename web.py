from flask import Flask, jsonify, render_template, request

from app import fetch_scores

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/api/scores")
def api_scores():
    days = int(request.args.get("days", 1))
    try:
        games = fetch_scores(days=days)
    except Exception as e:
        return jsonify({"error": str(e)}), 502
    return jsonify(games)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

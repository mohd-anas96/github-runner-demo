from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Home - GitHub Actions CI/CD"

@app.route("/about")
def about():
    return "About CI/CD and AWS"

@app.route("/contact")
def contact():
    return "Contact Page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

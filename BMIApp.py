from flask import Flask, render_template
BMI_app = Flask(__name__)

@BMI_app.route("/")
@BMI_app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    BMI_app.run(debug=True)


def home():
    return "Hello, World!"
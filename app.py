from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data["code"]

    try:
        result = subprocess.check_output(
            ["python", "-c", code], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        result = e.output

    return jsonify({"output": result})


if __name__ == "__main__":
    app.run(debug=True)

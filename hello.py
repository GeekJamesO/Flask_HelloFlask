from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_work():
    return "Hello World from James."

app.run(debug=True)

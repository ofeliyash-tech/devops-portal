from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Portal</h1>
    <p>Welcome to my DevOps project!</p>
    <p>Learn. Practice. Improve.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

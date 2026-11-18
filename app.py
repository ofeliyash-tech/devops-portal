from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <body style="background:#0f172a;
                 color:white;
                 text-align:center;
                 font-family:Arial;
                 padding:80px;">
        <h1 style="color:#38bdf8;">DevOps Portal</h1>
        <h2>Welcome to my DevOps project!</h2>
        <p>Learn. Practice. Improve.</p>
        <p>Docker | Git | GitHub | CI/CD</p>
    </body>
    """
@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


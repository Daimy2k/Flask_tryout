from flask import Flask

app= Flask(__name__)

@app.route("/")
def hello():
    return "<p>Dit is een test.</p> "

if __name__ == '__main__':
    app.run(debug=True)
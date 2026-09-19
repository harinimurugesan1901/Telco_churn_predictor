from flask import Flask
app = Flask("test")

@app.route('/')
def home():
    return "<h1>Website Working Bro!</h1>"

app.run(debug=True)
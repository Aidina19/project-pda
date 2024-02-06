import time
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route('/helloapp')
def helloapp():
    return "Hello From Seytech!"

@app.route('/_health')
def health():
    return "OK"

# @app.route('/healthx')
# def healthx():
#     time.sleep(1);
#     return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

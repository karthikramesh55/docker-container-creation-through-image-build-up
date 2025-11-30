from flask import Flask

app = Flask(__name__)

@app.route('/')
def kata_app_serving_functionality():
    return "The kata app is currently running successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
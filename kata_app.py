from flask import Flask
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def kata_app_serving_functionality():
    data = {
        "name": "Karthik Ramesh Kamath",
        "datetime": datetime.now().isoformat(),
        "journey": "Seeker"
    }
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
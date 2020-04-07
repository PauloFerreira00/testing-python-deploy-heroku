import os
from flask import Flask
from flask_cors import CORS 
import requests

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "* "}})

@app.route("/", methods=["GET"])
def index():
    return get_json()

def get_json():
    response = requests.get("http://api.open-notify.org/astros.json")
    if response.status_code == 200: 
        return response.text
    else:
        return "{}"

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port )

if __name__ == "__main__":
    main()
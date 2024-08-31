import requests
from flask import Flask, jsonify

 
app = Flask(__name__)

hafez_url = "http://127.0.0.1:5001/fal"
khayyam_url = "http://127.0.0.1:5002/today"

def hafez():
    response = requests.get(hafez_url)
    return response.json().get("fal")

def khayyam():
    response = requests.get(khayyam_url)
    return response.json().get("today")
 
@app.route("/", methods=['GET'])
def main():
    hafez = hafez()
    today = khayyam()
    return jsonify({"fal": hafez, "today": today})
 
if __name__ == "__main__":
    app.run(port=5000)
    
from khayyam import JalaliDatetime
from flask import Flask, jsonify


 
app = Flask(__name__)
 
@app.route("/today", methods=['GET'])
def get_today():
    today = JalaliDatetime.now().strftime('%C')
    return jsonify({"today": today})
 
if __name__ == "__main__":
    app.run(port=5002)

from flask import Flask, jsonify
import hafez 
app = Flask(__name__)
 
@app.route("/fal", methods=['GET'])
def generate_fal():
    omen1 = hafez.omen()
    omen1 = omen1["interpretation"]
    return jsonify({"fal": omen1})
 
if __name__ == "__main__":
    app.run(port=5001)
    
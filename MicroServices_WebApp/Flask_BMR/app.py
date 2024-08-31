from flask import Flask, request, jsonify,render_template,redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
           return {"hello":"world"}

@app.route('/process_data', methods=['POST'])
def process_data():
    # Get the JSON data from the request
    data = request.get_json()

    # Extract the variables
    height = data.get('height')
    weight = data.get('weight')
    gender = data.get('gender')
    age= data.get('age')

    if gender == "female":
            result = (10 * weight) + (6.25 * height) - (5 * age) - 161
            response={"result": result}
            print(response)
            return jsonify(response)

    elif gender == "male":
            response = (10 * weight) + (6.25 * height) - (5 * age) + 5 
            return jsonify(response), 200
    else:
             return render_template("BMR.html")
    # Perform your processing here
    # For this example, let's just return the received data
   
    


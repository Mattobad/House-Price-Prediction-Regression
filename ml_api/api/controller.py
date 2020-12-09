from flask import Blueprint, request, jsonify
from regression_model.predict import make_prediction

from  flask_cors import CORS

prediction_app = Blueprint('prediction_app',__name__)

CORS(prediction_app)

@prediction_app.route('/', methods=['GET'])
def index():

    title = "Full-Stack Data Science for House Price Prediction"
    heading = "This is the web app as final step for Full-Stack Data Science project. Code for the full life cycle of the project can be found from the link below."
    return jsonify({'title': title,
                    'heading': heading
                    })

@prediction_app.route('/health',methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'

@prediction_app.route('/v1/predict/regression',methods=['POST'])
def predict():
    if request.method == 'POST':
        # step:1 Extract Post data from request body as JSON
        json_data = request.get_json()
        print(f'User input from UI: {json_data}')


        # step 3: model prediction
        result = make_prediction(input_data=json_data)

        # step 4: Convert numpy ndarray to list
        predictions = round(result.get('prediction')[0],2)

        return jsonify({'prediction': predictions}), 200
     

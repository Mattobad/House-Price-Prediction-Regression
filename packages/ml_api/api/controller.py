from flask import Blueprint, request, jsonify
from regression_model.predict import make_prediction

from api.config import get_logger
#from api.validation import validate_inputs

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app',__name__)

@prediction_app.route('/health',methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'

@prediction_app.route('/v1/predict/regression',methods=['POST'])
def predict():
    if request.method == 'POST':
        # step:1 Extract Post data from request body as JSON
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        # # step:2 Validate the input using marshmallow schema
        #input_data,errors = validate_inputs(input_data=json_data)

        # step 3: model prediction
        result = make_prediction(input_data=json_data)
        _logger.info(f'Outputs: {result}')

        # step 4: Convert numpy ndarray to list
        predictions = result.get('prediction')[0]
        #print(f'prediction from model ==== {predictions}')
        #version = result.get('version')

        return jsonify({'predictions': predictions})
        # return jsonify({'predictions': predictions,
        #                 'errors': errors})


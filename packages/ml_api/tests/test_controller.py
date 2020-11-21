from regression_model.config import config as model_config
from regression_model.processing.data_management import load_dataset

import json
import math

def test_health_endpoint_returns_200(flask_test_client):

    # when
    response = flask_test_client.get('/health')

    # then
    assert response.status_code == 200


def test_prediction_endpoint_returns_prediction(flask_test_client):

    test_data = load_dataset(file_name=model_config.TESTING_DATA_FILE)
    post_json = test_data[0:1].to_json(orient='records')

    #when
    response = flask_test_client.post('/v1/predict/regression',json=post_json)

    #then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']

    assert  math.ceil(prediction) == 122974

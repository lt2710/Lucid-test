#import libraries
import joblib
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from flask import Flask, request, jsonify

# Load the trained model from current directory
model_file='logit.pkl'
logit=joblib.load(model_file)

# Initialise a Flask app
app = Flask(__name__)

# Create API endpoints
# Home
@app.route("/")
def home():
    return "Hello, this is an API to predict logit model for Lucid test. the /predict/ route will accept POSTed data points in json format and return prediction results."

# Predict endpoint accepting POST
@app.route('/predict/', methods=['POST'])
def predict_logit():
    # Read in new data and convert to pandas df
    data_json = request.get_json(force=True)
    data = pd.DataFrame.from_dict(data_json)

    # Use the predict method of the model to get the prediction for unseen data
    result = logit.predict(data)
    
    # return the result back
    return 'Predicted result for the observations ' + ' are: ' + str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
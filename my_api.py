import joblib
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from flask import Flask, request

# Load the trained model from current directory
model_file='logit.pkl'
logit=joblib.load(model_file)

# Initialise a Flask app
app = Flask(__name__)


# Create an API endpoint
@app.route("/")
def home():
    return "Hello, this is an API to predict logit model for Lucid test"

@app.route('/predict')
def predict_logit():
    # Read all necessary request parameters
    f1 = request.args.get('f1')
    f2 = request.args.get('f2')
    f3 = request.args.get('f3')
    f4 = request.args.get('f4')

    # Use the predict method of the model to get the prediction for unseen data
    small = np.array([[f1, f2, f3, f4]])
    unseen = np.append(small,np.repeat(3, 498))
    result = logit.predict(unseen)
    
    # return the result back
    return 'Predicted result for observation ' + str(unseen) + ' is: ' + str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
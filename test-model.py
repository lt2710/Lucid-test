#some code for testing

import joblib
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

model_file='logit.pkl'
logit=joblib.load(model_file)
test = pd.read_csv('data/lucid_dataset_test.csv')
random_sample = test.sample(3)
logit.predict(random_sample)
#this is a sample request to send 3 random points in the test data to the docker container.

import json
import requests
import pandas as pd

#read in test set and random samples
df = pd.read_csv('data/lucid_dataset_test.csv')
random_sample = df.sample(3)

#convert to json
j_data=random_sample.to_json()

#send POST request
r = requests.post('http://localhost:5000/predict/', data=j_data)

#print result
print(r.content)
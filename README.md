## Modeling building and deployment with Python and Docker
Building a classification model with highly imbalance data, and deploy an API for predicting new data in Docker.

Docker image available at: https://hub.docker.com/r/lt2710/lucid-test

## Updates
Model
 - Updated new data and corresponding model files

Docker
 - Changed Python version to 3.7

API
 - Changed the API to Flask from BaseHTTPServer
 - Moved prediction page to /predict/ route
 - Changed default port from 8080 to 5000
 - Added POST request with new data points sent as json
 - Disabled GET request

Docker code to build, run and commit the container: 
cd Documents/GitHub/Lucid-test
docker build -t lt2710/small .
docker run -p 5000:5000 lt2710/small

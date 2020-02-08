# Lucid-test
DS assignment for Lucid
Build a classification model with highly imbalance data, and deploy in Docker.
https://hub.docker.com/r/lt2710/lucid-test


# Docker code to build, run and commit the container
cd Documents/GitHub/Lucid-test
docker build -t lt2710/small .
docker run -p 5000:5000 lt2710/small

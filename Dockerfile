FROM python:3.7
LABEL maintainer "tianlangyi371@gmail.com"
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY my_api.py my_api.py
COPY logit.pkl logit.pkl
CMD python my_api.py 
FROM python:3-slim
ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN python send.py

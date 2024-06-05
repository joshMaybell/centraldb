# syntax=docker/dockerfile:1
FROM python:3.11-alpine
RUN apk update
RUN apk add lsblk
RUN apk add grep
RUN apk add sed
WORKDIR /work
RUN pip install wheel==0.40.0
RUN pip install --no-build-isolation cython==0.29.36 pyyaml==5.4.1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
RUN mkdir src
COPY ./src/ ./src/
WORKDIR /work/src
CMD ["python3", "main.py"]

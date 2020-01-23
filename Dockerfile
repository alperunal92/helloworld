FROM ubuntu:18.04
MAINTAINER Alper Unal "alper.unal92@hotmail.com"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["helloworld.py"]

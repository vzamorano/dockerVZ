FROM python:3.7.11-alpine3.13
EXPOSE 9000
COPY requirements.pip /tmp
WORKDIR /tmp
RUN pip install -r requirements.pip
COPY . /home/src
WORKDIR /home/src
CMD ["flask","run","--port=9000", "--host=0.0.0.0"]
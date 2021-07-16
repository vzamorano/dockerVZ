FROM python:3.7.11-alpine3.13 AS testing
COPY requirements.pip /tmp
WORKDIR /tmp
RUN pip install -r requirements.pip
COPY . /home/src
WORKDIR /home/src
RUN python3 test.py

FROM python:3.7.11-alpine3.13 
COPY requirements.pip /tmp
WORKDIR /tmp
RUN pip install -r requirements.pip
COPY --from=testing /home/src /app
WORKDIR /app
EXPOSE 9001
CMD ["flask","run","--port=9001", "--host=0.0.0.0"]
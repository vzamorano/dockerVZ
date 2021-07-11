# Docker
This is a repository with task about Docker course.

This app exposes the endpoint /dockerEndpoint in the port 9000

# Build the image
Run the next command to build the image

```
docker build -t pythonapp:v0.1 .
```

# Run the image
Run the next command to run the image
```
docker run -d --name homework2 -p 9000:9000 pythonappvz:v0.1
```
Verify if the container is running:
```
docker ps
```
Should be show the next output:
```
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                                       NAMES
f2d6079560cd   pythonappvz:v0.1   "flask run --port=90…"   20 minutes ago   Up 20 minutes   0.0.0.0:9000->9000/tcp, :::9000->9000/tcp   homework2
```

# App in the browser
Go to your browser and put the next URL:
```
<IP Number of your machine>:9000
```
To see the JSON with information
```
<IP Number of your machine>:9000/dockerEndpoint
```

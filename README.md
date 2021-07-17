# Docker
This is a repository with task about Docker course.

This app exposes the endpoint /dockerEndpoint in the port 9001

# Build the image
Run the next command to build the image

```
docker build -t pythonappvz:v0.1 .
```

# Run the image
Run the next command to run the image
```
docker run -d --name homework2 -p 9001:9001 pythonappvz:v0.1
```
Verify if the container is running:
```
docker ps
```
Should be show the next output:
```
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                                       NAMES
f2d6079560cd   pythonappvz:v0.1   "flask run --port=90…"   20 minutes ago   Up 20 minutes   0.0.0.0:9001->9001/tcp, :::9001->9001/tcp   homework2
```

# App in the browser
Go to your browser and put the next URL:
```
<IP Number of your machine>:9001
```
To see the JSON with information
```
<IP Number of your machine>:9001/dockerEndpoint
```
![Docker](https://1000logos.net/wp-content/uploads/2017/07/Docker-Logo-500x148.png)
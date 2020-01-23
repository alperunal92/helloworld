# Python Flask Dockerized #

```bash
$ git clone https://github.com/alperunal92/helloworldtask.git
```

```bash
$ cd helloworldtask
```

Build the image using the following command

```bash
$ docker build -t alperunal92/helloworld:latest .
```

Run the Docker container using the command shown below. (Test Locally)

```bash
$ docker run -d -p 5000:5000 alperunal92/helloworld:latest
```
Docker push the image Dockerhub. The push refers to a repository https://hub.docker.com/r/alperunal92/helloworld

```bash
$ docker push alperunal92/helloworld:latest
```
-----------------------------------------------------------------------------------------------------------------

# Deploy a flask app on AWS Elasticbeanstalk with Docker

```bash
Show a Dockerrun.aws.json file here -> https://github.com/alperunal92/helloworld/blob/master/Dockerrun.aws.json
```

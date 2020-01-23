# Python Flask Dockerized #

```bash
$ git clone https://github.com/alperunal92/helloworldtask.git
```

```bash
$ cd helloworldtask
```

Build the image using the following command

```bash
$ docker build -t helloworld:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 helloworld
```

# GitHub Actions deploy Flask to AWS Elastic Beanstalk

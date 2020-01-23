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

# Deploy a flask app on AWS Elastic Beanstalk with Docker

```bash
Show a Dockerrun.aws.json file here -> 
```
https://github.com/alperunal92/helloworld/blob/master/Dockerrun.aws.json

# Deployment of the AWS Elasticbeanstalk you can see the Elastic Beanstalk result

![picture](https://github.com/alperunal92/helloworld/blob/master/images/11.PNG)

Once your app has been deployed successfully, navigate to your app URL: http://helloworld-env.rxnur2ffn5.us-west-2.elasticbeanstalk.com/

# Automated CI/CD Pipeline Process

In this section, I will outline how to automate the process to look like this:
New code is pushed up to GitHub.
The Docker image is automatically built and pushed to Docker Hub.
The Elastic Beanstalk app redeploys automatically with the new images pulled from Docker Hub.
I used to manage CI/CD pipeline process on Buddy. Buddy's link is that https://buddy.works/

I created pipeline for project that is "Deploy to Hello World Flask App" 

![picture](https://github.com/alperunal92/helloworld/blob/master/images/12.PNG)

I linked my github repository and aws crendentials for automatically deployment elastic beanstalk.

The pipeline architecture is that

![picture](https://github.com/alperunal92/helloworld/blob/master/images/13.PNG)
![picture](https://github.com/alperunal92/helloworld/blob/master/images/14.PNG)
![picture](https://github.com/alperunal92/helloworld/blob/master/images/15.PNG)

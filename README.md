### Introduction

This is my starting framework for new code challenges that requires a quick API setup.
By default, there is a Dockerfile to build the image. Once that image is generated, 
you can run the container with a new service of Flask, 
a service that allows to create minimal but robust API services.

In addiction, it also provides a docker-compose.yaml file, in case in the future the project requires extra integrations with any other service. Those new services will be mounted in another container, and communication will work internally thanks to docker networks.

##### Why docker
I am using docker since long time, and it is the perfect tool to work as a developer. It allows me to generate full working setups, exactly with same installation that could be in other environment/machines. This minimize the risk of developers having different issue depending on the environment.

###### how to build docker

`docker build -t framework --no-cache .`

I'd like to work always with latest technology, that is why I am using python 3.10. According to the release notes, https://docs.python.org/3.10/whatsnew/3.10.html there has been big improvements on performance.

In requirements.txt also there is no version, as I'd like to work with latest version of each library in my local. Of course in case of docker containers are used in testing/production environment, another requirements.txt with fix version  will be required.


###### how to run docker container

while debugging, use

`docker run --rm -p 8888:8888 --name framework -v $PWD:/app framework`

in production or other env different than local, use:

`docker run --rm -p 8888:8888 --name framework framework`

Even you can run Flask service with:

`docker-compose up`

##### Code organization

Aside from `app.py` file, which is mandatory to start application, I've created two extra folders One to manage and gather other python files related to the application, and another folder for tests. I do believe that unit test are very important, to keep the code clean, and dont break any code that is working. A good coverage of the application can also indicate that it is robust. TDD (Test-Driven Development https://www.guru99.com/test-driven-development.html) is usually my ideal development methodology.

Coverage is tested with command:

`pytest --cov=. `
`pytest --cov=. --cov-report=html --cov-fail-under=95`


Aside from patterns, I'd applied S.O.L.I.D principles in to my code. Some nice samples can be found here https://gist.github.com/dmmeteo/f630fa04c7a79d3c132b9e9e5d037bfd 

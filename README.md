# MSD_assignment

This is an MSD task assignment.

There are three files
 a. Dockerfile
 b.EC2.txt
 c.main.py

main.py has the code that takes the file and prints out the top 10 most common successive words in the plain text

EC2.txt is the main text file. Which can be use as example as the plain textfile

Dockerfile is used to create the image of the Python script(main.py)


I have created docker image of this dockerfile and it is available on hub.docker.com
name of image: noumangul/python-msd1:python-msd1
link: https://hub.docker.com/layers/noumangul/python-msd1/python-msd1/images/sha256:4dfc2aacf375d67e8dc1d651b721190d2f6c5a56fb179a78cefc7539065ed139?tab=layers


######Docker command

Here are the docker commands I use to build the image

to build the docker image from docker file: 
docker build . -t python-msd-optimize



to build the container and execute the script:
docker build . -t python-msd-optimize

to run the image and create container
 docker run -d --name webserver python-msd1

to keep the container running:
docker run -d -t python-msd1 ,
-d: run container in the background,
-t: launch virtual envirnoment to keep container running

to check how many containers are running:
docker ps

To go inside the container:
docker exec -it 10bbe8c83279 /bin/bash

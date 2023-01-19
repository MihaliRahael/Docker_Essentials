# Docker Essentials

## Content

-   What is docker and why is it needed?
-   Docker image vs container
-   Virtual machines Vs Dockers
-   Docker basic commands
-   Create a docker image and run it as a container
-   Put our custom image into docker hub
-   Put our custom image into docker hub
-   Setup environment variable

## What is docker and why is it needed?

Docker is a set of, platform as a service products that uses OS-level virtualization to deliver software in packages called containers. A container is the same idea of a physical container like a box with an application in it. Inside the box the application seems to have its own ip address, and machine name, and it also has its own disk drive. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. All the containers in a system uses the same OS kernel.

Suppose we have 3 containers which contains services of python, Cassandra and Redis in each container respectively. Every container has its own IP, hostname, process, network and mounts. Using these services, we can build an application with these different containers by communicating them each other by sharing same OS kernel.

Suppose a person is moving from House A to B. As part of shifting he can move each and every items within the house one by one. But there is a higher probability of missing some products to move. Instead, pack everything in a container and shifting will reduce the prob of missing anything. Similarly consider a case of a project team which contains dev team and testing team. Dev team has created an ML application which contains all the files (ipynb, procfile, requirements, pickle etc). If we don’t create this application without docker and if dev team give this to testing team, they also have to do whatever setup, requirements, installations manually. Because of this, they obviously can face some issues due to configuration, dependencies, hardware or OS changes because Dev team might have different setups and configurations from other teams. Docker resolves all these issues by **standardizes the environment.** Because of this property we just need to **build the docker image once** which contains all the base configurations and requirements and we will try to use the same image in every machines (QA, Prod, Dev, Ops etc) we want to deploy.

## Docker image vs container

A docker image is an immutable file that contains the source code, libraries, dependencies, tools and other files needed for an application to run. A docker container is a virtualized run time environment where users can isolate applications from the underlying system.

From Dockerfile we create an image, and from image we will run the container. Dockerfile contains a set of instructions. This file automatically executes the commands in it and creates an image using the command docker build. The image is then used as a template, which will be basically used to run an application. This application will run inside a container. docker create is the command to create a container from an image.

|                  |
|------------------|
| Etc.             |
| Mongo DB config  |
| Req.text         |
| Python 3.7       |
| Linux base Image |

Layers

we need a base layer which is a base OS where everything is going to run. This layer can be linux base image or windows base image. Upon this we will have python 3.7 image. Above we will have requirements.txt image. Above that MongoDB config image. Likewise all sub images constitutes a big single image. When we run this image in some other person personal machine, container will get created. Whatever operations are running will be inside this container. We can run several containers in one machine. Around 65000 ports enabled for this.

Whenever we need to share the whole config setup, we will share image not container.

| **Docker image**                   | **Docker container**                                        |
|------------------------------------|-------------------------------------------------------------|
| Is a package or artifact           | Running image in another host’s machine creates a container |
| We can move or share this artifact | Once container created- it creates an Isolated environment  |

## Virtual machines Vs Dockers

Virtual machines can also achieve environment standardization. Then what upper hand does docker have? Consider a web server, which typically contains a CPU, RAM, HDD and n/w components. Suppose we create 3 VMs on top of this server. Each VM will be allocated the resources from the web server in a shared manner. Suppose VM1 is not working or hardly used and VM2 and 3 are heavily used. In that scenario the 2 machines cannot take the resources from VM1. Each VMs can use only the respective allocated resources. This is the major disadv of using VMs.

![image](https://user-images.githubusercontent.com/106816732/213420220-d4b71b04-59ce-4150-823a-c0b3ab5c0c94.png)

Docker virtualizes only the application layer. It doesn’t have its own OS kernel, instead it uses host’s OS kernel to interact with its hardware. Whereas in VM it virtualizes application layer and OS kernel. Therefore while creating VM , we need to allocate RAM and HDD whereas in docker its not needed (it uses host’s RAM)

| **Docker**                | **VM**                                                               |
|---------------------------|----------------------------------------------------------------------|
| Image size is small (MBs) | Size will be in GBs                                                  |
| Fast – starts and run     | Slow- OS kernel need to be started, app layer needs to be ready etc. |
| Compatibility issue       | We can install VM in any OS                                          |

Dockers resolves this issue by bringing the concept of virtualization. Say we have a server, on top we will have an OS. And on top of OS we will create dockers. **Each docker will be having its own process id, network config (port no and all) and more importantly root folder**. If D3 is not working, then D1 and D2 can use resources of D3. So the important properties of dockers are :

1.  Environment standardization
2.  Build once, deploy it anywhere
3.  Isolation
4.  Portability – we can take docker container through diff environments and it will be working similar

Dockers saves a lot of time wrt configuration setups cos the entire configuration is basically made within docker image and that can be run as a container anywhere (in our local system or remote server etc) . Docker is not like a virtual machine, but it as like a container which can independently run by communicating with the kernel of the respective OS. So first we will create a docker file. Whatever the information we are written inside the file, it will create a docker image and this docker image can be taken and run within a container ie it can as a docker container.

**Docker with ML**

We will dockerize the requirements.txt which contains all the libraries required and new environment. This docker container can be deployed in any machine we want. There is an important file called wsgi. Say we have a web server which communicates with the flask app (used to create some webapp). Whenever any user request comes, web server will talk to flask via wsgi interface and get the response quickly from flask and then server will show it to the user.

## Docker basic commands

-   **Start a container**

**Docker run nginx –** this will check for the image ‘nginx’, its its not found then it will automatically download from internet. we can run the container as well using this command. we can see the containers running in UI. We can pause or stop it there itself\*\*.\*\*

Images can be web server, mongo DB, python, ubuntu etc

-   **List containers**

**docker ps -** lists the live running containers

**docker ps -a -** lists the stopped and live containers

-   **Stop a container**

**docker stop \< container id\>**

-   **Remove a container**

**docker rm \<container name\> -** make sure to stop the container before removing

-   **List images**

**docker images**

-   **Remove images**

**docker rmi \<image name\>**

-   **Pull an image**

What if we don’t need to run the container instead just need the image.

**docker pull \<image name eg: nginx\>**

docker run ubuntu sleep 120 - run the ubuntu image for 2 mins then shutdown

-   **Running commands inside a container**

**docker run -it ubuntu bash** – This will take inside ubuntu container. We can use all linux commands then after. ‘exit’ will exit from container.

\-i : interactive option - open even if not attached (ie it wont disconnected)

\-t : allocate a pseudo tty (ie it command will create a pseudo terminal)

-   **Pulling an image from docker repository**

docker pull docker/getting-started

![image](https://user-images.githubusercontent.com/106816732/213420303-bfc943f9-72ff-4f5b-999a-6b8669610a5b.png)

Note : we can see the sublayers inside an image getting pulled. Refer layers architecture od docker explained earlier.

![image](https://user-images.githubusercontent.com/106816732/213420329-156c60ed-79ce-4d2a-a136-99f2e1330a37.png)

-   **Run the package/artifact/image**

**docker run -d -p 80:80 docker/getting-started**

\-d : detached mode ie it will run in the backend

\-p : assign port. First 80 is the host port no, and second 80 is container port no. 80:80 is mapping

Check whether the docker container is running using the command **docker ps**. Now the entire application is running in the container. (Container is running in our machine itself, we can check that in docker UI). And we can check the application through our local host address since ports are mapped. So go to 127.0.0.1:80/

**Lets see another example of pulling an image**

Run a jupyter lab using docker image using the command **docker pull rucio/jupyterlab** and **docker run -d -p 88:88.**

## Create a docker image

**Create Dockerfile ( a new file inside our project along other files.)**

**FROM** **python 3.7**– use to select any kind of base image. From the docker hub (all the images are present over here), it will take the particular base image which has linux and on top of it python 3.7. Each image contains several sub layers.

**COPY** **. /app** – Copy all the files (ML application files we created till now) in the current local location to the location (folder) which I have named as ‘app’ in base image ie copying to the ‘app’ folder inside the docker image. We can change the name to anything.

**WORKDIR** **/app** - setting this app folder in base image as the working directory

**RUN** – install the requirements

**EXPOSE \$PORT**– When the docker image runs as container, in order to access the application inside it, we have to expose some port. When we are deploying in cloud, the server will automatically assign this particular port.

**CMD** **gunicorn --workers=4 --bind 0.0.0.0:\$PORT app:app** – This command is used to run my webapp or our entire application. Gunicorn actually helps to run this entire python web application inside the Heroku cloud. Gunicorn is required whenever we try to deploy anything in Heroku platform. Whenever a request is coming to the application workers will divide based on the instances. Say 1000 requests are coming, workers will divide it to four 250 processes to make it easy. 0.0.0.0 IP address will be the local address in the Heroku cloud.

OR

**CMD [“python”,”app.py”] -** This is basically ‘python app.py’ command in linux.

**Build this docker image (Run this in terminal)**

docker build -t welcome-app .

**-t –** pseudo tty

Welcome-app is the image name I have given

Once the installation is done, check docker images and check for welcome-app in the result. Same image can be seen in docker desktop UI.

**Run the newly created docker image**

**docker ps** – check whether any container is running

docker run -d -p 5000:8000 welcome-app

**Test the application deployed using docker by going to the local host address with port, ie 127.0.0.1:5000/ OR 192.64.71.29:5000/ ie system private ip.**

**Note : Whenever we run our flask app, make sure to give the host and port no which should be the host port in docker command above.**

**Lets say we make some changes in docker image files. What to do ?**

**A**: we should remove the existing image and rebuild it.

**Docker rmi -f welcome-app** [-f : forcefully removing to avoid conflicts]

Now rebuild using above commands.

## Put our custom image into docker hub

To push an image to Docker Hub, you must first name your local image using your Docker Hub username and the repository name that you created through Docker Hub on the web.

You can add multiple images to a repository by adding a specific :\<tag\> to them (for example docs/base:testing). If it’s not specified, the tag defaults to latest.

Name your local images using one of these methods:

-   When you build them, using docker build -t \<hub-user\>/\<repo-name\>[:\<tag\>]
-   By re-tagging an existing local image docker tag \<existing-image\> \<hub-user\>/\<repo-name\>[:\<tag\>]
-   By using docker commit \<existing-container\> \<hub-user\>/\<repo-name\>[:\<tag\>] to commit changes

Now you can push this repository to the registry designated by its name or tag.

\$ docker push \<hub-user\>/\<repo-name\>:\<tag\>

The image is then uploaded and available for use by your teammates and/or the community.

**Eg:**

docker build -t bonny_philip/welcome-app

Now we can see a new image in docker images named as bonny_philip/welcome-app

Now push the latest docker using docker push bonny_philip/welcome-app:latest

Latest is the version info

Once pushing is done, image will be available in bonny’s dockerhub. Steffy can run this image in her machine by running the command docker pull bonny_philip/welcome-app

docker images will show the available images in her system.

Run the image using docker run -d -p 8000:5000 bonny_philip/welcome-app

Check whether container is running using the command docker ps

Check the working of docker container by going into the local host address ie 127.0.0.1:8000/

Note that this host port should be mentioned in flask app designed by Bonny.

## Environment variable

Suppose in a particular application we want to make something dynamic which need to be passed during runtime. Eg: user credentials. Consider the below code. Created app.py, build and run the image. Variables are static.

![image](https://user-images.githubusercontent.com/106816732/213420496-50d7d742-5d53-4fed-8d89-910495ff79ec.png)

![image](https://user-images.githubusercontent.com/106816732/213420475-b20cac32-029b-4c99-9d3b-5a9dbaf4b18c.png)

Now I want to make this dynamic so that any user can use this and add any functionality. Then environment variable comes into picture.

![image](https://user-images.githubusercontent.com/106816732/213420543-a56d99d8-990d-442c-928a-f5d850a639c5.png)

Build the new image

![image](https://user-images.githubusercontent.com/106816732/213420555-d1e00883-5317-45be-8a77-74d7e295d6c1.png)

Run the image with dynamic variables

![image](https://user-images.githubusercontent.com/106816732/213420580-d8cb2db0-fd25-4d79-9346-3631475ba12d.png)

**How to inspect all the environment variables**

Running the image with dynamic variables

![image](https://user-images.githubusercontent.com/106816732/213420604-cd6854a2-bdc0-458c-a014-f7151a426f80.png)

**‘docker ps’** will show the running containers. Do the docker inspect which will show all the env variables in the particular image.

![image](https://user-images.githubusercontent.com/106816732/213420631-8559fce6-52d8-4db2-ad50-4b3eade0d87d.png)

![image](https://user-images.githubusercontent.com/106816732/213420665-de130eaa-6db3-4fb5-a5c9-8f3822de2c38.png)

**We can create a specific file for all the environment variables as well. Which is the common practice. The file name would be .env**

![image](https://user-images.githubusercontent.com/106816732/213420704-3301a186-b6f4-481a-8e04-249866ce7be0.png)

![image](https://user-images.githubusercontent.com/106816732/213420726-b8ae9636-abcb-4117-8624-9aa8c64b652a.png)

**Commands and Entry points**

![image](https://user-images.githubusercontent.com/106816732/213420803-e00dee1e-d431-4eb2-8b93-e718375671d8.png)
We can write this in Dockerfile as well.

**Docker Compose**

Docker compose is a tool that was developed to help define and share multi-container applications. With compose we can create a YAML file to define the services and with a single command, can spin everything up and tear it all down.

Say we have 4 containers for Flask app, mongoDb, ansible and Jenkins. We will make containers up using separate docker run \<image name\> command. Using docker compose, using single YAML file we can bring all these up at once.

![image](https://user-images.githubusercontent.com/106816732/213420856-ab08aaaa-073e-437e-9527-6935175322d7.png)

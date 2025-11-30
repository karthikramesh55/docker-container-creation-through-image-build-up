# kata-docker-operations
A kata for docker image build-up + container creation through a Dockerfile
- Configuring a base image (Python 3.8-slim: Ubuntu)
- Creating a requirements.txt file for naming the dependencies for a serving application (kata_app) to run smoothly
- Packaging the source code for the serving application + the aforementioned requirements.txt file
- Configuring the installation of the dependencies on the machine of the image user
- Exposing the parent port to a target port through port forwarding for running the serving application on the latter
- Configuring the execution of the serving application through CMD ["...", "..."]

# Usage:
- The docker image could be built through:
    docker build -t kata-app-image:v1.0
- The information about the docker image could be obtained through:
    docker images
- A docker container could be created from the docker image by running the latter as follows:
    docker run -d -p 6000:6000 kata-app-image:v1.0
- The creation history about the docker container could be obtained through:
    docker ps -a
- The detailed configuration data about the docker container could be obtained through:
    docker inspect <container_identifier>
    docker inspect <container_name>
- The docker container could be stopped through:
    docker stop <container_identifier>
- The docker container could be deleted through:
    docker rm -f <container_name>
- The docker image could be deleted through:
    docker rmi <image_name:image_tag>

# Running the serving application on a target port
Since we created the docker container by running the docker image in a detached mode (-d),
and because we have forwarded the source port (i.e. the port of the container) onto the target port (i.e. the port of the target machine host), we could now verify if the serving application is running successfully through "curl http://localhost:6000" (as we have forwarded the source port 6000 onto the local machine host port 6000)

Last but not least, we could open the serving application on the browser through the target machine host through:
"$BROWSER" http://localhost:6000

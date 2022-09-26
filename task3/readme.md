# Task 3: Docker

## Task name: 
Manage Docker microservices

## Task description: 
Create a docker microservice

## Task preparation
- DEVASC VM installed docker

## Task implementation
1. Check docker in local machine
 `docker --version`
  ![docker-version](task3.1screenshot.JPG) 

2. Pull ntp image from docker hub
 `docker pull cturra/ntp`
  ![docker pull](task3.2screenshot.JPG)

3. Check the result:
 `docker images | grep ntp`
  ![check images](task3.3screenshot.JPG)  

4. Run the docker container
 `docker run --name=ntp --restart=always --detach --publish=123:123/udp cturra/ntp`
  ![docker container](task3.4screenshot.JPG)

5. Check the result
   ![Result](task3.5screenshot.JPG)    
 
## Task troubleshooting
No error occured in this task

## Task verification
 ![Confirm task3](task3.6screenshot.JPG)

# Task 4: Jenkins

## Task name: 
CI/CD Pipeline using Jenkins

## Task description: 
Create a Jenkins pipeline

## Task preparation
- DEVASC VM installed docker and jenkins

## Task implementation
1. Check if jenkins is enable in local machine      
![jenkins run](task4.1screenshot.JPG)    
- Jenkins is available in localhost:8080, we need to take the password to access as admin with this command:     
![Access to jenkins](task4.2screenshot.JPG)

2. Create Agent in Jenkins to perform the task (in this case I use my local VM)    
![Agent](task4.3screenshot.JPG)

3. Create pipeline to do the task     
![pipeline](task4.4screenshot.JPG)   

4. Create script for jenkinsfile to run the job    
![script](task4scriptsceenshot.JPG) 

5. Check the result     
![Result](task4.5screenshot.JPG)         
 
## Task troubleshooting
Got "Permission denied when trying to connect to Docker daemon" when pulling ntp from docker, fixed this by the command `sudo usermod -aG docker jenkins`

## Task verification
![Confirm task4](task4.6screenshot.JPG)

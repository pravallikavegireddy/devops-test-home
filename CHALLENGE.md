# Note from the DevOps Team

Thank you for applying to Modulr! 

This test should take a few hours to complete however we understand everyone has other commitments, so please take your time.

Please commit your changes using git and submit it through greenhouse. Please ensure your submission contains any details you think are relevant to your changes, and that you explain any challenges you might have faced with the test.


## Le Petite Patisserie

You work as a DevOps Engineer for a small development house and the lead engineer on a client, Le Petite Patisserie, has left the company. 

The application is in the early stage of development and you have that engineer's to-do list available in the objectives below. These are now your tasks.

# Objectives

1. Write a Dockerfile that containerises the backend application and update the documentation for running it in `backend/README.md`.
2. Write a Docker Compose file that can be used to run both the backend and frontend containers with one command and document how to use it in the `README.md` in the root of the repository. Both containers should be able to communicate with each other.
3. How would you test the functionality of the running applications? Please write your answer in the answers section of `CHALLENGE.md` and implement your suggestions if you feel comfortable doing so. 
4. If you stop the applications using `docker compose down` and start them again using `docker-compose up`, you will see errors in the logs from the backend. Why is that? How would you fix this problem? Please write your answer in the answers section of `CHALLENGE.md` and implement the fix if you feel comfortable doing so.
5. Le Petit Patisserie now wants to deploy these applications to production. How would you achieve this? What deployment paradigm and tools would you use to do so? Please go into detail and include an architecture diagram with your submission. Assume that the applications will be deployed to AWS (although if you are more familiar with another cloud provider, that's okay too).



# Your Answers

## Question 3
To start with we will do the sanity testing of the application by loading the applictation in the browser in this case and observe the time its taking to load the application.

once the application is loaded we will see if the UI is alligned as per specs with respect to Pain au Chocolat, Croque monsieur and Box of Macarons of all the menu items.

Next, Start the first steps in identifying the functionalities of the application by walking through the items in the menu as provided in this application and then we will develop the input data depending on the specifications and we will figure out the output keeping application specifications and will examine the outputs by comparing actual and expected results.

Next steps would Regression testing and then followed by load testing and we can automate all these check by automation with selenim.

## Question 4
Sorry about this question as i couldnt able to build the backend image . I am facing issues with sqlite db when build a docker image of backend app.

## Question 5
The applications will be deployed to AWS. I use blue-green deployement strategy and the tools  use for this deployment is Elasticbeanstalk.
1.For that we need to configure Dockerrun.aws.json which is similar to docker-compose file. because docker is multi container application so in aws we use ECS for that we need to add Dockerrun.aws.json file.
2. push the code on Github.
3. Integrate with Jenkins
4. Host on AWS elastic Beanstalk.
![architecture](https://user-images.githubusercontent.com/61916849/207135970-ef19553c-af56-4514-b5b1-9a4c660251cc.jpg)

the same application using EC2, you are choosing a more traditional server-based approach instead of a managed serverless approach(in EC2 we manage our own server) 

User
 |
HTTPS Request
 |
EC2 Instance
 |
Node.js + Express Server
 |
Database (RDS / DynamoDB)
 |
S3 (Files)

Create an EC2 instance
Install your runtime (node js)
Deploy your Node.js application(npm install and npm start)
Configure networking
Need to manage scaling !Manage scaling by adding more servers and everything 
           
    	  Users
                  |
              CloudFront(amazon CDN)
                  |
            Load Balancer
                  |
       ---------------------
       |                   |
    EC2 #1              EC2 #2
   Node.js             Node.js
       |                   |
       ---------------------
                  |
              Database

If we go with amplify and lambda 
Client
 |
Amplify Hosting
 |
API Gateway
 |
Lambda
 |
DynamoDB

WE DONT MANAGE SERVERS ANY MORE HERE 
Client
 |
Load Balancer
 |
EC2
 |
Your Node.js server

With EC2, we have more control because we manage the server environment and deploy our application directly onto virtual machines. With serverless services like Lambda and Amplify, AWS manages the infrastructure, scaling, and availability, allowing us to focus more on application development.

A startup might choose Lambda/Amplify for faster development and automatic scaling, while a company with specific infrastructure requirements may choose EC2 for more control.


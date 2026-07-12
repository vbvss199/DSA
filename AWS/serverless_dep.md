Serverless Deployment 

AWS Amplify : serverless deployment 
Deploy React, Angular, Vue, Next.js apps with CI/CD, authentication, APIs, and storage.

AWS Lambda: Serverless backend compute 
Run REST APIs, business logic, image processing, scheduled jobs, AI endpoints.

Amazon API Gateway: API layer
Exposes Lambda functions as REST or HTTP APIs

Amazon DynamoDB:Serverless NoSQL database
User data , application data , sessions

Amazon S3:Static file hosting & storage
React build files, images, documents.

Amazon Cloud Front :CDN 
Fast global delivery of frontend assets.

Amazon Cognito:Authentication
User sign-up, login, JWT tokens, social logins.

AWS AppSync:GraphQL APIs
Real-time GraphQL backend for web/mobile apps

RDS (managed relational databases): Relational Databses 


React / Angular / Next.js Frontend
              |
              ↓
        AWS Amplify
              |
   -----------------------
   |          |          |
Hosting    Auth       APIs
   |          |          |
S3 +      Cognito    Lambda
CloudFront
              |
              ↓
          DynamoDB






REST : lo we define how clients and server communicate via https protocols like GET PUT post delete

If we run a node then it exposes a end point it is https using rest principles it is a rest api 

Client ->HTTPS -> API gateway ->node.js express service 
REST (Representational State Transfer) is an architectural style/convention for designing APIs. It defines how you organize and interact with resources.














GOOGLE serverless deployment 
Cloud Firestore is actually a Google Cloud (GCP) service, but it's also part of the Firebase platform.

Firebase App Hosting or Firebase Hosting: deploy front end applications 
Cloud Functions for Firebase: Run serverless backend code
HTTPS endpoints exposed by Cloud Functions (or API Gateway on GCP if needed): Expose backend APIs
Cloud Firestore: NoSQL database
Cloud Storage for Firebase: Store images, videos, files

Firebase Auth: User authentication
Firebase Cloud Messaging (FCM): Push notifications
Firebase Hosting includes a global CDN: Delivers front end assets quickly 


EC2 = renting an empty apartment
You get the space.
You set up everything yourself.
Amplify = renting a fully managed apartment
The infrastructure is already configured.
You focus on using it.
AWS Amplify is a managed service that simplifies deploying web and mobile applications by handling infrastructure, CI/CD, hosting, and integrations with services like Cognito and Lambda.


STUDY ALL OF THESE THINGS AND MAKE SURE TO TOUCH EVERY POINT IN THE RESUME !!!!

Resources :
https://aws.amazon.com/serverless/ 
https://aws.amazon.com/serverless/ 
https://docs.amplify.aws/?utm_source=chatgpt.com

Fire base
https://firebase.google.com/docs?utm_source=chatgpt.com

http:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview?utm_source=chatgpt.com

Rest APi:
https://github.com/microsoft/api-guidelines?utm_source=chatgpt.com

System Design : Alex xiu and Gaurav Sen !!!!

RESUME : touch every point !!!!


DAY 1: Friday 10 : go through all the amazon services, write notes and revise it !!!




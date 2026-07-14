AWS amplify 
Works with most of the front end frame works 
They provide structure and reusable components for the creating user interfaces 
Integrates with popular front end frame works like react next js angular and vue as well

Amplify supports GraphQl api 
Amplify provides built in authentication and authorisation as well

AWS amplify integrates with the serverless backend services such as lambda , dynamo db and s3, amazon cognito(auth and authorisation) and appsync(graphql )

Continuous integration and continuous delivery (CI/CD) automate the process of integrating code changes and deploying applications.

Amplify streamlines secure and reliable hosting for modern web applications 
This service integrates with github to deploy applications to amplify hosting 

Amplify includes an AI kit that provides tools for incorporating AI services into applications, including pre-built UI components and API interfaces.
With the Amplify AI kit, developers can add sophisticated capabilities like natural language processing and image recognition to their applications.

Amplify offers a suite of pre-built, cloud-connected components that integrate directly with AWS services. These include the Authenticator, Geo capabilities through Amazon Location Services, Face Liveness detection through Amazon Rekognition, and file management tools for Amazon S3.


Lambda runs serverless compute functions when triggered by events. It executes application logic and transforms data.
CloudFront distributes static content from Amazon S3 to users through a global content delivery network. This reduces latency and improves performance.

Amazon Cognito drives the authentication features that Amplify offers
Cognito delivers secure user sign-up, sign-in, and access control. When you add authentication through Amplify, it sets up Amazon Cognito the user and identity pools automatically.
Your application gets pre-built UI components and APIs for authentication. You receive secure, standards-compliant identity management without working directly with Amazon Cognito.
it means Amplify provides ready-made login and signup components that connect to Amazon Cognito behind the scenes.
Amplify will:
Display the login UI.
Talk to Amazon Cognito.
Handle JWT tokens.
Manage sessions.
Refresh tokens automatical

Through the AWS AppSync integration, you can build GraphQL APIs that link your applications to data sources. Define a GraphQL schema in Amplify to create an API layer accessing DynamoDB tables, Lambda functions, and HTTP endpoints.
You receive automated resolver setup, data transformations, and real-time updates. Your application gets live data synchronization across multiple clients without managing the technical details.

Connect to Amazon S3 through Amplify to add secure file storage to your applications. Upload, download, and manage files with straightforward API calls. No direct Amazon S3 configuration is needed.
Amplify creates buckets, applies security settings, and generates secure URLs automatically. You can add features like profile pictures or document sharing while maintaining proper access control.


Run code without managing servers by integrating Amplify with Lambda. By creating functions through Amplify, you set up appropriate roles, memory, and triggers automatically.
You can write business logic while Amplify handles deployment, versions, and service connections. Your computing resources adapt to demand automatically.

Amplify works with Amazon Bedrock to incorporate generative AI capabilities into applications through the Amplify AI kit. Developers can access foundation models through a unified API.
The AI kit supports text generation, code completion, and natural language processing tasks. Applications can use these AI capabilities while maintaining consistent performance and scalability through the Amplify framework.

Amplify Hosting works with AWS WAF to protect web applications. This integration adds security rules and filtering for incoming web traffic.
Developers can implement protection against common web exploits and define custom security rules. The integration helps maintain application security while preserving performance and user experience.


For security , implement proper authentication authorisation through the IAM policies appropriately for secure data transmissions between services 

For monitoring purpose configure Amazons Cloud watch metrics and alarm to track your applications traffic errors data transfer and latency Use CloudWatch Logs and access logs to analyze request patterns.


AWS AppSync manages GraphQL APIs and handles real-time data synchronization.

To develop the application with AWS amplify go to aws console and search for the aws amplify 
Next choose the choose template or deploy app 

To deploy an app choose the provider we can either choose gitlab git github or bitbucket 
The amplify vite template opens in a new browser window create a new repository under this and make it private 

Next choose the front end framework next or react or angular 
And authorize the git with aws amplify 

Set up the code in vs code and clone it for the local dev 
While working with the frontend download the backend configuration file in the aws amplify console its a json file and paste it under the root of the project 

Under data theres a folder called resource.ts wich contains the data resource configuration 
This central location configures the data backend 
A.schema defines the backend data models each a.model creates a model in the dynamo db 

Ampify gives us the pre built components where we dont need to write code it gives us reusable components 
<LoginPage />
<SignupPage />
and handling API calls manually, you can do something like:
<Authenticator>
  <App />
</Authenticator>


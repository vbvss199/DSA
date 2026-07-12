Amazon Lambda: we just write the Lambda functions in any of our languages (node.js or js  or Python)

AWS Lambda is a serverless compute service where you upload a piece of code (a function), and AWS runs that code whenever it is triggered.

AWS Lambda is a serverless compute service that runs your code only when triggered by an event, scales automatically, and charges only for the milliseconds of execution time used. Its key features are:

Run code for virtually any type of application or backend service. Just upload your code as a ZIP file or container image
and Lambda automatically allocates compute execution power and runs your code based on the incoming request or event, for any scale of traffic.
runs rest api, compute backend logic, image processing, and backend logic 

You can use AWS Lambda to preprocess data before feeding it to your machine learning model. With Lambda access to EFS, you can also serve your model for prediction at scale without having to provision or manage any infrastructure.

Execute code in response to triggers such as changes in data, shifts in system state, or actions by users. Lambda can be triggered by AWS services such as S3, DynamoDB, Kinesis, or SNS, and can connect to existing EFS(Elastic File System for Serverless File System) file systems or to workflows with AWS Step Functions

Example: We just write the Node.js function, which will be triggered by any call to the function by any user 

exports.handler = async (event) => {
    const user = event.userId;

    // business logic
    const result = await getUser(user);

    return {
        statusCode: 200,
        body: JSON.stringify(result)
    };
};
AWS Lambda executes this function when something triggers it.

Trigger1: HTTP request-> api gateway ->aws lambda(function or code) ->dynamodb

Trigger 2:image uploaded->S3 event ->aws lambda ->resize function

AWS Lambda is a serverless compute service that runs our backend functions without managing servers. We can write business logic in Node.js, and Lambda executes it in response to events such as API Gateway requests, database changes, or file uploads





The cloud provider fully manages these servers, meaning they handle provisioning, scaling, security, and isolation. This allows developers to focus on their applications without the overhead of managing infrastructure.

Lambda supports multiple runtimes 
Each major release of a supported programming language comes with a unique runtime identifier, such as nodejs20.x or python3.13, allowing you to select the version that best suits your application requirements.

Lambda Invocations:
Synchronous invocation :
Asynchronous invocation: 
Event Source Mapping:

Batching enables high-throughput message processing, allowing up to 10,000 messages per batch.

Lambda functions sit idle and cost nothing until triggered by an event from another AWS service or endpoint. Billing is based on the number of requests and the duration of execution in milliseconds, with no charge when code is not running.
Reduces operational complexity by handling infrastructure automatically. Improves developer productivity and speeds up project delivery.

Works mainly in these three ways
Trigger (event source ): An event occurs, such as a file uploaded to S3, an HTTP request hitting API Gateway, or a message arriving in an SQS queue.
Lambda Function: AWS spins our code to process the specific event 
Destination (downstream event): The function performs an action, such as saving data to DynamoDB, returning an HTTP response, or writing a processed file back to S3.
 A new image uploaded to an S3 bucket triggers a Lambda function that resizes the image and saves the result to a separate S3 bucket.

Image Processing :
Serverless Backend: An HTTP request hits API Gateway; Lambda runs the logic to fetch data and return it to the user.
File Processing: A user uploads a photo to S3; Lambda triggers instantly to create a thumbnail version.

AWS Lambda offers a generous Free Tier that includes 1 Million requests and 400,000 GB-seconds of compute time per month forever. Beyond the free tier, you are billed on two factors:
*** If your code is inefficient and takes 10 seconds to run, you pay for 10 seconds. If you optimize it to run in 200ms, your bill drops significantly.****
Real-time File Processing: Trigger a function to resize images, transcode videos, or perform OCR on documents as they are uploaded to S3.
Serverless Web Backends: Use Amazon API Gateway to create a REST API that triggers Lambda functions to handle HTTP requests for your web or mobile application.
Data Processing (ETL): Process and transform real-time data from streams like Amazon Kinesis or DynamoDB Streams.
Automation / "Cron in the Cloud": Schedule functions to run at regular intervals using Amazon EventBridge to perform tasks like generating daily reports, cleaning up resources, or running backups.


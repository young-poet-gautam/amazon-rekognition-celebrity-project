# amazon-rekognition-celebrity-project
This project leverages AWS Rekognition to recognize celebrities in images uploaded to an S3 bucket. The solution triggers an AWS Lambda function to process the image using Rekognition's RecognizeCelebrities API. Once processed, the recognized celebrity names are logged in CloudWatch Logs.

# Celebrity Recognition using AWS Rekognition

This project uses **AWS Rekognition** to recognize celebrities from images uploaded to an **S3 bucket**. When an image is uploaded, a **Lambda function** is triggered, which calls Rekognition's `RecognizeCelebrities` API to identify celebrities in the image.

## Services Used:
- AWS Lambda
- Amazon S3
- Amazon Rekognition
- CloudWatch (for logging)

## Project Setup:

### 1. AWS Configuration:
- Create an S3 bucket to upload images.
- Create a Lambda function with the provided `lambda_function.py`.
- Ensure your Lambda function has appropriate IAM roles (S3, Rekognition, CloudWatch access).
  ![image](https://github.com/user-attachments/assets/f34c9b06-02fb-44cf-9099-398ad8ce0000)


### 2. Deploying the Lambda Function:
- Upload the `lambda_function.py` to AWS Lambda.
- Set up the S3 bucket to trigger Lambda on new image uploads.
![image](https://github.com/user-attachments/assets/d93d38f1-82de-42c3-b8f9-a4cdd4c16896)

### 3. Example Images:
The `assets/` directory contains two test images:
- `testimage1.jpg` - Jackie Chan
- `testimage2.jpeg` - Shahrukh Khan
![image](https://github.com/user-attachments/assets/2a33e457-ae1e-4add-b788-f803d6dbe9cb)


### 4. CloudWatch Logs:
You can check the recognized celebrities' names in **CloudWatch Logs** after an image is uploaded.
![image](https://github.com/user-attachments/assets/19756787-ad81-4a33-81f9-1e9c9acac1c0)


## Dependencies:
- Python 3.x
- Boto3

## To Do:
- Extend functionality to store recognized celebrity names in S3.
- Add CloudFormation script to automate setup.

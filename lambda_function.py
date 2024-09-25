import json
import boto3
import os

# Initialize Rekognition and S3 clients
rekognition_client = boto3.client('rekognition')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Get the bucket and image key from the S3 trigger event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Log bucket and key for debugging
        print(f"Image received from bucket: {bucket}, key: {key}")
        
        # Ensure the file is an image (optional but recommended)
        if not key.lower().endswith(('.png', '.jpg', '.jpeg')):
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'File type not supported. Please upload PNG, JPG, or JPEG images.'
                })
            }

        # Call Amazon Rekognition to recognize celebrities in the image
        response = rekognition_client.recognize_celebrities(
            Image={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': key
                }
            }
        )

        # Retrieve and log the names of recognized celebrities
        celebrity_names = [celebrity['Name'] for celebrity in response['CelebrityFaces']]

        if celebrity_names:
            print(f"Recognized celebrities: {', '.join(celebrity_names)}")
        else:
            print("No celebrities recognized.")
        
        # Return the list of recognized celebrities
        return {
            'statusCode': 200,
            'body': json.dumps({
                'recognized_celebrities': celebrity_names
            })
        }
    
    except Exception as e:
        print(f"Error processing image: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error occurred while processing the image',
                'error': str(e)
            })
        }

import json
import boto3
import os

sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event['body'])
        name = body.get('name')
        email = body.get('email')
        message = body.get('message')

        # SNS Message
        sns_message = f"""
New Feedback Received!

Name: {name}
Email: {email}
Message: {message}
        """

        sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Message=sns_message.strip(),
            Subject='New Feedback Submission'
        )

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'PUT,OPTIONS'
            },
            'body': json.dumps({'message': 'Feedback submitted successfully!'})
        }
        
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': 'Error submitting feedback'})
        }

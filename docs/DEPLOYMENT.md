# Deployment Steps

## Step 1: Create SNS Topic
1. Go to SNS Console
2. Create Topic (Standard)
3. Subscribe Email endpoint

## Step 2: Create Lambda
- Runtime: Python 3.14
- Code: See lambda/index.js
- Add Environment Variable: SNS_TOPIC_ARN
- Attach IAM Policy for SNS publish

## Step 3: API Gateway
- Create REST API
- Create Resource: feedback
- Methods: OPTIONS (CORS), PUT (Lambda integration)
- Deploy API

## Step 4: S3 Static Website
- Create bucket
- Enable static website hosting
- Upload frontend files
- Set bucket policy for public read

## Step 5: Update Frontend
Replace API_ENDPOINT in index.html with your API Gateway URL

## Step 6: Test
Submit form and check email

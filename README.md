# AWS Static Website with Feedback Form using S3, Lambda, SNS, API Gateway

## Overview
This project deploys a static website on S3 with a feedback form. The form submits data via API Gateway to a Lambda function, which publishes to SNS for email notifications.

## Architecture
- **S3**: Hosts static website (index.html with feedback form)
- **API Gateway**: REST API with /feedback resource (OPTIONS for CORS, PUT for submission)
- **Lambda**: Processes feedback and publishes to SNS
- **SNS**: Topic for email notifications

## Prerequisites
- AWS Account
- AWS CLI configured
- AWS Management Console access
- Python 3.12 for Lambda

## Setup Steps

### 1. Clone and Navigate
```bash
git clone <your-repo>
cd feedback-static-site-aws
```

### 2. Manual Setup (Console)

### 3. Lambda Code
See `lambda/`

### 4. Frontend
See `frontend/index.html`

### 5. Deployment Steps
Detailed in docs/DEPLOYMENT.md

### Workflow Diagram
See `docs/WORKFLOW.md` (Mermaid diagram)

## Features
- CORS enabled
- Secure permissions (IAM roles)
- Email notifications via SNS

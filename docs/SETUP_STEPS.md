# Complete Step-by-Step Setup Guide

## Phase 1: SNS Topic (Create First)

1. AWS Console → SNS → Topics → **Create topic**
2. Name: `feedback-topic`
3. Type: Standard
4. After creation → **Create subscription**
   - Protocol: **Email**
   - Endpoint: Your email address
   - Confirm the subscription from your email

**Note**: Copy the Topic ARN (you will need it in Lambda)

---

## Phase 2: Lambda Function

1. AWS Console → Lambda → **Create function**
2. Function name: `feedback-processor`
3. Runtime: **Python 3.12**
4. Architecture: x86_64
5. **Create function**

**Upload Code**:
- Paste the code from `lambda/index.py`

**Environment Variables**:
- Key: `SNS_TOPIC_ARN`
- Value: Your SNS Topic ARN

**Permissions (IAM Role)**:
- Attach this policy to the Lambda execution role:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Allow",
      "Action": "sns:Publish",
      "Resource": "arn:aws:sns:*:*:feedback-topic"
    }]
  }
  ```

---

## Phase 3: API Gateway

1. API Gateway → **Create API** → REST API
2. API name: `feedback-api`
3. **Create Resource**:
   - Resource Name: `feedback`
4. **Create Method**:
   - **PUT** method on `/feedback`
   - Integration Type: **Lambda Function**
   - Select your Lambda function
5. **Enable CORS**:
   - Actions → Enable CORS
6. **OPTIONS** method will be added automatically

**Deploy API**:
- Actions → Deploy API → New Stage (e.g., `prod`)
- Copy the Invoke URL (update it in `index.html`)

---

## Phase 4: S3 Static Website

1. S3 → **Create bucket**
   - Name: unique name (e.g., `my-feedback-site-2026`)
   - Uncheck "Block all public access"
2. Upload `frontend/index.html` to the bucket
3. **Properties** → Static website hosting → Enable
   - Index document: `index.html`
4. **Permissions** → Bucket Policy:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Sid": "PublicReadGetObject",
       "Effect": "Allow",
       "Principal": "*",
       "Action": "s3:GetObject",
       "Resource": "arn:aws:s3:::your-bucket-name/*"
     }]
   }
   ```

---

## Phase 5: Final Testing

1. Open the S3 website URL
2. Fill the form and submit
3. You should see success message
4. Check your email for notification

**Troubleshooting**:
- CORS error → Check CORS settings in API Gateway
- Permission error → Verify Lambda IAM role
- No email → Confirm SNS subscription

---

**Pro Tip**: For production, consider using Terraform or AWS SAM for Infrastructure as Code.

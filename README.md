# severless-application
# AWS Serverless Student Registration Application

A serverless web application for registering students using AWS services. The project uses AWS Lambda, Amazon API Gateway, and a frontend built with HTML, CSS, and JavaScript.

## 📌 Project Overview

The **Student Registration Application** allows users to enter student details such as name and email through a web interface. The data is processed by an AWS Lambda function through an API endpoint.

This project demonstrates a serverless architecture where there is no need to manage servers manually.

## 🏗️ Architecture

```
User
 |
 | 
Frontend (HTML + CSS + JavaScript)
 |
 |
API Gateway
 |
 |
AWS Lambda Function
 |
 |
Database (DynamoDB / Storage Layer)
```

## 🚀 Features

* Student registration form
* Serverless backend using AWS Lambda
* REST API integration using AWS SAM
* Frontend hosted separately from backend
* JSON-based API communication
* Scalable and cost-effective architecture

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* AWS Lambda
* AWS SAM (Serverless Application Model)

### AWS Services

* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB
* AWS CloudWatch

### Tools

* Git & GitHub
* Visual Studio Code
* AWS SAM CLI
* Docker

## 📂 Project Structure

```
aws-serverless-student-registration/

│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambda/
│   ├── app.py
│   ├── database.py
│   └── utils.py
│
├── events/
│   └── event.json
│
├── tests/
│   ├── test_api.py
│   └── test_lambda.py
│
├── screenshots/
│
├── template.yaml
├── requirements.txt
├── README.md
└── samconfig.toml
```

## ⚙️ Prerequisites

Before running the project, install:

* Python 3.x
* AWS CLI
* AWS SAM CLI
* Docker
* Git

Configure AWS CLI:

```bash
aws configure
```

## ▶️ Running the Application Locally

### Step 1: Clone Repository

```bash
git clone <repository-url>
```

Move into project directory:

```bash
cd aws-serverless-student-registration
```

### Step 2: Build SAM Application

```bash
sam build
```

### Step 3: Start Local API

```bash
sam local start-api
```

The API will start at:

```
http://127.0.0.1:3000
```

### Step 4: Run Frontend

Open the `frontend/index.html` file using Live Server.

Frontend will run on:

```
http://127.0.0.1:5500
```

## 🔌 API Endpoint

### Register Student

**Method:**

```
POST
```

**Endpoint:**

```
/students
```

### Request Body

```json
{
    "name": "Vishakha",
    "email": "vishakha@test.com"
}
```

### Response

```json
{
    "message": "Student registered successfully"
}
```

## 🧪 Testing API

Example using PowerShell:

```powershell
curl -Method POST http://127.0.0.1:3000/students `
-Headers @{"Content-Type":"application/json"} `
-Body '{"name":"Vishakha","email":"vishakha@test.com"}'
```

## ☁️ Deployment

To deploy this application on AWS:

Build the application:

```bash
sam build
```

Deploy:

```bash
sam deploy --guided
```

AWS SAM will create required resources automatically.

## 📊 Monitoring

Application monitoring can be performed using:

* AWS CloudWatch Logs
* AWS CloudWatch Metrics
* AWS Lambda Monitoring

## 🔒 Security Considerations

* IAM roles are used instead of hardcoded credentials
* API input validation is implemented
* AWS best practices are followed
* Sensitive information is not stored in source code

## 🎯 Future Enhancements

* Add user authentication using Amazon Cognito
* Deploy frontend using Amazon S3 and CloudFront
* Add complete CRUD operations
* Add automated CI/CD pipeline using GitHub Actions
* Add DynamoDB integration

## 👩‍💻 Author

**Vishakha Jadhav**

MCA Student | AWS & DevOps Learner

Skills:

* AWS Cloud
* Serverless Architecture
* Python
* DevOps Tools
* Web Development

---

⭐ If you find this project useful, consider giving it a star on GitHub.

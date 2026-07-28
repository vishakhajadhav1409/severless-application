import re
import json


def validate_student(data):
    """
    Validate student registration data
    """

    required_fields = ["name", "email", "course"]

    # Check if all required fields exist
    for field in required_fields:
        if field not in data:
            return False, f"{field} is required"

    # Check empty values
    if not data["name"].strip():
        return False, "Name cannot be empty"

    if not data["email"].strip():
        return False, "Email cannot be empty"

    if not data["course"].strip():
        return False, "Course cannot be empty"

    # Email validation
    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if not re.match(email_pattern, data["email"]):
        return False, "Invalid email address"

    return True, "Validation Successful"


def success_response(message, data=None):

    body = {
        "status": "success",
        "message": message
    }

    if data:
        body["data"] = data

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def error_response(message):

    return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "status": "error",
            "message": message
        })
    }
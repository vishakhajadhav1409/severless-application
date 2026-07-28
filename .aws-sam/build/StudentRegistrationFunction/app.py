import json
import uuid

from database import save_student
from utils import validate_student, success_response, error_response


def lambda_handler(event, context):
    try:
        # Read request body
        if "body" not in event:
            return error_response("Request body is missing")

        body = json.loads(event["body"])

        # Validate input
        is_valid, message = validate_student(body)

        if not is_valid:
            return error_response(message)

        # Create student object
        student = {
            "id": str(uuid.uuid4()),
            "name": body["name"],
            "email": body["email"],
            "course": body["course"]
        }

        # Save to DynamoDB
        save_student(student)

        # Return success response
        return success_response(
            "Student Registered Successfully",
            student
        )

    except Exception as e:
        print(f"ERROR: {str(e)}")

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "status": "error",
                "message": str(e)
            })
        }
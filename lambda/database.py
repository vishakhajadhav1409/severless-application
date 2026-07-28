import boto3
import os

# Create DynamoDB resource
dynamodb = boto3.resource("dynamodb")

# Connect to the DynamoDB table
table = dynamodb.Table(os.environ["TABLE_NAME"])


def save_student(student):
    """
    Save a student record into DynamoDB
    """
    response = table.put_item(Item=student)
    return response


def get_student(student_id):
    """
    Retrieve a student by studentId
    """
    response = table.get_item(
        Key={
            "studentId": student_id
        }
    )

    return response.get("Item")


def delete_student(student_id):
    """
    Delete a student record
    """
    response = table.delete_item(
        Key={
            "studentId": student_id
        }
    )

    return response


def get_all_students():
    """
    Retrieve all students
    """
    response = table.scan()
    return response.get("Items", [])
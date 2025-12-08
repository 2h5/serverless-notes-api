import json
import boto3
import os
from botocore.exceptions import ClientError


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def handler(event, context):
    
    if not event["pathParameters"].get("id"):

        return {

            "statusCode": 400,
            "body": json.dumps({"message": "ID not found"})

        }

    data = event["pathParameters"]["id"]
    key_dict = {"noteId": data}
    
    
    try:
        table.delete_item(Key=key_dict,
        ConditionExpression='attribute_exists(noteId)')
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Note successfully deleted"})
        }
    except ClientError as e:
        if e.response["Error"]["Code"] == 'ConditionalCheckFailedException':
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Note not found"})
            }
        else:
            return {
                "statusCode": 500,
                "body": json.dumps({"message": "Test error"})
            }

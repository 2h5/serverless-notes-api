import json
import boto3
import os
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def handler(event, context):
    
    data = json.loads(event["body"])
    # try:
    #     user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
    # except KeyError:
    #     return {"statusCode": 401, "body": "Unauthorized"}

    if not data.get("title") or not data.get("content"):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Note title and content can not be empty."})
        }

    note_id = uuid.uuid4().hex

    item = {
        "noteId": note_id,
        "title": data["title"],
        "content": data["content"],
        "createdAt": datetime.utcnow().isoformat()
    }

    
    
    table.put_item(Item=item)

    
    return {
            "statusCode": 201, 
            "body": json.dumps({"title": data["title"], 
                                "noteId": note_id,
                                "message": "Note created"})
        }

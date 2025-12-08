import json
import boto3
import os
from datetime import datetime



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

    piece = table.get_item(Key=key_dict)  
   
   
    if not piece.get('Item'): 
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Note not found"})
        }
        
    note = json.loads(event["body"])    
    
    if not note.get("title") or not note.get("content"):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Note title and content can not be empty."})
        }

    now = datetime.utcnow().isoformat()   
    
    item = {
        "noteId": data,
        "title": note["title"],
        "content": note["content"],
        "createdAt": piece['Item']['createdAt'],
        "updatedAt": now
    }
    
    if "attachment" in note:
        item["attachment"] = note["attachment"]
        
    table.put_item(Item=item)
    
    return {
            "statusCode": 200, 
            "body": json.dumps({"noteId": data,
                                "title": note["title"],
                                "content": note["content"],
                                "attachment": item.get("attachment"),
                                "createdAt": piece['Item']['createdAt'],
                                "updatedAt": now,
                                "message": "Note Updated"})
                            }

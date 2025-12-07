import json
import boto3
import os



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
        
    else:
        return {
                "statusCode": 200,
                "body":json.dumps({"message": "Note found", 
                                    "note": piece['Item']})
        }
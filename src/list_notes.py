import json
import boto3
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def handler(event, context):
  
    scan = table.scan()
    
    scanned = scan["Items"]
    tables = []
    for items in scanned:
        tables.append(items)
        
    print(tables)

    cleaned = []
    
    
    for note in tables:
        title = note["title"]
        noteid = note["noteId"]
        
        
        new = {
            "title": title,
            "noteId": noteid
        }
        cleaned.append(new)
        
    print(new)
    print(cleaned)
    return {
        
        "statusCode": 200,
        "body": json.dumps({"message": cleaned})
    }
    
  
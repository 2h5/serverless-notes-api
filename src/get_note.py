import json
import boto3
import os


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def handler(event, context):
    

    # resp = table.get_item(Key={"userId": user_id, "id": note_id})
    # item = resp.get("Item")

    # if not item:
    #     return {
    #         "statusCode": 404,
    #         "body": "Not found, unfinished here"
    #     }


    return {


        "statusCode": 200, 
        "body": json.dumps({"message": "API is working, final update for test"})


    }


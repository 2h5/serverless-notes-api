import json
import boto3
import os


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])

def handler(event, context):
    #we are going to do full overwrite, just replace the entire note completely
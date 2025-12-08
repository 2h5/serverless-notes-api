import json
import boto3
import os
import uuid
import mimetypes



s3 = boto3.client("s3")
bucket = os.environ["IMAGE_BUCKET"]

def handler(event, context):
    
    try:
        body = json.loads(event.get("body") or "{}")
    except:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid JSON body"})
        }

    content_type = body.get("contentType")
    
    if not content_type:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Missing 'contentType' in request body"})
        }
    
    extension = mimetypes.guess_extension(content_type)
    
    if not extension:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": f"Unsupported content type: {content_type}"})
        }
        
    
    note_id = event["pathParameters"].get("id")
    if not note_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "ID not provided"})
        }

    file_id = str(uuid.uuid4())
    key = f"images/{note_id}/{file_id}{extension}"
    
    upload_url = s3.generate_presigned_url(
                                            ClientMethod="put_object",
                                            Params={"Bucket": bucket, "Key": key, 'ContentType': content_type},
                                            ExpiresIn=500
    )
    
    download_url = s3.generate_presigned_url(                 
        ClientMethod="get_object",                            
        Params={"Bucket": bucket, "Key": key},                
        ExpiresIn=3600                                       
    )
    
    
    file_url = f"https://{bucket}.s3.amazonaws.com/{key}"
    
    return {
        "statusCode": 200,
        "body": json.dumps({
                            "uploadUrl": upload_url,
                            "downloadUrl": download_url,
                            "fileUrl": file_url,
                            "contentType": content_type,
                            "extension": extension
        })
    }
    
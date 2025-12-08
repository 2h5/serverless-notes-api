# Notes API (Serverless)

This project is a serverless Notes API built with AWS API Gateway, Lambda, DynamoDB, and S3.
It supports creating notes, listing them, updating, deleting, and uploading images using presigned S3 URLs.

Code is split into separate Lambda functions for each action.



## Features

### 1. Create a Note
Creates a new note with a UUID, title, and content.
Code reference: create_note.py

### 2. Get a Single Note
Fetches a note using its noteId.
Code reference: get_note.py

### 3. List All Notes
Scans DynamoDB and returns all notes (title + noteId).
Code reference: list_notes.py 

### 4. Update a Note
Updates a note while preserving createdAt and adding updatedAt.
Code reference: update_note.py

### 5. Delete a Note
Deletes a note using a conditional check so nonexistent notes fail gracefully.
Code reference: delete_note.py

### 6. Presigned Image Upload
Generates presigned S3 PUT and GET URLs for image uploads.
Validates content types and stores files under images/{noteId}/.
Code reference: presign_image_upload.py

## Architecture
API Gateway
→ Lambda functions
→ DynamoDB Notes Table
→ S3 Image Bucket

Lambdas read environment variables (TABLE_NAME, IMAGE_BUCKET) from serverless.yml.

## REST Endpoints (Example)
POST /notes
GET /notes
GET /notes/{id}
PUT /notes/{id}
DELETE /notes/{id}
POST /notes/{id}/images

## Example: Create a Note (Request Body)
{
  "title": "Shopping List",
  "content": "Eggs, Milk, Bread"
}

## Environment Variables
TABLE_NAME = DynamoDB table name
IMAGE_BUCKET = S3 bucket for images

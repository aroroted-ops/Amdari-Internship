import io
import boto3
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account

# --- Configuration ---
# Google Drive Settings
SERVICE_ACCOUNT_FILE =  'path/to/your/credentials.json'
DRIVE_FILE_ID = 'your_drive_file_id_here'
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# AWS S3 Settings
S3_BUCKET_NAME = 'your-s3-bucket-name'
S3_OBJECT_NAME = 'your-desired-s3-object-name'
AWS_ACCESS_KEY = 'your_aws_access_key_here'
AWS_SECRET_KEY = 'your_aws_secret_key_here'


def drive_to_s3():
    # 1. Authenticate Google Drive
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    drive_service = build('drive', 'v3', credentials=creds)

    # 2. Setup S3 Client
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY
    )

    print(f"Downloading file ID {DRIVE_FILE_ID} from Drive...")
    
    # 3. Stream from Drive to a Buffer
    request = drive_service.files().get_media(fileId=DRIVE_FILE_ID)
    file_buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(file_buffer, request)
    
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download Progress: {int(status.progress() * 100)}%")

    # 4. Upload Buffer to S3
    print("Uploading to S3...")
    file_buffer.seek(0)  # Reset buffer pointer to the beginning
    s3_client.upload_fileobj(file_buffer, S3_BUCKET_NAME, S3_OBJECT_NAME)
    
    print(f"Success! File uploaded to {S3_BUCKET_NAME}/{S3_OBJECT_NAME}")

if __name__ == "__main__":
    drive_to_s3()

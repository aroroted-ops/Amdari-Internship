import io
import boto3
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account

# --- Configuration ---
SERVICE_ACCOUNT_FILE = "C:\\Users\\Light\\Documents\\GitHub\\Amdari-Internship\\Sentinel Claims Analytics Platform-Finale Project\\custom-rigging-346209-4b49d0bafa51.json"
# Use the ID of the FOLDER here
FOLDER_ID = '1b0QIHpwSmbV_jeOHAvrxUeOCR0Shvo9K'

S3_BUCKET_NAME = 'amdari-internship-s3-sentinel-claims-analytics-platform'
AWS_ACCESS_KEY = 'AKIA4GWCPJXO3G4QPAF6'
AWS_SECRET_KEY = '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'

def sync_folder_to_s3():
    # 1. Auth
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, 
        scopes=['https://www.googleapis.com/auth/drive.readonly']
    )
    drive_service = build('drive', 'v3', credentials=creds)
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    # 2. List all CSVs in the folder
    # We filter by parent folder ID and ensure we only get CSV files
    query = f"'{FOLDER_ID}' in parents and mimeType = 'text/csv' and trashed = false"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get('files', [])

    if not files:
        print("No CSV files found. Did you share the folder with the Service Account email?")
        return

    for file in files:
        file_id = file['id']
        file_name = file['name']
        
        print(f"Downloading {file_name}...")
        
        # 3. Download to Memory
        request = drive_service.files().get_media(fileId=file_id)
        file_buffer = io.BytesIO()
        downloader = MediaIoBaseDownload(file_buffer, request)
        
        done = False
        while not done:
            status, done = downloader.next_chunk()
        
        # 4. Upload to S3
        file_buffer.seek(0)
        s3_client.upload_fileobj(file_buffer, S3_BUCKET_NAME, file_name)
        print(f"Successfully moved {file_name} to S3.")

if __name__ == "__main__":
    sync_folder_to_s3()
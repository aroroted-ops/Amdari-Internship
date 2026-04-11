import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os

def upload_to_s3(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    file_path = "dataset"
    file_name = os.path.join(file_path, file_name)


    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Initialize the S3 client
    s3_client = boto3.client('s3')

    try:
        print(f"Uploading {file_name} to {bucket}...")
        s3_client.upload_file(file_name, bucket, object_name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except ClientError as e:
        print(f"Unexpected error: {e}")
        return False

# Example Usage
if __name__ == "__main__":
    # Replace these with your actual details
    LOCAL_FILE = 'my_dataset.csv'
    BUCKET_NAME = 'my-cool-datasets-bucket'
    S3_KEY = 'data/2026/my_dataset.csv' # Optional: path inside the bucket

    upload_to_s3(LOCAL_FILE, BUCKET_NAME, S3_KEY)

import boto3
import os
import sys
from botocore.exceptions import NoCredentialsError

print("Loading upload_files.py")

bucketeer_aws_bucket_name = os.environ.get('AWS_BUCKET_NAME', None)
bucketeer_aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', None)
bucketeer_aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', None)


if None in [bucketeer_aws_bucket_name, bucketeer_aws_access_key_id, bucketeer_aws_secret_access_key]:
    print("")
    print("env.AWS_BUCKET_NAME="    , bucketeer_aws_bucket_name)
    print("env.AWS_ACCESS_KEY_ID="    , bucketeer_aws_access_key_id)
    print("env.AWS_SECRET_ACCESS_KEY=", bucketeer_aws_secret_access_key)
    print("")
    print("Error - One or more of required vars is None!")
    print("")
    print("Aborting..")
    sys.exit(1)

db_path = os.path.join('/', 'app', 'db')

session = boto3.Session(
         aws_access_key_id=bucketeer_aws_access_key_id,
         aws_secret_access_key=bucketeer_aws_secret_access_key)


# Create an S3 access object
print(f"Getting client connection to s3 for upload object")
s3_client = boto3.client("s3", aws_access_key_id=bucketeer_aws_access_key_id,
                        aws_secret_access_key=bucketeer_aws_secret_access_key)


def upload_to_s3_bucket(local_file, bucket_dest_file_path):
    print(f"Uploading file: '{local_file}'  -> {bucket_dest_file_path}")
    try:
        s3_client.upload_file(local_file, bucketeer_aws_bucket_name, bucket_dest_file_path)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


# uploaded = upload_to_s3_bucket(r"C:\David\git\elbit-ground-beta\app\db\driving\data_activity.csv", 'driving/data_activity.csv')


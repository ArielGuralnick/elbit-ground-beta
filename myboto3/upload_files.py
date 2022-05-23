
import boto3
import os
import sys

print("upload_files.py")

bucketeer_aws_bucket_name = os.environ.get('AWS_BUCKET_NAME', None)
bucketeer_aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', None)
bucketeer_aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
bucketeer_aws_bucket_region_name = os.environ.get('AWS_REGION_NAME', None)


if None in [bucketeer_aws_bucket_name, bucketeer_aws_access_key_id, bucketeer_aws_secret_access_key, bucketeer_aws_bucket_region_name]:
    print("")
    print("env.AWS_BUCKET_NAME="    , bucketeer_aws_bucket_name)
    print("env.AWS_ACCESS_KEY_ID="    , bucketeer_aws_access_key_id)
    print("env.AWS_SECRET_ACCESS_KEY=", bucketeer_aws_secret_access_key)
    print("env.AWS_REGION="           , bucketeer_aws_bucket_region_name)
    print("")
    print("Error - One or more of required vars is None!")
    print("")
    print("Aborting..")
    sys.exit(1)

db_path = os.path.join('/', 'app', 'db')

session = boto3.Session(
         aws_access_key_id=bucketeer_aws_access_key_id,
         aws_secret_access_key=bucketeer_aws_secret_access_key)


print("Getting session to s3 bucket")
s3 = session.resource('s3')

print(f"Getting bucket: '{bucketeer_aws_bucket_name}'")
my_bucket = s3.Bucket(bucketeer_aws_bucket_name)

# Create an S3 access object
print(f"Getting client connection to s3")
s3_client = boto3.client("s3")


paginator = s3_client.get_paginator('list_objects')
result = paginator.paginate(Bucket=bucketeer_aws_bucket_name, Delimiter='/')
for prefix in result.search('CommonPrefixes'):
    print(prefix.get('Prefix'))

print("")

print("Finished")


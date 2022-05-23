
import boto3
import os

bucket_name = "bucketeer-6a878c84-4c94-43bf-9c1c-7ef1bdebdc5c"

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', None)
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
aws_bucket_region_name = os.environ.get('AWS_BUCKET_REGION_NAME', None)

download_target_path = os.getcwd()

session = boto3.Session(
         aws_access_key_id=aws_access_key_id,
         aws_secret_access_key=aws_secret_access_key)


print("Getting session to s3 bucket")
s3 = session.resource('s3')

print(f"Getting bucket: '{bucket_name}'")
my_bucket = s3.Bucket(bucket_name)

# Create an S3 access object
print(f"Getting client connection to s3")
s3_client = boto3.client("s3")


def download_dir(prefix, local, bucket, client=s3_client):
    """
    params:
    - prefix: pattern to match in s3
    - local: local path to folder in which to place files
    - bucket: s3 bucket with target contents
    - client: initialized s3 client object
    """
    keys = []
    dirs = []
    next_token = ''
    base_kwargs = {
        'Bucket':bucket,
        'Prefix':prefix,
    }
    while next_token is not None:
        kwargs = base_kwargs.copy()
        if next_token != '':
            kwargs.update({'ContinuationToken': next_token})
        results = client.list_objects_v2(**kwargs)
        contents = results.get('Contents')
        for i in contents:
            k = i.get('Key')
            if k[-1] != '/':
                keys.append(k)
            else:
                dirs.append(k)
        next_token = results.get('NextContinuationToken')
    for d in dirs:
        dest_pathname = os.path.join(local, d)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
    for k in keys:
        dest_pathname = os.path.join(local, k)
        if not os.path.exists(os.path.dirname(dest_pathname)):
            os.makedirs(os.path.dirname(dest_pathname))
        client.download_file(bucket, k, dest_pathname)



print("List all files to download")
paginator = s3_client.get_paginator('list_objects')
result = paginator.paginate(Bucket=bucket_name, Delimiter='/')
for prefix in result.search('CommonPrefixes'):
    print(prefix.get('Prefix'))

print("")
print("Downloading all files")
for prefix in result.search('CommonPrefixes'):
    dir_to_download = prefix.get('Prefix')
    print(f"Downloading: {dir_to_download}")
    download_dir(dir_to_download, download_target_path, bucket_name, s3_client)

print("Finished")



import boto3
import os

bucket_name = "bucketeer-6a878c84-4c94-43bf-9c1c-7ef1bdebdc5c"

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID', None)
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY', None)

session = boto3.Session(
         aws_access_key_id=aws_access_key_id,
         aws_secret_access_key=aws_secret_access_key)


#Then use the session to get the resource
print("Getting session to s3 bucket")
s3 = session.resource('s3')

print(f"Getting bucket: '{bucket_name}'")
my_bucket = s3.Bucket(bucket_name)

print("All items in bucket:")
for i in my_bucket.objects.all():
    print(i)



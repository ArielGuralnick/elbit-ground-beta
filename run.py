from app import app
import os
import sys
import boto3

print("Reading env: 'PORT' for listening port assign")
listen_port = os.getenv('PORT', 47382)

# Let's use Amazon S3
s3 = boto3.resource("s3")

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

if __name__ == "__main__":
    # app.run(debug=True, host="127.0.0.1", port=listen_port)  # <- 127.0.0.1 == Access only from localhost
    app.run(debug=True, host="0.0.0.0", port=listen_port)  # Access from any IP - For linux containers / heruko



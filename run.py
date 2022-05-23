from app import app
from myboto3 import download_all_files_from_db
import os
import sys


print("Reading env: 'PORT' for listening port assign")
listen_port = os.getenv('PORT', 47382)

def download_all_files_from_db():
    # Download all files from DB
    bucket_name = os.environ.get('AWS_BUCKET_NAME')
    if not bucket_name:
        print("Error - Missing env: 'AWS_BUCKET_NAME'")
        sys.exit(1)
    print("Downloading all files from DB from bucket: 'bucketeer-6a878c84-4c94-43bf-9c1c-7ef1bdebdc5c'")
    download_all_files_from_db.download_all_files_from_db(bucket_name)

if __name__ == "__main__":
    download_all_files_from_db()
    # app.run(debug=True, host="127.0.0.1", port=listen_port)  # <- 127.0.0.1 == Access only from localhost
    app.run(debug=True, host="0.0.0.0", port=listen_port)  # Access from any IP - For linux containers / heruko

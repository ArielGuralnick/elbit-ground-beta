from app import app
from myboto3 import download_all_files_from_db
import os


print("Reading env: 'PORT' for listening port assign")
listen_port = os.getenv('PORT', 47382)

# Download all files from DB
print("Downloading all files from DB")
download_all_files_from_db.download_all_files_from_db()

if __name__ == "__main__":
    # app.run(debug=True, host="127.0.0.1", port=listen_port)  # <- 127.0.0.1 == Access only from localhost
    app.run(debug=True, host="0.0.0.0", port=listen_port)  # Access from any IP - For linux containers / heruko

from app import app
from myboto3 import download_files
import os
import shutil


print("Reading env: 'PORT' for listening port assign")
listen_port = os.getenv('PORT', 47382)


def reset_local_db():
    try:
        print("Removing db dir at: '/app/db'")
        shutil.rmtree('/app/db')
        print("OK")
    except OSError as e:
        print("Error: %s : %s" % ('/app/db', e.strerror))
    print("Re-creating db dir")
    if os.path.exists('/app/db'):
        print("DB dir already exists. Nothing to do")
        return
    try:
        os.makedirs('/app/db')
        print("Done")
    except OSError as e:
        print("Error: %s : %s" % ('/app/db', e.strerror))


def download_updates_from_db():
    # Download all files from DB
    download_files.download_all_files_from_db()

if __name__ == "__main__":
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        reset_local_db()
        download_updates_from_db()
    # app.run(debug=True, host="127.0.0.1", port=listen_port)  # <- 127.0.0.1 == Access only from localhost
    app.run(debug=True, host="0.0.0.0", port=listen_port)  # Access from any IP - For linux containers / heruko

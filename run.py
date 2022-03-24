from app import app
import os
import sys

print("Reading env: 'PORT' for listening port assign")
listen_port = os.getenv('PORT', 47382)


if __name__ == "__main__":
    # app.run(debug=True, host="127.0.0.1", port=listen_port)  # <- 127.0.0.1 == Access only from localhost
    app.run(debug=True, host="0.0.0.0", port=listen_port)  # Access from any IP - For linux containers / heruko



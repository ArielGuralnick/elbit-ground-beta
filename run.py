from app import app
import os
import sys

print("Reading env: 'PORT' for listening port assign")
listen_port = os.getenv('PORT')
print("Found PORT value:", listen_port)
listen_port = 80
if not listen_port:
    print("Error - Missing env: 'PORT'")
    print("Aborting..")
    sys.exit(1)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=listen_port)  # Access from any IP - For linux containers..
    # app.run(debug=True, host="0.0.0.0", port=listen_port)  # <- 127.0.0.1 == Access only from localhost



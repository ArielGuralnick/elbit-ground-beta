from app import app

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=47382)  # Access from any IP - For linux containers..
    app.run(debug=True, host="127.0.0.1", port=47382)  # <- 127.0.0.1 == Access only from localhost



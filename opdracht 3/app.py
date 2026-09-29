from flask import Flask
import socket
import time
import random

app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()

    slow_request = random.randint(1, 3) == 1

    if slow_request:
        time.sleep(5)
        request_type = "SLOW"
        duration = "5 seconds"
    else:
        request_type = "FAST"
        duration = "0.1 seconds"

    return f"""
    Container: {hostname}<br>
    Type request: {request_type}<br>
    Processing time: {duration}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
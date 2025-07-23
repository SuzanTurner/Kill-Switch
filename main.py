from flask import Flask, request, jsonify

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import status
import json
import os

app = Flask(__name__)
# STATUS_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "status.json"))


# def get_status():
#     with open(STATUS_FILE, "r") as f:
#         status = json.load(f)
#     return status

from pathlib import Path

CONFIG_FILE = Path(__file__).resolve().parent / "config.py"

def get_status():
    status_ = status
    return status_


# @app.route("/update", methods=["POST"])
# def update_status():
#     data = request.json
#     with open(STATUS_FILE, "w") as f:
#         json.dump(data, f, indent=2)
#     return jsonify({"msg": "Status updated ✅", "new_status": data})


@app.route("/update", methods=["POST"])
def update_status():
    data = request.json

    # py_content = f"status = {json.dumps(data, indent=2)}\n"
    py_content = f"status = {repr(data)}\n"

    with open(CONFIG_FILE, "w") as f:
        f.write(py_content)

    return jsonify({"msg": "Status updated ✅", "new_status": data})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

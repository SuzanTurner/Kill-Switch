from flask import Flask, request, jsonify
import sys, os, json, importlib, requests
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import config

app = Flask(__name__)
CONFIG_FILE = Path(__file__).resolve().parent / "config.py"

@app.route("/status", methods=["GET"])
def serve_status():
    importlib.reload(config)
    return jsonify(config.status)

@app.route("/update", methods=["POST"])
def update_status():
    data = request.json
    py_content = f"status = {repr(data)}\n"
    with open(CONFIG_FILE, "w") as f:
        f.write(py_content)
    return jsonify({"msg": "Status updated ✅", "new_status": data})

def fetch_status():
    try:
        res = requests.get("https://kill-switch-lt62.onrender.com/status", timeout=3)
        return res.json()
    except Exception as e:
        print("🔥 Kill switch check failed:", e)
        return {"lock": True, "message": "Default lockdown mode"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

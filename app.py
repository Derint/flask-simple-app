import os
from flask import Flask, jsonify

app = Flask(__name__)

# Read config values from environment variables (injected via ConfigMap)
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "debug")


@app.route("/")
def home():
    return f"Welcome to the Flask App running in {ENVIRONMENT} mode!"


@app.route("/api/status", methods=["GET"])
def status():
    return jsonify(
        {
            "status": "running",
            "uptime": "72 hours",
            "env": ENVIRONMENT,
            "log_level": LOG_LEVEL,
        }
    )


@app.route("/api/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify(
        {
            "user_id": user_id,
            "name": f"User{user_id}",
            "email": f"user{user_id}@example.com",
        }
    )


@app.route("/api/data", methods=["GET"])
def get_data():
    sample_data = {"items": [1, 2, 3, 4], "count": 4}
    return jsonify(sample_data)


@app.route("/api/data/new", methods=["GET"])
def get_data_new():
    sample_data = {"data": [1, 2, 3, 4], "count": 4}
    return jsonify(sample_data)


@app.route("/api/user/info", methods=["GET"])
def user_info():
    return jsonify({"username": "demo_user", "role": "admin", "active": True})


@app.route("/api/metrics/system", methods=["GET"])
def system_metrics():
    return jsonify({"cpu": "25%", "memory": "512MB", "disk": "40% used"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

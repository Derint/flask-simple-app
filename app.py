from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask App!"


@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({"status": "running", "uptime": "72 hours"})


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
def get_data():
    sample_data = {"data": [1, 2, 3, 4], "count": 4}
    return jsonify(sample_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

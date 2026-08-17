from flask import Flask, request, jsonify

app = Flask(__name__)

latest_data = {
    "temperature": None,
    "tds": None,
    "turbidity": None,
    "ph": None
}


@app.route("/")
def home():
    return "Water Quality API is running!"


@app.route("/api/water", methods=["POST"])
def receive_data():

    global latest_data

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No JSON data received"
        }), 400

    latest_data.update(data)

    print("Received:", latest_data)

    return jsonify({
        "status": "success",
        "data": latest_data
    }), 200


@app.route("/api/water", methods=["GET"])
def get_data():

    return jsonify(latest_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

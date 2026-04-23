from flask import Flask, request, jsonify
from app.ecu1_service import ECU1Service
from app.ecu2_service import ECU2Service

app = Flask(__name__)

ecu1 = ECU1Service()
ecu2 = ECU2Service()

@app.route("/set_speed", methods=["POST"])
def set_speed():
    speed = request.json.get("speed", 0)
    ecu1.set_speed(speed)
    return jsonify({"msg": "sent"})

@app.route("/ecu2", methods=["GET"])
def ecu2_status():
    return jsonify(ecu2.get_status())
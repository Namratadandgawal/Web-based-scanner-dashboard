# app.py

from flask import Flask, render_template, request, jsonify, send_file
from scanner import scan_ports
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Scan route
@app.route("/scan", methods=["POST"])
def scan():

    data = request.json

    target = data["target"]
    mode = data["mode"]

    if mode == "top":
        scan_data = scan_ports(target, mode="top")
    else:
        start_port = int(data["start_port"])
        end_port = int(data["end_port"])
        scan_data = scan_ports(target, start_port, end_port)

    scan_data["timestamp"] = str(datetime.now())
    scan_data["target"] = target

    return jsonify(scan_data)


# Download report as TXT
@app.route("/download", methods=["POST"])
def download():

    data = request.json
    filename = "scan_report.txt"

    with open(filename, "w") as f:
        f.write("===== Intelligent Recon Report =====\n")
        f.write(f"Target: {data['target']}\n")
        f.write(f"Time: {data['timestamp']}\n")
        f.write(f"Risk Score: {data['risk_score']}\n\n")

        for item in data["results"]:
            f.write(
                f"Port: {item['port']} | "
                f"Service: {item['service']} | "
                f"Risk: {item['risk']}\n"
            )

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

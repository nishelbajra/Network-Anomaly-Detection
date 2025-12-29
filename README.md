# Network Anomaly Detection

## Project Overview

This repository contains a machine learning framework designed for identifying irregular patterns in network traffic. By analyzing telemetry data, the system provides a high-fidelity approach to detecting potential security threats, unauthorized access attempts, and unusual data exfiltration.

## Core Capabilities

* **Inference Engine**: Uses Scikit-learn to classify network packets based on historical baselines.
* **REST Interface**: Built with Flask to allow for remote data submission and real-time classification.
* **Data Integration**: Compatible with standard network monitoring tools such as Wireshark and tcpdump.
* **Extensibility**: Modular design allows for the integration of new datasets or updated machine learning models.

## Technical Stack

* **Language**: Python 3.10+
* **Framework**: Flask (Web API)
* **Data Science**: Scikit-learn, Pandas, Joblib
* **Data Format**: JSON-based packet telemetry

## Installation and Deployment

### 1. Environment Setup

Clone the repository and install the necessary dependencies:
```bash
git clone https://github.com/webpro255/network-anomaly-detection.git
cd network-anomaly-detection
pip install -r requirements.txt
```

### 2. Service Execution

Initialize the Flask application to start the detection service:
```bash
python3 app.py
```

### 3. API Verification

Submit sample network data to the `/predict` endpoint to verify the detection logic:
```bash
curl -X POST http://<server-ip>:5000/predict \
-H "Content-Type: application/json" \
-d '[{"src_ip": "192.168.0.1", "dest_ip": "192.168.0.2", "src_port": 1234, "dest_port": 80, "protocol": "TCP","packet_size": 100}]'
```

## File Architecture

* **app.py**: Handles API routing and request processing.
* **anomaly_detection.py**: Contains the logic for feature engineering and model prediction.
* **pipeline.pkl**: The serialized model used for classifying traffic.
* **kddcup.data_10_percent**: Reference dataset used for model validation.

## Use Cases

* **Infrastructure Security**: Monitoring small business or home networks for unauthorized traffic.
* **Incident Response**: Assisting security analysts in identifying compromised nodes.
* **Academic Research**: Serving as a baseline for machine learning applications in cybersecurity.

## Development Roadmap

* **Native Packet Capture**: Integration with live network interfaces for direct data ingestion.
* **Reporting Dashboard**: Development of a visualization layer for monitoring anomaly trends.
* **Heuristic Optimization**: Testing deep learning architectures to improve detection accuracy.

## License

This project is available under the MIT License. See the LICENSE file for more details.

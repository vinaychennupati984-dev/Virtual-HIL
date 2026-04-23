# 🚗 Virtual HIL Multi-ECU Simulation (Python)

## 📌 Overview
This project simulates a **Virtual Hardware-in-the-Loop (HIL)** environment with multiple ECUs communicating over CAN.

- ECU1 sends vehicle speed via CAN
- ECU2 receives and processes the signal
- ECU2 applies logic (brake if speed > 80 km/h)
- REST API used to control ECU1
- DBC used for signal encoding/decoding

---

## 🏗️ Architecture

API → ECU1 → CAN → ECU2 → Logic (Brake)

---

## ⚙️ Tech Stack

- Python 3
- Flask (REST API)
- python-can (CAN simulation)
- cantools (DBC parsing)
- pytest (testing)
- Docker (containerization)
- Jenkins (CI/CD)

---

## 📁 Project Structure
virtual_hil/
├── app/
├── can_layer/
├── dbc/
├── tests/
├── system_runner.py
├── client.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile


---

## 🚀 How to Run

### 1. Install dependencies

pip install -r requirements.txt


### 2. Start system

python system_runner.py


---

## 🧪 Run Client (Trigger System)

python client.py


---

## 🔍 Check ECU2 Output

Expected:
{
"speed": 90,
"brake": true
}


---

## 🧪 Run Tests
pytest -v


---

## 🐳 Run with Docker

### Build:
docker build -t virtual-hil .


### Run:

docker run -p 5000:5000 virtual-hil


---

## 🔁 CI/CD (Jenkins)

- Runs pytest on every commit
- Fails build if tests fail

---

## 🎯 Key Features

- Multi-ECU communication simulation
- CAN message encoding/decoding via DBC
- Real-time signal processing
- Automated validation with pytest
- CI/CD ready pipeline

---

## 💬 Interview Summary

> Built a multi-ECU Virtual HIL system using Python where ECUs communicate over CAN using DBC signals, with API control, automated testing, and CI/CD integration.

---

## 📌 Future Enhancements

- UDS diagnostics (Read/Write DTC)
- Real CAN hardware (SocketCAN)
- Live dashboard visualization
- Fault injection scenarios

---

## 👨‍💻 Author
Vinay Chandra
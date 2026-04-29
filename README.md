# 🚗 Virtual HIL Simulation with CI/CD (Python + Docker + Jenkins + TCP Socket)

---

## 📌 Overview

This project implements a Virtual Hardware-in-the-Loop (HIL) simulation using Python.  
It simulates communication between two ECUs over a virtual CAN bus and exposes APIs for interaction.

Additionally, the system now supports **TCP Socket-based communication**, enabling simulation of **Ethernet-style ECU interaction**.

The system is fully automated with:

✅ Automated testing (Pytest)  
✅ Containerization (Docker)  
✅ CI/CD pipeline (Jenkins)  
✅ Image publishing (Docker Hub)  

---

## 🧠 Architecture


Client → Flask API → ECU1 → CAN → ECU2
↑
TCP Socket (NEW)


### Components:

- **ECU1**: Receives speed via API or Socket and sends CAN message  
- **ECU2**: Receives CAN message and updates state  
- **CAN Layer**: Simulates communication between ECUs  
- **API Layer**: Allows REST-based interaction  
- **Socket Layer (NEW)**: Enables TCP/Ethernet-style communication  

---

## ⚙️ Features

🚗 Virtual ECU communication over CAN  
🌐 REST API using Flask  
🔌 TCP Socket communication (NEW)  
🧪 Automated tests using Pytest  
🐳 Dockerized application  
🔄 CI/CD pipeline using Jenkins  
☁️ Docker Hub integration  

---

## 📂 Project Structure


virtual_hil/
│
├── app/
│ ├── api.py
│ ├── ecu1_service.py
│ ├── ecu2_service.py
│
├── can_layer/
│ ├── can_interface.py
│ ├── can_listener.py
│
├── socket_layer/ # NEW
│ ├── socket_server.py
│ ├── socket_client.py
│
├── tests/
│ ├── test_final.py
│ ├── test_system.py
│ ├── test_socket_interface.py # NEW
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── system_runner.py
├── client.py
└── README.md


---

## 🚀 Running Locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt

2️⃣ Run application
python system_runner.py

This will start:

REST API
CAN simulation
TCP Socket server 

3️⃣ Test API
python client.py

4️⃣ Test Socket Communication 
python -m socket_layer.socket_client

🔌 TCP Socket Interface 

This interface simulates Ethernet-based ECU communication.

Supported Commands
Command	Description
ECU1:SET_SPEED:60	Set speed in ECU1
ECU1:GET_STATUS	Get ECU1 status
ECU2:PROCESS_SPEED:90	Process speed in ECU2
ECU2:GET_STATUS	Get ECU2 status
Example Output
ECU1:SET_SPEED:60 -> ACK:ECU1:SPEED_SET:60
ECU1:GET_STATUS -> {'speed': 60}
ECU2:PROCESS_SPEED:90 -> ACK:ECU2:SPEED_PROCESSED:90
ECU2:GET_STATUS -> {'speed': 90, 'brake': True}

🧪 Run Tests
pytest
🧪 Socket Test Cases 
Validate ECU1 speed update via socket
Validate ECU1 status retrieval
Validate ECU2 processing logic
Validate invalid command handling

🐳 Docker Usage
Build image
docker build -t virtual-hil .
Run container
docker run -p 5000:5000 virtual-hil
📦 Run from Docker Hub
docker pull chennupativinaychandra/virtual-hil:latest
docker run -p 5000:5000 chennupativinaychandra/virtual-hil:latest
🔄 CI/CD Pipeline (Jenkins)

Pipeline stages:

Clone code from GitHub
Install dependencies
Run Pytest
Build Docker image
Push image to Docker Hub
🔁 Pipeline Flow
GitHub → Jenkins → Pytest → Docker Build → Docker Hub
⚡ Trigger

Pipeline triggered manually or via GitHub webhook

🧠 Key Learnings
Difference between embedded build vs container build
Running Flask inside Docker (0.0.0.0 binding)
Docker image lifecycle (build → tag → push → pull)
CI/CD automation using Jenkins
Secure credential handling in Jenkins
Multi-interface communication (CAN + REST + Socket)

📈 Improvements
Docker layer caching optimization
Automated testing before image build
Reusable container deployment
Scalable CI/CD pipeline
Extend socket layer to DoIP / SOME-IP

💬 Interview Highlights
Built end-to-end Virtual HIL simulation system
Integrated CAN + REST API + TCP Socket communication
Developed Pytest-based automation for validation
Implemented CI/CD pipeline using Jenkins
Containerized application using Docker

🏁 Conclusion

This project demonstrates a complete automotive-style simulation system combining:

ECU communication (CAN)
Service-based interaction (REST)
Ethernet-style communication (TCP Socket)
Automation (Pytest)
DevOps (Docker + Jenkins)

👉 It represents a scalable validation framework aligned with real-world automotive systems.
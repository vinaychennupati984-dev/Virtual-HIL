# 🚗 Virtual HIL Simulation with CI/CD (Python + Docker + Jenkins)

## 📌 Overview

This project implements a **Virtual Hardware-in-the-Loop (HIL) simulation** using Python.
It simulates communication between two ECUs over a virtual CAN bus and exposes APIs for interaction.

The system is fully automated with:

* ✅ Automated testing (Pytest)
* ✅ Containerization (Docker)
* ✅ CI/CD pipeline (Jenkins)
* ✅ Image publishing (Docker Hub)

---

## 🧠 Architecture

Client → Flask API → ECU1 → CAN → ECU2

* **ECU1**: Receives speed via API and sends CAN message
* **ECU2**: Receives CAN message and updates state
* **CAN Layer**: Simulates communication between ECUs
* **API Layer**: Allows external interaction

---

## ⚙️ Features

* 🚗 Virtual ECU communication over CAN
* 🌐 REST API using Flask
* 🧪 Automated tests using Pytest
* 🐳 Dockerized application
* 🔄 CI/CD pipeline using Jenkins
* ☁️ Docker Hub integration

---

## 📂 Project Structure

```
virtual_hil/
│
├── app/
│   ├── api.py
│   ├── ecu1_service.py
│   ├── ecu2_service.py
│
├── can_layer/
│   ├── can_interface.py
│   ├── can_listener.py
│
├── tests/
│   ├── test_final.py
│   ├── test_system.py
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── system_runner.py
├── client.py
└── README.md
```

---

## 🚀 Running Locally

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run application

```
python system_runner.py
```

### 3️⃣ Test API

```
python client.py
```

---

## 🧪 Run Tests

```
pytest
```

---

## 🐳 Docker Usage

### Build image

```
docker build -t virtual-hil .
```

### Run container

```
docker run -p 5000:5000 virtual-hil
```

---

## 📦 Run from Docker Hub

```
docker pull chennupativinaychandra/virtual-hil:latest
docker run -p 5000:5000 chennupativinaychandra/virtual-hil:latest
```

---

## 🔄 CI/CD Pipeline (Jenkins)

Pipeline stages:

1. Clone code from GitHub
2. Install dependencies
3. Run Pytest
4. Build Docker image
5. Push image to Docker Hub

---

## 🔁 Pipeline Flow

```
GitHub → Jenkins → Pytest → Docker Build → Docker Hub
```

---

## ⚡ Trigger

* Pipeline triggered manually or via GitHub webhook

---

## 🧠 Key Learnings

* Difference between **embedded build vs container build**
* Running Flask inside Docker (`0.0.0.0` binding)
* Docker image lifecycle (build → tag → push → pull)
* CI/CD automation using Jenkins
* Secure credential handling in Jenkins

---

## 📈 Improvements

* Docker layer caching optimization
* Automated testing before image build
* Reusable container deployment
* Scalable CI/CD pipeline

---

## 💬 Interview Highlights

* Built end-to-end HIL simulation system
* Integrated CAN + API communication
* Automated testing and deployment pipeline
* Containerized application for portability

---

## 🏁 Conclusion

This project demonstrates a **complete backend + embedded-style simulation system** with modern DevOps practices.

---

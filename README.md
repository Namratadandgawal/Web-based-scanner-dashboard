# 🛡 Intelligent Recon Dashboard

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/) 
[![Flask](https://img.shields.io/badge/Flask-2.3-green?logo=flask)](https://flask.palletsprojects.com/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 💡 Project Overview

**Intelligent Recon Dashboard** is a web-based **Port Scanning & Risk Analysis Tool** built with Python and Flask.  
It allows cybersecurity enthusiasts and SOC analysts to scan TCP ports, detect services, and generate risk scores for IP addresses or domain targets — all through a clean and interactive web interface.  

This tool is ideal for **educational purposes**, penetration testing labs, and cybersecurity learning projects.

---

## 🚀 Features

- 🔎 **Custom Port Range Scanning**  
- ⚡ **Top 100 Common Ports Scan Option**  
- 📊 **Automated Risk Scoring System**  
- 🖥 **Interactive Web Dashboard**  
- 📁 **Downloadable Scan Reports**  
- 🌐 Supports **IP Addresses & Domain Targets**

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.12 |
| Framework | Flask |
| Networking | Python Socket |
| Production Server | Gunicorn |
| Frontend | HTML, CSS, Bootstrap (optional) |

---

## 📂 Project Structure

web-scanner-dashboard/
│
├── app.py 
├── scanner.py 
├── requirements.txt 
│
├── templates/
│ ├── index.html 
│ └── dashboard.html # Scan results dashboard
│
└── static/ # CSS / JS / assets


---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Namratadandgawal/Web-based-scanner-dashboard.git
cd your-repo-name
2️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run Locally (Windows / Linux)
python app.py
Open your browser:

http://127.0.0.1:5000
📊 Example Scan Output
Target: scanme.nmap.org
Port Range: 1 - 1024

Port 22  - ssh   - Risk: Medium
Port 80  - http  - Risk: Low

Overall Risk Score: 3
📈 Risk Scoring Logic
Low Risk → Common public services (HTTP, HTTPS)

Medium Risk → Remote access services (SSH, FTP)

High Risk → Database ports, exposed admin services

Risk score is calculated based on exposed services and weighted severity.


🔒 Security & Legal Disclaimer
⚠ Educational Purposes Only

Only scan systems you own or have explicit permission to test

Unauthorized scanning may violate cybersecurity laws

The developer assumes no liability for misuse

👩‍💻 Author

Namrata Dandgawal
Defensive Cybersecurity | Threat Detection | SIEM | Digital Forensics |

GitHub: https://github.com/Namratadandgawal

LinkedIn: https://linkedin.com/in/namratadandgawal

# ISS Overhead Notifier

This application sends an email notification every time the International Space Station is passing overhead during nighttime at the user's location.

### 🔧 Technologies Used
- **Python**
- **smtplib** (Email automation)
- **Requests** (APIs)
- **Datetime**
- ISS API and Sunrise-Sunset API

### ✨ Features
- Checks real-time ISS position using public APIs  
- Verifies if it's dark at the user’s location  
- Sends an automated email alert if the ISS is visible  
- Runs continuously as a background script  

### 📂 Files
- `main.py` — Program logic and API requests

### 🎯 Purpose
A project combining **automation**, **API consumption**, and **conditional event alerts**.
